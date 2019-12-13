import pandas as pd
import geopandas as gpd
import variables as var
from shapely import wkt

# validation
# 1. checks if actors were geolocated within their original postcode

import warnings  # ignore unnecessary warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
pd.options.mode.chained_assignment = None


priv_folder = "Private_data/"
pub_folder = "Public_data/"

# READ GEOGRAPHICAL UNITS

# read all postcodes
postcodes = gpd.read_file(pub_folder + 'Administrative_units/Postcodegebied_PC4_WGS84.shp')
postcodes = postcodes[['geometry', 'PC4', 'AMA_post_3']]
postcodes['centroid'] = postcodes['geometry'].centroid

# read all municipalities
municip = gpd.read_file(pub_folder + 'Administrative_units/All_Gemeente_WGS84.shp')
municip = municip[['geometry', 'GM_NAAM']]
municip.rename(columns={'GM_NAAM': 'Name'}, inplace=True)
municip['centroid'] = municip['geometry'].centroid

# read all countries
countries = gpd.read_file(pub_folder + 'Administrative_units/EU_landen.shp')
countries = countries[['geometry', 'NAME']]
countries.rename(columns={'NAME': 'Name'}, inplace=True)
countries['centroid'] = countries['geometry'].centroid
countries = countries[countries['Name'] != 'The Netherlands']

# read all continents
continents = gpd.read_file(pub_folder + 'Administrative_units/continents.shp')
continents = continents[['geometry', 'CONTINENT']]
continents.rename(columns={'CONTINENT': 'Name'}, inplace=True)
continents['centroid'] = continents['geometry'].centroid
continents = continents[continents['Name'] != 'Europe']

admin_areas = pd.concat([municip, countries, continents])

for scope in var.scopes:
# for scope in ['FW']:
# if False:

    INPUT_2 = "Input_{0}_part2/".format(scope)
    PART1 = "Exports_{0}_part1/".format(scope)

    # read a list of all Dutch cities
    citiesNL = pd.read_excel(pub_folder + 'citiesNL.xlsx')

    # read a list of non Dutch cities
    cities = pd.read_excel(pub_folder + 'cities.xlsx')

    # read actors with their locations and postcodes
    locations = pd.read_excel(priv_folder + PART1 + 'Export_LMA_locations.xlsx')

    geolocations = pd.read_csv(priv_folder + INPUT_2 + '{0}_locations_WGS84.csv'.format(scope), encoding='utf-8')
    # !!!! temp fix - remove duplicates
    geolocations.drop_duplicates(subset=['Key'], inplace=True)

    # merge addresses with found geolocations
    geolocations = pd.merge(locations, geolocations, on='Key', how='left')
    unlocated = geolocations[geolocations['WKT'].isna()].copy()
    geolocations.dropna(subset=['WKT'], inplace=True)

    geolocations['WKT'] = geolocations['WKT'].apply(wkt.loads)
    geolocations = gpd.GeoDataFrame(geolocations, geometry='WKT', crs={'init': 'epsg:4326'})

    # do spatial join
    print 'Input files have been read, performing spatial join......'
    spatial = gpd.sjoin(geolocations, postcodes, how='left')

    # do postcode join
    print 'Spatial join has been performed, checking quality'
    spatial['Postcode4'] = spatial['Postcode'].apply(lambda x: str(x)[:4])
    spatial.loc[spatial['Postcode4'] == spatial['PC4'], 'valid'] = True
    spatial.loc[spatial['Postcode4'] != spatial['PC4'], 'valid'] = False

    correct = spatial[spatial['valid'] == True]
    correct = correct[['Key', 'Adres', 'Plaats', 'Postcode', 'Postcode4', 'WKT']]
    incorrect = spatial[spatial['valid'] == False]
    incorrect = incorrect[['Key', 'Adres', 'Plaats', 'Postcode', 'Postcode4', 'WKT']]

    unlocated = unlocated[['Key', 'Adres', 'Plaats', 'Postcode', 'WKT']]
    unlocated['Postcode4'] = unlocated['Postcode'].apply(lambda x: str(x)[:4])

    # check if it is supposed to be in the Netherlands
    # if yes - bring to the centroid of the postcode

    incorrect = pd.concat([incorrect, unlocated])
    in_NL = pd.merge(incorrect, citiesNL, left_on='Plaats', right_on='Woonplaats')
    within_pc = pd.merge(in_NL, postcodes[['PC4', 'centroid']], left_on='Postcode4', right_on='PC4')
    within_pc['WKT'] = within_pc['centroid']

    # if there is no postcode match, check if it is in a right municipality / country
    # if not, then repeat the geolocating process

    no_postcode = incorrect[(incorrect['Key'].isin(within_pc['Key']) == False)]
    no_postcode = pd.merge(no_postcode, cities, left_on='Plaats', right_on='data_name', how='left')

    # update wrong names
    no_postcode.loc[no_postcode['real_name'].isna() == False, 'Plaats'] = no_postcode['real_name']
    no_postcode.drop(columns=['data_name', 'real_name'], inplace=True)
    # merge with the Dutch cities
    no_postcode = pd.merge(no_postcode, citiesNL, left_on='Plaats', right_on='Woonplaats', how='left')
    no_postcode.loc[no_postcode['location'].isna(), 'location'] = no_postcode['Gemeente']
    no_postcode.drop(columns=['Woonplaats', 'Gemeente'], inplace=True)

    # check if it is in a right polygon
    # take out instances without geometry
    no_geom = no_postcode[no_postcode['WKT'].isna()]
    no_postcode = no_postcode[no_postcode['WKT'].isna() == False]
    no_postcode = gpd.sjoin(no_postcode, admin_areas, how='left')

    within_polygon = no_postcode[no_postcode['location'] == no_postcode['Name']]

    wrong_polygon = no_postcode[no_postcode['location'] != no_postcode['Name']]
    wrong_polygon = wrong_polygon[['Key', 'Adres', 'Plaats', 'Postcode', 'location', 'WKT']]
    no_geom = no_geom[['Key', 'Adres', 'Plaats', 'Postcode', 'location', 'WKT']]
    wrong_polygon = pd.concat([wrong_polygon, no_geom])
    wrong_polygon = pd.merge(wrong_polygon, admin_areas, left_on='location', right_on='Name', how='left')
    print wrong_polygon[wrong_polygon['centroid'].isna()]
    wrong_polygon['WKT'] = wrong_polygon['centroid']

    # concatenate all together
    validated = pd.concat([correct, within_pc, within_polygon, wrong_polygon])
    validated.drop_duplicates(subset=['Key'], inplace=True)

    # validate that nothing is missing
    if len(validated.index) == (len(geolocations.index) + len(unlocated.index)):
        print scope, 'geolocations have been validated:'
        print '\t', len(correct.index), 'actors have been assigned to the right postcode'
        print '\t', len(within_polygon.index), 'actors have been assigned to the right administrative area'
        print '\t', len(within_pc.index), 'actors have been relocated to their postcode centroid in the Netherlands'
        print '\t', len(wrong_polygon.index), 'actors have been relocated to their administrative area centroid'
    else:
        print (len(geolocations.index) + len(unlocated.index)) - len(validated.index), 'geolocations have not been validated:'
        non_validated = geolocations[(geolocations['Key'].isin(validated['Key']) == False)]
        print non_validated

    # export validated geolocations
    loc_wgs84 = validated[['Key', 'WKT']]
    loc_wgs84.to_csv(priv_folder + INPUT_2 + '{}_locations_WGS84_validated.csv'.format(scope), index=False)

    # loc_wgs84['WKT'] = loc_wgs84['WKT'].apply(wkt.loads)
    loc_wgs84 = gpd.GeoDataFrame(loc_wgs84, geometry='WKT', crs={'init': 'epsg:4326'})
    loc_RDnew = loc_wgs84.to_crs({'init': 'epsg:28992'})
    loc_RDnew.to_csv(priv_folder + INPUT_2 + '{}_locations_validated.csv'.format(scope), index=False)
