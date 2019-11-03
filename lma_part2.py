# -*- coding: utf-8 -*-
"""
Built uppon
https://github.com/rusne/LMA-analysis/blob/master/lma_part2.py
Created on Wed Aug 22 09:17:31 2018

@author: geoFluxus Team

"""

import pandas as pd
import geopandas as gpd
import numpy as np
from shapely import wkt

import warnings  # ignore unnecessary warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
pd.options.mode.chained_assignment = None

# ______________________________________________________________________________
# ______________________________________________________________________________

# P R E P A R A T I O N
# ______________________________________________________________________________
# ______________________________________________________________________________

# define years of analysis
years = [2014, 2015, 2016, 2017, 2018]
buffer_dist = 250

roles = ['Afzender', 'Inzamelaar', 'Bemiddelaar', 'Handelaar', 'Ontvanger']

# choose scope: Food Waste, Construction & Demolition Waste, Consumption Goods

while True:
    scope = raw_input('Choose scope: CDW / FW / CG\n')
    if scope == 'CDW' or scope == 'FW' or scope == 'CG':
        break
    else:
        print 'Wrong choice.'

priv_folder = "Private_data/"
pub_folder = "Public_data/"

INPUT = "Input_{0}_part2/".format(scope)
EXPORT = "Exports_{0}_part2/".format(scope)

PART1 = "Exports_{0}_part1/".format(scope)

# ______________________________________________________________________________
# ______________________________________________________________________________

# G I V I N G   N A C E   T O   O N T D O E N E R
# ______________________________________________________________________________
# ______________________________________________________________________________

print 'Loading LMA ontdoeners.......'
LMA_ontodoeners = pd.read_excel(priv_folder + PART1 + 'Export_LMA_ontdoener.xlsx'.format(scope))

print 'Loading LMA locations.......'
LMA_locations = pd.read_csv(priv_folder + INPUT + '{0}_locations.csv'.format(scope))

# ______________________________________________________________________________
# reading all LISA actors
# ______________________________________________________________________________

print 'Loading LISA actors & locations.......'
LISA_actors = pd.read_excel(priv_folder + 'LISA_data/all_LISA_part2.xlsx') # ,
                            # nrows=50000)

# ______________________________________________________________________________
# reading Noord Holland area covered by LISA dataset
# ______________________________________________________________________________

print 'Loading LISA boundary.......'
LISA_boundary = gpd.read_file(pub_folder + 'LISA_boundary.shp')


# ______________________________________________________________________________
# ______________________________________________________________________________

# C O N N E C T I N G   O N T D O E N E R S   W I T H   L I S A
# ______________________________________________________________________________
# ______________________________________________________________________________

# first ontdoeners need to be matched with their locations
ontdoeners = pd.merge(LMA_ontodoeners, LMA_locations, on='Key', how='left')
print ontdoeners['Key'].nunique(), 'ontdoeners in total'

# then all actors that fall out of the LISA boundary need to be filtered out

ontdoeners['WKT'] = ontdoeners['WKT'].apply(wkt.loads)
LMAgdf = gpd.GeoDataFrame(ontdoeners, geometry='WKT', crs={'init': 'epsg:28992'})

joined = gpd.sjoin(LMAgdf, LISA_boundary, how='left')
in_boundary = joined[joined['bound'] == 'boundary']
out_boundary = joined[joined['bound'] != 'boundary']

print in_boundary['Key'].nunique(), 'ontdoeners are inside the LISA boundary'
print out_boundary['Key'].nunique(), 'ontdoeners are outside the LISA boundary'

# further matching only happens for the actors inside the boundary

LMA_inbound = in_boundary[['Key', 'Name', 'Orig_name', 'Jaar', 'Adres', 'Postcode', 'WKT']]

total_inbound = LMA_inbound['Key'].nunique()

# ______________________________________________________________________________
# 1. BY NAME AND ADDRESS
#    year  and role is not important - if both name and address are the same
# ______________________________________________________________________________

LMA_inbound1 = LMA_inbound[['Key', 'Orig_name', 'Adres']].copy()
LMA_inbound1.drop_duplicates(subset=['Key'], inplace=True)

by_name_and_address = pd.merge(LMA_inbound1, LISA_actors, left_on='Key', right_on='key')

# matching control output
control_output = by_name_and_address[['Key', 'Orig_name', 'Adres', 'orig_zaaknaam', 'adres', 'activenq', 'AG']]
control_output['match'] = 1

# OUTPUT BY NAME AND ADDRESS
output_by_name_address = by_name_and_address[['Key', 'activenq']].copy()
output_by_name_address['how'] = 'by name and address'

print len(output_by_name_address.index), 'actors have been matched by name & postcode',
print round(len(output_by_name_address.index) / float(total_inbound) * 100, 2), '%'

# take out those actors that had not been matched
remaining = LMA_inbound[(LMA_inbound['Key'].isin(output_by_name_address['Key']) == False)]

print remaining['Key'].nunique(), 'remaining'

# ______________________________________________________________________________
# 2. BY NAME ONLY
#    geographically closer one gets a priority
# ______________________________________________________________________________

LMA_inbound2 = remaining[['Key', 'Name', 'Orig_name', 'Adres', 'WKT']].copy()
LMA_inbound2.drop_duplicates(subset=['Key'], inplace=True)

by_name = pd.merge(LMA_inbound2, LISA_actors, left_on='Name', right_on='zaaknaam')

by_name['wkt'] = by_name['wkt'].apply(wkt.loads)
# by_name['WKT'] = by_name['WKT'].apply(wkt.loads)

# by_name['dist'] = by_name.apply(lambda by_name: by_name['wkt'].distance(by_name['WKT']), axis=1)
by_name['dist'] = by_name.apply(lambda x: x['wkt'].distance(x['WKT']), axis=1)
closest = by_name.loc[by_name.groupby(['Key'])['dist'].idxmin()]

# matching control output
control_output_2 = closest[['Key', 'Orig_name', 'Adres', 'orig_zaaknaam', 'adres', 'activenq', 'AG']]
control_output_2['match'] = 2
control_output = control_output.append(control_output_2)

# OUTPUT BY NAME
output_by_name = closest[['Key', 'activenq']].copy()
output_by_name['how'] = 'by name'

print len(output_by_name.index), 'actors have been matched by name',
print round(len(output_by_name.index) / float(total_inbound) * 100, 2), '%'

# take out those actors that had not been matched
remaining = remaining[(remaining['Key'].isin(output_by_name['Key']) == False)]

print remaining['Key'].nunique(), 'remaining'

# ______________________________________________________________________________
# 3. BY ADDRESS ONLY
#    correct year gives priority in matching
# ______________________________________________________________________________

LMA_inbound3 = remaining[['Key', 'Orig_name', 'Adres', 'Jaar', 'Postcode']].copy()
LMA_inbound3.drop_duplicates(subset=['Key'], inplace=True)

by_address = pd.merge(LMA_inbound3, LISA_actors, left_on=['Adres', 'Postcode'], right_on=['adres', 'postcode'])

# find those that got matched to only one NACE code
by_address['count'] = by_address.groupby(['Key'])['activenq'].transform('count')
matched_by_address = by_address[by_address['count'] == 1]

print matched_by_address['Key'].nunique(), 'actors have been matched only by address',

ambiguous = by_address[by_address['count'] > 1]

# give priority by year if possible, otherwise discard the matching
temp = pd.DataFrame(columns=ambiguous.columns)
for year in years:
    col = 'in{0}'.format(year)
    m = ambiguous[(ambiguous['Jaar'] == year) & (ambiguous[col] == 'JA')]
    temp.append(m)

ambiguous['count'] = ambiguous.groupby(['Key'])['activenq'].transform('count')
matched_ambiguous = ambiguous[ambiguous['count'] == 1]

print matched_ambiguous['Key'].nunique(), 'additional actors have been matched by address and year'

discard = ambiguous[ambiguous['count'] > 1]
print discard['Key'].nunique(), 'matches have been discarded due to multiple NACE codes'

by_address = pd.concat([matched_by_address, matched_ambiguous])

# matching control output
control_output_3 = by_address[['Key', 'Orig_name', 'Adres', 'orig_zaaknaam', 'adres', 'activenq', 'AG']]
control_output_3['match'] = 3
control_output = control_output.append(control_output_3)

by_address = by_address[['Key', 'activenq']]
by_address.drop_duplicates(inplace=True)

# OUTPUT BY ADDRESS
output_by_address = by_address[['Key', 'activenq']]
output_by_address['how'] = 'by address'

print len(output_by_address.index), 'actors have been matched only by address',
print round(len(output_by_address.index) / float(total_inbound) * 100, 2), '%'

# take out those actors that had not been matched
remaining = remaining[(remaining['Key'].isin(output_by_address['Key']) == False)]

print remaining['Key'].nunique(), 'remaining'
#
# remaining.to_excel('remaining.xlsx')

# ______________________________________________________________________________
# 4. BY PROXIMITY
#    matching on activity group only
#    in case of doubt, assign the closer one
# ______________________________________________________________________________

# remaining = pd.read_excel('remaining.xlsx')
# remaining['WKT'] = remaining['WKT'].apply(wkt.loads)
remaining_geo = gpd.GeoDataFrame(remaining, geometry='WKT', crs={'init': 'epsg:28992'})
# LISA_actors = pd.read_excel(priv_folder + 'LISA_data/all_LISA_part2.xlsx',
#                             nrows=50000)
#
LISA_actors['wkt'] = LISA_actors['wkt'].apply(wkt.loads)
LISA_actors_geo = gpd.GeoDataFrame(LISA_actors[['key', 'orig_zaaknaam', 'adres', 'activenq', 'AG', 'wkt']], geometry='wkt', crs={'init': 'epsg:28992'})
#
LMA_inbound4 = remaining_geo[['Key', 'Orig_name', 'Adres', 'WKT']]
LMA_inbound4.drop_duplicates(subset=['Key'], inplace=True)
LMA_inbound4['buffer'] = LMA_inbound4['WKT'].buffer(buffer_dist)
buffers = gpd.GeoDataFrame(LMA_inbound4[['Key', 'buffer']], geometry='buffer', crs={'init': 'epsg:28992'})
#
# LISA_actors_geo.to_file('LISA.shp')
# buffers.to_file('LMA.shp')

# LISA_actors_geo = gpd.read_file('LISA.shp')
# buffers = gpd.read_file('LMA.shp')

contains = gpd.sjoin(buffers, LISA_actors_geo, how='inner', op='intersects')

distances = pd.merge(contains, LISA_actors_geo[['wkt']], left_on='index_right', right_index=True)
distances = pd.merge(distances, LMA_inbound4[['Orig_name', 'Adres', 'WKT']], left_index=True, right_index=True)
distances['dist'] = distances.apply(lambda x: x['wkt'].distance(x['WKT']), axis=1)


# distances['freq'] = distances.groupby(['Key', 'AG'])['AG'].transform('count')
# distances['max_freq'] = distances.groupby(['Key'])['freq'].transform('max')
# matched_AG = distances[distances['freq'] == distances['max_freq']]
#
# # select those that match with only one most frequent activity group
# matched_1 = matched_AG[matched_AG.groupby('Key')['AG'].transform('nunique') == 1]
# print matched_1['Key'].nunique(), 'actors have been matched by the most frequent surrounding activity'
#
# # matching control output
# control_output_4 = matched_1[['Key', 'Orig_name', 'Adres', 'orig_zaaknaam', 'adres', 'activenq', 'AG']]
# control_output_4['match'] = 4
# control_output = control_output.append(control_output_4)
#
# # select those that match with multiple most frequent activity groups
# matched_2 = matched_AG[matched_AG.groupby('Key')['AG'].transform('nunique') > 1]
# # and then select geographically closest one from the list
# matched_2.reset_index(inplace=True)
# matched_2 = matched_2.loc[matched_2.groupby(['Key'])['dist'].idxmin()]
# print len(matched_2.index), 'actors have been matched by the closest actor (<{0}m)'.format(buffer_dist)

distances.reset_index(inplace=True)
matched_TEMP = distances.loc[distances.groupby(['Key'])['dist'].idxmin()]
print len(matched_TEMP.index), 'actors have been matched by the closest actor (<{0}m)'.format(buffer_dist)

# # matching control output
# control_output_5 = matched_2[['Key', 'Orig_name', 'Adres', 'orig_zaaknaam', 'adres', 'activenq', 'AG']]
# control_output_5['match'] = 5
# control_output = control_output.append(control_output_5)

# matched_by_proximity = pd.concat([matched_1, matched_2])
# matched_by_proximity = matched_by_proximity[['Key', 'AG']]
# matched_by_proximity.drop_duplicates(inplace=True)

matched_by_proximity = matched_TEMP[['Key', 'activenq']].drop_duplicates()

# OUTPUT BY PROXIMITY
output_by_proximity = matched_by_proximity.copy()
output_by_proximity['how'] = 'by proximity'

print len(output_by_proximity.index), 'actors have been matched by proximity',
print round(len(output_by_proximity.index) / float(total_inbound) * 100, 2), '%'

# take out those actors that had not been matched
remaining = remaining[(remaining['Key'].isin(output_by_proximity['Key']) == False)]

print remaining['Key'].nunique(), 'remaining unmatched'

control_output.to_excel('control_output.xlsx')

# ______________________________________________________________________________
# 5. UNMATCHED
#    not matched with anything, gets a dummy NACE code
#    points outside the LISA boundary also get a dummy code
# ______________________________________________________________________________

remaining['activenq'] = '0000'
out_boundary['activenq'] = '0000'

output_unmatched = pd.concat([remaining[['Key', 'activenq']], out_boundary[['Key', 'activenq']]])
output_unmatched.drop_duplicates(subset=['Key'], inplace=True)
output_unmatched['how'] = 'unmatched'

# ______________________________________________________________________________
# ______________________________________________________________________________

# G I V I N G   N A C E   T O  V E R W E R K E R
# ______________________________________________________________________________
# ______________________________________________________________________________

print 'Loading LMA verwerkers.......'
verwerkers = pd.read_excel(priv_folder + PART1 + 'Export_LMA_verwerker.xlsx')

verwerkers = verwerkers[['Key']].drop_duplicates()
print len(verwerkers), 'verwekers have been found'

verwerkers['activenq'] = verwerkers['Key'].apply(lambda x: '3820' + x.split()[-1])

output_verwerker = verwerkers[['Key', 'activenq']]
output_verwerker['how'] = 'verwerker'

# ______________________________________________________________________________
# ______________________________________________________________________________

#  C O N C A T E N A T E   O U T P U T S
# ______________________________________________________________________________
# ______________________________________________________________________________

all_nace = pd.concat([output_by_name_address, output_by_name, output_by_address,
                     output_by_proximity, output_unmatched, output_verwerker])

# ______________________________________________________________________________
# ______________________________________________________________________________

# G I V I N G   N A C E   T O   A L L   O T H E R   R O L E S
# ______________________________________________________________________________
# ______________________________________________________________________________

role_map = {'Afzender': '3810',
            'Inzamelaar': '3810',
            'Bemiddelaar': '3810',
            'Handelaar': '3810',
            'Ontvanger': '3810'}

for role in roles:

    print 'Loading LMA {0}s.......'.format(role)
    LMA_role = pd.read_excel(priv_folder + PART1 + 'Export_LMA_{0}.xlsx'.format(role))

    keys = LMA_role[['Key']].drop_duplicates()
    print len(keys), '{0}s have been found'.format(role)

    keys['activenq'] = role_map[role]

    output_role = keys.copy()
    output_role['how'] = role
    all_nace = all_nace.append(output_role)

print len(all_nace)
print all_nace['Key'].nunique()

# ______________________________________________________________________________
# ______________________________________________________________________________

# E X P O R T   A L L   A C T O R
# with their assigned NACE codes
# ______________________________________________________________________________
# ______________________________________________________________________________

all_nace.to_excel(priv_folder + EXPORT + 'All_actors.xlsx')
