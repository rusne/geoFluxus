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

for scope in var.scopes:
    print var.titles[scope]
    EXPORT = "Exports_{0}_part3/".format(scope)
    analysis = pd.read_excel(priv_folder + EXPORT + '{0}_LMA_Analysis_part3.xlsx'.format(scope))

    print 'produced in AMA / AMS'

    analysis['Herkomst_wkt'] = analysis['Herkomst_wkt'].apply(wkt.loads)
    herkomsts = gpd.GeoDataFrame(analysis, geometry='Herkomst_wkt', crs={'init': 'epsg:4326'})

    herkomsts_AMA = gpd.sjoin(herkomsts, AMA, how='left')
    herkomsts_AMS = gpd.sjoin(herkomsts, AMS, how='left')

    print 'treated in AMA / AMS'

    analysis['Verwerker_wkt'] = analysis['Verwerker_wkt'].apply(wkt.loads)
    verwerkers = gpd.GeoDataFrame(analysis, geometry='Verwerker_wkt', crs={'init': 'epsg:4326'})

    verwerkers_AMA = gpd.sjoin(verwerkers, AMA, how='left')
    verwerkers_AMS = gpd.sjoin(verwerkers, AMS, how='left')

    analysis.loc[ontdoeners_AMA['index_right'].notna(), 'ontdoener_in_AMA'] = 'JA'
    analysis.loc[ontdoeners_AMS['index_right'].notna(), 'ontdoener_in_AMS'] = 'JA'
    analysis.loc[herkomsts_AMA['index_right'].notna(), 'herkomst_in_AMA'] = 'JA'
    analysis.loc[herkomsts_AMS['index_right'].notna(), 'herkomst_in_AMS'] = 'JA'
    analysis.loc[verwerkers_AMA['index_right'].notna(), 'verwerker_in_AMA'] = 'JA'
    analysis.loc[verwerkers_AMS['index_right'].notna(), 'verwerker_in_AMS'] = 'JA'

    analysis.to_excel(priv_folder + EXPORT + '{0}_LMA_Analysis_part4.xlsx'.format(scope))
