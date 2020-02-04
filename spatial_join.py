# -*- coding: utf-8 -*-
# v. python 2.7
"""
Created on Tue Nov 12 2019

@author: geoFluxus Team

"""

import pandas as pd
import geopandas as gpd
import variables as var
from shapely import wkt

# adds to the analysis files extra columns
# based on waste produced / treated in AMS / AMA

priv_folder = "Private_data/"
pub_folder = "Public_data/"

AMA = gpd.read_file(pub_folder + 'Administrative_units/Metropoolregio_WGS84.shp')
AMS = gpd.read_file(pub_folder + 'Administrative_units/Gemeente2017_WGS84.shp')
AMS = AMS[AMS['GM_NAAM'] == 'Amsterdam']

# read all provinces
provinces = gpd.read_file(pub_folder + 'Administrative_units/Provincie_WGS84.shp')
provinces = provinces[['geometry', 'PROVINCIE']]
provinces.rename(columns={'PROVINCIE': 'Name'}, inplace=True)

# read all countries
countries = gpd.read_file(pub_folder + 'Administrative_units/EU_landen.shp')
countries = countries[['geometry', 'NAME']]
countries.rename(columns={'NAME': 'Name'}, inplace=True)
countries = countries[countries['Name'] != 'The Netherlands']
#
# # read all continents
# continents = gpd.read_file(pub_folder + 'Administrative_units/continents.shp')
# continents = continents[['geometry', 'CONTINENT']]
# continents.rename(columns={'CONTINENT': 'Name'}, inplace=True)
# continents = continents[continents['Name'] != 'Europe']

# read all countries in all other continents
continents = gpd.read_file(pub_folder + 'Administrative_units/world_landen_noEU.shp')
continents = continents[['geometry', 'NAME']]
continents.rename(columns={'NAME': 'Name'}, inplace=True)

admin_areas = pd.concat([provinces, countries, continents])


# admin_areas['centroid'] = admin_areas['geometry'].centroid
# admin_areas = admin_areas[['Name', 'centroid']]
#
admin_areas.to_file(pub_folder + 'Administrative_units/combinded_admin_areas_WGS84.shp')


if False:
# for scope in var.scopes:
# for scope in ['FW']:
    print var.titles[scope]
    EXPORT = "Exports_{0}_part3/".format(scope)
    analysis = pd.read_excel(priv_folder + EXPORT + '{0}_LMA_Analysis_part3.xlsx'.format(scope))

    print 'produced in AMA / AMS'

    analysis['Herkomst_wkt'] = analysis['Herkomst_wkt'].apply(wkt.loads)
    herkomsts = gpd.GeoDataFrame(analysis, geometry='Herkomst_wkt', crs={'init': 'epsg:4326'})

    herkomsts_AMA = gpd.sjoin(herkomsts, AMA, how='left')
    herkomsts_AMS = gpd.sjoin(herkomsts, AMS, how='left')

    print 'country of origin'

    analysis = gpd.sjoin(herkomsts, admin_areas, how='left')
    analysis.drop(columns=['index_right'], inplace=True)
    analysis.rename(columns={'Name': 'orig_country'}, inplace=True)
    analysis.loc[analysis['orig_country'].isna(), 'orig_country'] = 'Noord-Holland'

    print 'treated in AMA / AMS'

    analysis['Verwerker_wkt'] = analysis['Verwerker_wkt'].apply(wkt.loads)
    verwerkers = gpd.GeoDataFrame(analysis, geometry='Verwerker_wkt', crs={'init': 'epsg:4326'})

    verwerkers_AMA = gpd.sjoin(verwerkers, AMA, how='left')
    verwerkers_AMS = gpd.sjoin(verwerkers, AMS, how='left')

    print 'country of destination'

    analysis = gpd.sjoin(verwerkers, admin_areas, how='left')
    analysis.drop(columns=['index_right'], inplace=True)
    analysis.rename(columns={'Name': 'dest_country'}, inplace=True)
    analysis.loc[analysis['dest_country'].isna(), 'dest_country'] = 'Noord-Holland'

    analysis.loc[herkomsts_AMA['index_right'].notna(), 'herkomst_in_AMA'] = 'JA'
    analysis.loc[herkomsts_AMS['index_right'].notna(), 'herkomst_in_AMS'] = 'JA'
    analysis.loc[verwerkers_AMA['index_right'].notna(), 'verwerker_in_AMA'] = 'JA'
    analysis.loc[verwerkers_AMS['index_right'].notna(), 'verwerker_in_AMS'] = 'JA'

    # filter out those entries where both ontdoener and verwerker are outside the AMA
    pre = len(analysis.index)
    analysis = analysis[(analysis['herkomst_in_AMA'] == 'JA') | (analysis['verwerker_in_AMA'] == 'JA')]

    print pre - len(analysis.index), 'flows have been filtered due to being located completely outside of AMA'

    analysis.to_excel(priv_folder + EXPORT + '{0}_LMA_Analysis_part4.xlsx'.format(scope))
