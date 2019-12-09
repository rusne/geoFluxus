import pandas as pd
import geopandas as gpd
from shapely import wkt

# validation
# 1. checks if actors were geolocated within their original postcode

# choose scope
while True:
    scope = input('Choose scope: CDW / FW / CG\n')
    if scope == 'CDW' or scope == 'FW' or scope == 'CG':
        break
    else:
        print('Wrong choice.')


priv_folder = "Private_data/"
pub_folder = "Public_data/"

INPUT_2 = "Input_{0}_part2/".format(scope)
PART1 = "Exports_{0}_part1/".format(scope)

# read actors with their locations and postcodes
locations = pd.read_excel(priv_folder + PART1 + 'Export_LMA_locations.xlsx')

geolocations = pd.read_csv(priv_folder + INPUT_2 + '{0}_locations_WGS84.csv'.format(scope), encoding='utf-8')
# !!!! temp fix - remove duplicates
geolocations.drop_duplicates(subset=['Key'], inplace=True)

geolocations['wkt'] = locations['wkt'].apply(wkt.loads)
geolocations = gpd.GeoDataFrame(locations, geometry='wkt', crs={'init': 'epsg:4326'})

# merge addresses with found geolocations
locs = pd.merge(locations, geolocations, on='Key', how='outer')

# read all postcodes
postcodes = gpd.read_file(pub_folder + 'Administrative_units/Postcodegebied_PC4_WGS84.shp')

# do spatial join
print('Input files have been read, performing spatial join......')
spatial = gpd.sjoin(locs, postcodes, how='left')

# do postcode join
print('Spatial join has been performed, performing theoretical join......')
theoretical = pd.merge(spatial, postcodes, left_on='postcode', right_on='PC4', how='left')

# check if spatial and postcode joins match
print(theoretical)
