# -*- coding: utf-8 -*-
"""
Built uppon
https://github.com/rusne/LMA-analysis/blob/master/lma_part2.py
Created on Wed Aug 22 09:17:31 2018

@author: geoFluxus Team

"""

import os
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
# Reading the LMA Actor list with their roles
# ______________________________________________________________________________

print 'Loading LMA actors.......'
LMA_actors = pd.read_excel(priv_folder + PART1 + 'Export_LMA_actors.xlsx'.format(scope))
#
# if any of the actors orginally did not have postcodes,
# read in the manually searched postcodes
# if 'Export_LMA_actors_without_postcode.xlsx' in os.listdir(priv_folder + PART1):
#     LMA_actors_w_postcode = pd.read_excel(priv_folder + INPUT + 'Input_actors_without_postcode.xlsx'.format(scope))
#
#     # check if actor file is older than the postcode file
#     # if not, give a warning as indexes might not match
#     t1 = os.path.getctime(priv_folder + PART1 + 'Export_LMA_actors.xlsx')
#     t2 = os.path.getctime(priv_folder + INPUT + 'Input_actors_without_postcode.xlsx')
#
#     if t1 > t2:
#         print 'WARNING! Your part1 exports are newer than other input files,'
#         print 'make sure they are all up to date'
#
#     LMA_actors.update(LMA_actors_w_postcode, overwrite=False)
#     no_postcode = LMA_actors[LMA_actors['Postcode'] == np.NaN]
#     if len(no_postcode.index) > 0:
#         print 'WARNING! Not all LMA actors have a postcode,',
#         print 'this will result in unexpected matching behaviour'


# create a unique key for LMA actors: Name + Postcode
# LMA_actors['LMA_key'] = LMA_actors['Name'] + ' ' + LMA_actors['Postcode']

# reading the LMA location list

print 'Loading LMA locations.......'
LMA_locations = pd.read_csv(priv_folder + INPUT + 'LMA_locations.csv')

# ______________________________________________________________________________
# reading all LISA actors
# ______________________________________________________________________________

print 'Loading LISA actors & locations.......'
LISA_actors = pd.read_excel(priv_folder + 'LISA_data/all_LISA_part2.xlsx',
                            nrows=100000)

# ______________________________________________________________________________
# reading Noord Holland area covered by LISA dataset
# ______________________________________________________________________________

print 'Loading LISA boundary.......'
LISA_boundary = gpd.read_file(pub_folder + 'LISA_boundary.shp')

# ______________________________________________________________________________
# ______________________________________________________________________________
# F U N C T I O N S
# ______________________________________________________________________________
# ______________________________________________________________________________


def give_bvdid(ind, scope, start_bvd):
    bvdid = 'LMA' + scope + str(ind + start_bvd).zfill(5)
    return bvdid


def chain_order(role):
    if role == 'ontdoener':
        return 0
    elif role == 'inzamelaar':
        return 1
    elif role == 'ontvanger':
        return 2
    elif role == 'verwerker':
        return 3
    else:
        print 'error: unknown role has been found  ', role


def give_nace(role):
    nace_by_role = {'ontdoener': 'WP-0004',
                    'inzamelaar': 'WT-0005',
                    'ontvanger': 'WT-0006',
                    'verwerker': 'WT-0007'}
    return nace_by_role[role]


# ______________________________________________________________________________
# ______________________________________________________________________________

# C O N N E C T I N G   A C T O R S
# ______________________________________________________________________________
# ______________________________________________________________________________

# first all actors that fall out of the LISA boundary need to be filtered out

LMA_locations['WKT'] = LMA_locations['WKT'].apply(wkt.loads)
LMAgdf = gpd.GeoDataFrame(LMA_locations, geometry='WKT', crs={'init': 'epsg:28992'})

joined = gpd.sjoin(LMAgdf, LISA_boundary, how='left')
in_boundary = joined[joined['Name'] == 'boundary']
out_boundary = joined[joined['Name'] != 'boundary']

print len(in_boundary.index), 'LMA actors are inside the LISA boundary'
print len(out_boundary.index), 'LMA actors are outside the LISA boundary'

# further matching only happens for the actors inside the boundary

in_boundary = in_boundary[['Key', 'WKT']]
LMA_inbound = pd.merge(LMA_actors, in_boundary, on='Key')

# number of actors that need to be matched
total_inbound = LMA_inbound['Key'].nunique()
print total_inbound

# ______________________________________________________________________________
# 1. BY NAME AND ADDRESS
#    year  and role is not important - if both name and address are the same
# ______________________________________________________________________________

LMA_inbound1 = LMA_inbound[['Key']].copy()
LMA_inbound1.drop_duplicates(inplace=True)

by_name_and_address = pd.merge(LMA_inbound1, LISA_actors, left_on='Key', right_on='key')

# OUTPUT BY NAME AND ADDRESS
output_by_name_address = by_name_and_address[['Key', 'activenq']].copy()

print len(output_by_name_address.index), 'actors have been matched by name & postcode',
print round(len(output_by_name_address.index) / float(total_inbound) * 100, 2), '%'

# take out those actors that had not been matched
remaining = LMA_inbound[(LMA_inbound['Key'].isin(output_by_name_address['Key']) == False)]

print remaining['Key'].nunique(), 'remaining'

# ______________________________________________________________________________
# 2. BY NAME ONLY
#    geographically closer one gets a priority
# ______________________________________________________________________________

LMA_inbound2 = remaining[['Name', 'Key', 'WKT']].copy()
LMA_inbound2.drop_duplicates(subset=['Key'], inplace=True)

by_name = pd.merge(LMA_inbound2, LISA_actors, left_on='Name', right_on='zaaknaam')

by_name['wkt'] = by_name['wkt'].apply(wkt.loads)
# by_name['WKT'] = by_name['WKT'].apply(wkt.loads)

by_name['dist'] = by_name.apply(lambda by_name: by_name['wkt'].distance(by_name['WKT']), axis=1)
closest = by_name.loc[by_name.groupby(['Key'])['dist'].idxmin()]

# OUTPUT BY NAME
output_by_name = closest[['Key', 'activenq']].copy()

print len(output_by_name.index), 'actors have been matched by name',
print round(len(output_by_name.index) / float(total_inbound) * 100, 2), '%'

# take out those actors that had not been matched
remaining = remaining[(remaining['Key'].isin(output_by_name['Key']) == False)]

print remaining['Key'].nunique(), 'remaining'

# ______________________________________________________________________________
# 3. BY ADDRESS ONLY
#    correct year gives priority in matching
# ______________________________________________________________________________

LMA_inbound3 = remaining[['Key', 'Adres', 'Jaar', 'Postcode']].copy()
LMA_inbound3.drop_duplicates(subset=['Key'], inplace=True)

by_address = pd.merge(LMA_inbound3, LISA_actors, left_on=['Adres', 'Postcode'], right_on=['adres', 'postcode'])

# find those that got matched to only one NACE code
by_address['count'] = by_address.groupby(['Key'])['activenq'].transform('count')
matched = by_address[by_address['count'] == 1]
matched = matched[['Key', 'activenq']]
matched.drop_duplicates(inplace=True)

print len(matched.index), 'actors have been matched only by address',

ambiguous = by_address[by_address['count'] > 1]

# give priority by year if possible, otherwise discard the matching
temp = pd.DataFrame(columns=ambiguous.columns)
for year in years:
    col = 'in{0}'.format(year)
    match = ambiguous[(ambiguous['Jaar'] == year) & (ambiguous[col] == 'JA')]
    temp.append(match)

ambiguous['count'] = ambiguous.groupby(['Key'])['activenq'].transform('count')
matched_ambiguous = ambiguous[ambiguous['count'] == 1]
matched_ambiguous = matched_ambiguous[['Key', 'activenq']]
matched_ambiguous.drop_duplicates(inplace=True)

print len(matched_ambiguous.index), 'additional actors have been matched by address and year'

discard = ambiguous[ambiguous['count'] > 1]
print discard['Key'].nunique(), 'matches have been discarded'

# OUTPUT BY ADDRESS
output_by_address = pd.concat([matched, matched_ambiguous])

print len(output_by_address.index), 'actors have been matched only by name',
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
LISA_actors_geo = gpd.GeoDataFrame(LISA_actors[['key', 'activenq', 'AG', 'wkt']], geometry='wkt', crs={'init': 'epsg:28992'})
#
LMA_inbound4 = remaining_geo[['Key', 'WKT']]
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
distances = pd.merge(distances, LMA_inbound4[['WKT']], left_index=True, right_index=True)
distances['dist'] = distances.apply(lambda x: x['wkt'].distance(x['WKT']), axis=1)


distances['freq'] = distances.groupby(['Key', 'AG'])['AG'].transform('count')
distances['max_freq'] = distances.groupby(['Key'])['freq'].transform('max')
matched_AG = distances[distances['freq'] == distances['max_freq']]

# select those that match with only one most frequent activity group
matched_1 = matched_AG[matched_AG.groupby('Key')['AG'].transform('nunique') == 1]
matched_1 = matched_1[['Key', 'AG']]
matched_1.drop_duplicates(inplace=True)
print len(matched_1.index), 'actors have been matched by the most frequent surrounding activity'

# select those that match with multiple most frequent activity groups
matched_2 = matched_AG[matched_AG.groupby('Key')['AG'].transform('nunique') > 1]
# and then select geographically closest one from the list
matched_2.reset_index(inplace=True)
matched_2 = matched_2.loc[matched_2.groupby(['Key'])['dist'].idxmin()]
print len(matched_2.index), 'actors have been matched by the closest actor (<{0}m)'.format(buffer_dist)

output_by_proximity = pd.concat([matched_1, matched_2[['Key', 'AG']]])

print len(output_by_proximity.index), 'actors have been matched by proximity',
print round(len(output_by_proximity.index) / float(total_inbound) * 100, 2), '%'

# take out those actors that had not been matched
remaining = remaining[(remaining['Key'].isin(output_by_proximity['Key']) == False)]

print remaining['Key'].nunique(), 'remaining'

remaining.to_excel('remaining.xlsx')

# ______________________________________________________________________________
# 5. UNMATCHED
#    not matched with anything, gets a dummy NACE code
# ______________________________________________________________________________



if False:
    lma_key_role_postcode = LMA_actors[['LMA_key', 'Name', 'who']]
    matched_by_name = pd.merge(lma_key_role_postcode, ORBIS_by_name,
                               left_on='Name', right_on='LMA Name', how='right')

    matched_by_name = matched_by_name[['LMA_key', 'who', 'name', 'Postcode',
                                       'BvDid', 'NACE', 'Year']]

    # BY ADDRESS
    LMA_actors['Huisnr'] = LMA_actors['Huisnr'].fillna(-999)
    LMA_actors['Huisnr'] = LMA_actors['Huisnr'].astype(int)  # avoid float-ization
    lma_key_role_address = LMA_actors[['LMA_key', 'Name', 'who', 'Postcode', 'Huisnr']]
    lma_key_role_address['address_key'] = lma_key_role_address['Postcode'] + ' ' + lma_key_role_address['Huisnr'].astype(str)

    ORBIS_all['postcode'] = ORBIS_all['postcode'].str.replace(' ','')
    ORBIS_all['postcode'] = ORBIS_all['postcode'].str.upper()
    # remove entries without an address as they cannot be matched anyway
    # this cleaning is not done earlier because the company with a vaild nace can still be matched by name
    ORBIS_all.dropna(subset=['postcode'], inplace=True)

    ORBIS_all['huisnummer'] = ORBIS_all['huisnummer'].fillna(-999)
    ORBIS_all['huisnummer'] = ORBIS_all['huisnummer'].astype(int)  # avoid float-ization
    ORBIS_all['address_key'] = ORBIS_all['postcode'] + ' ' + ORBIS_all['huisnummer'].astype(str)

    matched_by_address = pd.merge(lma_key_role_address, ORBIS_all, on='address_key', how='left')

    matched_by_address = matched_by_address[['LMA_key', 'name', 'who', 'postcode',
                                             'BvDid', 'nace', 'year']]

    # merging both methods into one for the decision tree
    matched_by_name.rename(columns={'name': 'ORBIS_name_by_name',
                                    'BvDid': 'BvDid_by_name',
                                    'Postcode': 'Postcode_by_name',
                                    'NACE': 'NACE_by_name',
                                    'Year': 'Year_by_name'}, inplace=True)

    matched_by_address.rename(columns={'name': 'ORBIS_name_by_address',
                                       'BvDid': 'BvDid_by_address',
                                       'postcode': 'Postcode_by_address',
                                       'nace': 'NACE_by_address',
                                       'year': 'Year_by_address'}, inplace=True)

    matched = pd.merge(matched_by_address, matched_by_name, on=['LMA_key', 'who'], how='left')

    matched.replace(np.NaN, '',inplace=True) #data cleaning

    # _________________________________________________________
    # 4) I M P L E M E N T I N G   A   D E C I S I O N   T R E E
    # _________________________________________________________

    total_count = len(LMA_actors)
    bvdindex = 0
    print total_count, "actors need to be matched"

    LMA_output_columns = ['LMA_key', 'Name',
                          'Postcode', 'City', 'Address',
                          'NACE', 'Role', 'BvDid',
                          'Matched name', 'Matched postcode', 'Matched NACE',
                          'Matched BvDid', 'Matched year', 'how']

    ORBIS_output_columns = ['BvDid', 'name', 'NACE', 'Code', 'Year', 'Description english',
                            'Description original', 'BvDii', 'Website', 'Employees',
                            'Turnover', 'Postcode', 'Address', 'City', 'Country', 'wkt']

    # _____________________________________________________________________
    # DECISION 1a: the same BvDid is found matching by name and by address
    # _____________________________________________________________________

    confirmed_or_unmatched = matched[matched['BvDid_by_address'] == matched['BvDid_by_name']]

    confirmed = confirmed_or_unmatched[confirmed_or_unmatched['BvDid_by_address'] != '']
    confirmed_count = len(confirmed.index)
    print '1a:', confirmed_count, 'actors have been confirmed'

    #output part 1a
    shortlist = confirmed[['BvDid_by_name', 'LMA_key', 'who']]
    shortlist.rename(columns={'BvDid_by_name': 'BvDid'}, inplace=True)

    ORBIS_actors_output = pd.merge(shortlist, ORBIS_by_name, on=['BvDid'], how='left')

    confirmed_output = ORBIS_actors_output[['LMA_key', 'name',
                                  'Postcode', 'City', 'Address',
                                  'NACE', 'who', 'BvDid',
                                  'name', 'Postcode', 'NACE', 'BvDid', 'Year']]
    confirmed_output['how'] = '1a'
    confirmed_output.columns = LMA_output_columns
    confirmed_output.drop_duplicates(inplace=True)

    # output file for the GDSE actor table
    ORBIS_actors_output = ORBIS_actors_output[ORBIS_output_columns]
    ORBIS_actors_output.drop_duplicates(inplace=True)
    ORBIS_actors_output.to_excel(ExportFolder + 'Export_ORBIS_actors.xlsx')

    # _____________________________________________________________________
    # DECISION 1b: actor has not been matched neither by name nor address
    # _____________________________________________________________________

    unmatched = confirmed_or_unmatched[confirmed_or_unmatched['BvDid_by_address'] == '']
    unmatched_count = len(unmatched.index)
    print '1b:', unmatched_count, 'actors have been unmatched'

    #output file 1b
    shortlist = unmatched[['LMA_key', 'who']]
    unmatched_output = pd.merge(shortlist, LMA_actors, on=['LMA_key', 'who'], how='left')

    unmatched_output.reset_index(drop=True, inplace=True)
    unmatched_output['BvDid'] = unmatched_output.index.map(int)
    unmatched_output['BvDid'] = unmatched_output['BvDid'].apply(give_bvdid, scope=scope, start_bvd=bvdindex)
    bvdindex += len(unmatched_output.index)

    unmatched_output['NACE'] = unmatched_output['who'].apply(give_nace)
    unmatched_output['Address'] = unmatched_output['Straat'] + ' ' + unmatched_output['Huisnr'].astype(str)
    unmatched_output = unmatched_output[['LMA_key', 'Name', 'Postcode', 'Plaats',
                                         'Address', 'NACE', 'who', 'BvDid']]
    unmatched_output['Matched name'] = ''
    unmatched_output['Matched postcode'] = ''
    unmatched_output['Matched NACE'] = ''
    unmatched_output['Matched BvDid'] = ''
    unmatched_output['Matched year'] = ''
    unmatched_output['how'] = '1b'
    unmatched_output.columns = LMA_output_columns


    # take out those actors that had been confirmed or unmatched
    matched_step2 = matched[(matched['LMA_key'].str.cat(matched['who']).isin(confirmed_or_unmatched['LMA_key'].str.cat(confirmed_or_unmatched['who'])) == False)]

    # __________________________________________________________________________________
    # DECISION 2a: actor has been matched to only one BvDid by address, nothing by name
    # __________________________________________________________________________________

    matched_step2['freq'] = matched_step2.groupby(['LMA_key', 'who'])['LMA_key'].transform('count')
    single_match = matched_step2[matched_step2['freq'] == 1]

    by_address = single_match[single_match['BvDid_by_name'] == '']
    by_address_count = len(by_address.index)
    print '2a:', by_address_count, "actors have been matched only by address"

    #output file 2a
    shortlist = by_address[['LMA_key', 'who', 'NACE_by_address',
                            'ORBIS_name_by_address', 'Postcode_by_address',
                            'BvDid_by_address', 'Year_by_address']]
    by_address_output = pd.merge(shortlist, LMA_actors, on=['LMA_key', 'who'], how='left')

    by_address_output.reset_index(drop=True, inplace=True)
    by_address_output['BvDid'] = by_address_output.index.map(int)
    by_address_output['BvDid'] = by_address_output['BvDid'].apply(give_bvdid, scope=scope, start_bvd=bvdindex)
    bvdindex += len(by_address_output.index)

    by_address_output['Address'] = by_address_output['Straat'] + ' ' + by_address_output['Huisnr'].astype(str)
    by_address_output = by_address_output[['LMA_key', 'Name', 'Postcode', 'Plaats',
                                           'Address', 'NACE_by_address', 'who', 'BvDid',
                                           'ORBIS_name_by_address', 'Postcode_by_address',
                                           'NACE_by_address', 'BvDid_by_address', 'Year_by_address']]
    by_address_output['how'] = '2a'
    by_address_output.columns = LMA_output_columns

    # __________________________________________________________________________________
    # DECISION 2b: actor has been matched to only one BvDid by name, nothing by address
    # __________________________________________________________________________________

    by_name = single_match[single_match['BvDid_by_address'] == '']
    by_name_count = len(by_name.index)
    print '2b:', by_name_count, "actors have been matched only by name"

    #output file 2b
    shortlist = by_name[['LMA_key', 'who', 'NACE_by_name',
                         'ORBIS_name_by_name', 'Postcode_by_name',
                         'BvDid_by_name', 'Year_by_name']]
    by_name_output = pd.merge(shortlist, LMA_actors, on=['LMA_key', 'who'], how='left')

    by_name_output.reset_index(drop=True, inplace=True)
    by_name_output['BvDid'] = by_name_output.index.map(int)
    by_name_output['BvDid'] = by_name_output['BvDid'].apply(give_bvdid, scope=scope, start_bvd=bvdindex)
    bvdindex += len(by_name_output.index)

    by_name_output['Address'] = by_name_output['Straat'] + ' ' + by_name_output['Huisnr'].astype(str)
    by_name_output = by_name_output[['LMA_key', 'Name', 'Postcode', 'Plaats',
                                     'Address', 'NACE_by_name', 'who', 'BvDid',
                                     'ORBIS_name_by_name', 'Postcode_by_name',
                                     'NACE_by_name', 'BvDid_by_name', 'Year_by_name']]
    by_name_output['how'] = '2b'

    by_name_output.columns = LMA_output_columns

    # ____________________________________________________________________________________
    # DECISION 2c: actor has been matched by both name and address but to different actors
    # ____________________________________________________________________________________

    by_name_and_address = single_match[(single_match['BvDid_by_name'] != '') & (single_match['BvDid_by_address'] != '')]
    by_name_and_address_count = len(by_name_and_address.index)
    print '2c:', by_name_and_address_count, "actors have been matched by name and address to different entities"

    by_na_same_nace = by_name_and_address[by_name_and_address['NACE_by_name'] == by_name_and_address['NACE_by_address']]
    by_na_same_nace_count = len(by_na_same_nace.index)
    print '\t', by_na_same_nace_count, "of them still have the same NACE code"

    by_na_diff_nace = by_name_and_address[by_name_and_address['NACE_by_name'] != by_name_and_address['NACE_by_address']]

    by_name_and_address_a = by_na_diff_nace[by_na_diff_nace['Year_by_address'] > by_na_diff_nace['Year_by_name']]
    by_name_and_address_n = by_na_diff_nace[by_na_diff_nace['Year_by_address'] <= by_na_diff_nace['Year_by_name']]

    # output file 2c
    shortlist_na = by_na_same_nace[['LMA_key', 'who', 'NACE_by_name',
                                    'ORBIS_name_by_name', 'Postcode_by_name',
                                    'BvDid_by_name', 'Year_by_name']]
    shortlist_a = by_name_and_address_a[['LMA_key', 'who', 'NACE_by_address',
                                         'ORBIS_name_by_address', 'Postcode_by_address',
                                         'BvDid_by_address', 'Year_by_address']]
    shortlist_n = by_name_and_address_n[['LMA_key', 'who', 'NACE_by_name',
                                         'ORBIS_name_by_name', 'Postcode_by_name',
                                         'BvDid_by_name', 'Year_by_name']]
    col = ['LMA_key', 'who', 'NACE', 'matched name', 'matched postcode', 'matched bvdid', 'matched_year']
    shortlist_na.columns = col
    shortlist_a.columns = col
    shortlist_n.columns = col
    shortlist = pd.concat([shortlist_na, shortlist_a, shortlist_n])


    by_name_and_address_output = pd.merge(shortlist, LMA_actors, on=['LMA_key', 'who'], how='left')

    by_name_and_address_output.reset_index(drop=True, inplace=True)
    by_name_and_address_output['BvDid'] = by_name_and_address_output.index.map(int)
    by_name_and_address_output['BvDid'] = by_name_and_address_output['BvDid'].apply(give_bvdid, scope=scope, start_bvd=bvdindex)
    bvdindex += len(by_name_and_address_output.index)

    by_name_and_address_output['Address'] = by_name_and_address_output['Straat'] + ' ' + by_name_and_address_output['Huisnr'].astype(str)
    by_name_and_address_output = by_name_and_address_output[['LMA_key', 'Name', 'Postcode', 'Plaats',
                                                             'Address', 'NACE', 'who', 'BvDid',
                                                             'matched name', 'matched postcode',
                                                             'NACE', 'matched bvdid', 'matched_year']]
    by_name_and_address_output['how'] = '2c'
    by_name_and_address_output.columns = LMA_output_columns

    # take out those actors that had been matched
    matched_step3 = matched_step2[(matched_step2['freq'] != 1)]

    # _________________________________________________________________________
    # DECISION 3: actor has been matched to multiple others by name and address
    # _________________________________________________________________________

    # actors are different by name and address but NACE code is the same


    # all possibilities are equal, therefore the dataframe needs to be reorganised vertically
    step3_a = matched_step3[['LMA_key', 'who', 'ORBIS_name_by_address', 'Postcode_by_address',
                             'BvDid_by_address', 'NACE_by_address', 'Year_by_address']]
    step3_a['how'] = 'by address'
    step3_n = matched_step3[['LMA_key', 'who', 'ORBIS_name_by_name', 'Postcode_by_name',
                             'BvDid_by_name', 'NACE_by_name', 'Year_by_name']]
    step3_n['how'] = 'by name'
    step3_n = step3_n[step3_n['BvDid_by_name'] != '']
    col = ['LMA_key', 'who', 'ORBIS_name', 'ORBIS_Postcode', 'ORBIS_BvDid', 'NACE', 'Year', 'how']
    step3_a.columns = col
    step3_n.columns = col

    step3 = pd.concat([step3_a, step3_n])
    step3.drop_duplicates(inplace=True)
    step3['Year'].replace('', '0', inplace=True)
    step3['Year'] = step3['Year'].astype(int)
    step3.reset_index(drop=True, inplace=True)

    step3.to_excel(ExportFolder + 'actors_matched_ambiguously.xlsx')

    # _________________________________________________________________________
    # DECISION 3a: actor has been matched to multiple others but they all have the same NACE
    # _________________________________________________________________________

    step3['NACE_options'] = step3.groupby(['LMA_key', 'who'])['NACE'].transform('nunique')
    same_NACE = step3[step3['NACE_options'] == 1]
    same_NACE.drop_duplicates(subset=['LMA_key', 'who', 'NACE'], inplace=True)

    same_NACE_count = len(same_NACE.index)
    print '3a:', same_NACE_count, 'actors have been matched to multiple entities but all of the same NACE code'

    # output file 3a
    shortlist = same_NACE[['LMA_key', 'who', 'NACE', 'ORBIS_name', 'ORBIS_Postcode', 'ORBIS_BvDid', 'Year']]
    by_nace_output = pd.merge(shortlist, LMA_actors, on=['LMA_key', 'who'], how='left')

    by_nace_output.reset_index(drop=True, inplace=True)
    by_nace_output['BvDid'] = by_nace_output.index.map(int)
    by_nace_output['BvDid'] = by_nace_output['BvDid'].apply(give_bvdid, scope=scope, start_bvd=bvdindex)
    bvdindex += len(by_nace_output.index)

    by_nace_output['Address'] = by_nace_output['Straat'] + ' ' + by_nace_output['Huisnr'].astype(str)
    by_nace_output = by_nace_output[['LMA_key', 'Name', 'Postcode', 'Plaats',
                                     'Address', 'NACE', 'who', 'BvDid',
                                     'ORBIS_name', 'ORBIS_Postcode', 'NACE', 'ORBIS_BvDid', 'Year']]
    by_nace_output['how'] = '3a'
    by_nace_output.columns = LMA_output_columns

    # _________________________________________________________________________
    # DECISION 3b: actor has been matched to multiple others but they all have different NACE
    # _________________________________________________________________________

    step3 = step3[step3['NACE_options'] != 1]

    ambiguous_match = step3.loc[step3.groupby(['LMA_key', 'who'])['Year'].idxmax()]
    ambiguous_match_count = len(ambiguous_match.index)
    print '3b:', ambiguous_match_count, "have been matched ambiguously"

    # output file 3b
    shortlist = ambiguous_match[['LMA_key', 'who', 'NACE', 'ORBIS_name', 'ORBIS_Postcode', 'ORBIS_BvDid', 'Year']]
    ambiguous_output = pd.merge(shortlist, LMA_actors, on=['LMA_key', 'who'], how='left')

    ambiguous_output.reset_index(drop=True, inplace=True)
    ambiguous_output['BvDid'] = ambiguous_output.index.map(int)
    ambiguous_output['BvDid'] = ambiguous_output['BvDid'].apply(give_bvdid, scope=scope, start_bvd=bvdindex)
    bvdindex += len(ambiguous_output.index)

    ambiguous_output['Address'] = ambiguous_output['Straat'] + ' ' + ambiguous_output['Huisnr'].astype(str)
    ambiguous_output = ambiguous_output[['LMA_key', 'Name', 'Postcode', 'Plaats',
                                         'Address', 'NACE', 'who', 'BvDid',
                                         'ORBIS_name', 'ORBIS_Postcode', 'NACE', 'ORBIS_BvDid', 'Year']]
    ambiguous_output['how'] = '3b'
    ambiguous_output.columns = LMA_output_columns

    # _________________________________________________________________________
    # N A C E    C O N S T R A I N T S
    # _________________________________________________________________________


    unconfirmed_output = pd.concat([unmatched_output, by_address_output, by_name_output, by_name_and_address_output, by_nace_output, ambiguous_output])
    print 'unconfirmed_output:', len(unconfirmed_output.index)

    # CONSTRAINT 1:
        # ontdoener can have any NACE,
        # inzamelaar can belong to groups E, H, otherwise UNKNOWN
        # ontvanger can belong to groups E, H, otherwise UNKNOWN
        # verwerker can belong to groups E, H, otherwise UNKNOWN
        # exception: an actor has been matched by both name and address

    actors_constraint1 = unconfirmed_output[unconfirmed_output['Role'] != 'ontdoener']
    actors_constraint1 = actors_constraint1[actors_constraint1['NACE'].str.startswith('E') == False]
    actors_constraint1 = actors_constraint1[actors_constraint1['NACE'].str.startswith('H') == False]

    # exclude constrained subset from all the uncofirmed actors
    actors_no_constraint1 = pd.concat([actors_constraint1, unconfirmed_output]).drop_duplicates(keep=False)

    actors_constraint1['NACE'] = actors_constraint1['Role'].apply(give_nace)

    unconfirmed_output = pd.concat([actors_no_constraint1, actors_constraint1])
    all_actors = pd.concat([confirmed_output, unconfirmed_output])
    print 'all_actors:', len(all_actors.index)

    # export the final list of actors

    all_actors.to_excel(ExportFolder + 'Export_all_actor_matches.xlsx')

    # _____________________________________________________________________________
    # _____________________________________________________________________________
    # N E W    A C T O R   T A B L E
    # _____________________________________________________________________________
    # _____________________________________________________________________________

    new_actors = unconfirmed_output.copy()
    # the unknown fields are filled with empty cells
    new_actors['code'] = ''
    new_actors['year'] = 2016
    new_actors['description english'] = ''
    new_actors['description original'] = new_actors['Role']
    new_actors['BvDii'] = ''
    new_actors['Website'] = ''
    new_actors['employees'] = ''
    new_actors['turnover'] = ''
    new_actors = new_actors[['BvDid', 'Name', 'code', 'year', 'description english', 'description original',
                             'BvDii', 'Website', 'employees', 'turnover', 'NACE']]

    new_actors.to_excel(ExportFolder + 'Export_LMA_actors.xlsx')


    # _____________________________________________________________________________
    # _____________________________________________________________________________
    #  A C T O R    L O C A T I O N S    T A B L E
    # _____________________________________________________________________________
    # _____________________________________________________________________________

    locations = all_actors.copy()
    locations = locations[['BvDid', 'Postcode', 'Address', 'City']]
    locations.drop_duplicates(subset=['BvDid'], inplace=True)

    locations.to_excel(ExportFolder +'Export_LMA_actors_locations.xlsx', index=False)


    # _____________________________________________________________________________
    # _____________________________________________________________________________
    #  A C T I V I T Y  &  A C T I V I T Y   G R O U P   T A B L E S
    # _____________________________________________________________________________
    # _____________________________________________________________________________

    activities = all_actors[['NACE']]
    activities.drop_duplicates(inplace=True)

    nace_table = pd.read_excel('NACE_table.xlsx'.format(projectname))
    nace_table.rename(columns={'Code':'NACE'}, inplace=True)
    nace_table_merged = pd.merge(activities, nace_table, how='left', on='NACE')

    activity_table = nace_table_merged[['NACE', 'Name', 'AG code']]
    activity_table.columns = ['NACE', 'Name', 'AG']
    activity_table.to_excel(ExportFolder + 'Export_LMA_activities.xlsx')

    activity_group_table = nace_table_merged[['AG code', 'Activity Group']]
    activity_group_table.drop_duplicates(inplace=True)
    activity_group_table.columns = ['Code', 'Name']
    activity_group_table.to_excel(ExportFolder + 'Export_LMA_activity_groups.xlsx')

    # _____________________________________________________________________________
    # _____________________________________________________________________________
    #  U N K N O W N   N A C E   C O D E S
    # _____________________________________________________________________________
    # _____________________________________________________________________________

    unknown_nace_table = all_actors[all_actors['NACE'].str[0] == 'W']
    unknown_nace_table = unknown_nace_table[['BvDid', 'LMA_key', 'Name', 'Postcode',
                                             'Address', 'City', 'Role', 'NACE']]
    print 'unknown nace:', len(unknown_nace_table.index)
    unknown_nace_table.to_excel(ExportFolder + 'Unknown_NACE.xlsx')
