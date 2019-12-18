# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 2019

@author: geoFluxus Team

"""

import pandas as pd

# reads separate LISA and KvK files (located & unlocated)
# combines them into a single one
# and merges with the NACE activity groups

import warnings  # ignore unnecessary warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
pd.options.mode.chained_assignment = None

priv_folder = "Private_data/"
pub_folder = "Public_data/"

print('Loading LISA dataset....')
all_LISA = pd.read_excel(priv_folder + 'LISA_data/all_LISA_part1.xlsx')
# LISA_unlocated = pd.read_csv(priv_folder + 'LISA_data/LISA_kml_RDnew.csv', sep=',')
# LISA_located = pd.read_csv(priv_folder + 'LISA_data/LISA_located.csv')
LISA_loc = pd.read_csv(priv_folder + 'LISA_data/LISA_RDnew_MRA.csv', sep=',')

print('LISA dataset has been loaded')

# LISA_unlocated = LISA_unlocated[['WKT', 'key']]
# LISA_unlocated.rename(columns={'WKT': 'wkt'}, inplace=True)
#
# LISA_located = LISA_located[['wkt', 'key']]
#
# LISA_loc = pd.concat([LISA_unlocated, LISA_located])
# LISA_loc.drop_duplicates(subset=['key'], inplace=True)

LISA = pd.merge(all_LISA, LISA_loc, on='key')
print(len(LISA.index), len(all_LISA.index))

print('Loading KvK dataset....')
all_KvK = pd.read_excel(priv_folder + 'KvK_data/all_KvK_part1.xlsx')
KvK_loc = pd.read_csv(priv_folder + 'KvK_data/KvK_RDnew_MRA.csv', sep=',')

# KvK dataset needs to be connected back with the addresses
KvK_key_add = all_KvK[['key', 'adres', 'postcode', 'plaats']].drop_duplicates()
KvK_loc = pd.merge(KvK_loc, KvK_key_add, on='key')
KvK_loc.drop(columns=['key'], inplace=True)

KvK = pd.merge(all_KvK, KvK_loc, on=['adres', 'postcode', 'plaats'])
print(len(KvK.index), len(all_KvK.index))

#
NACE_table = pd.read_excel(pub_folder + 'NACE_table.xlsx', sheet_name='NACE_nl')
# activity_groups['Digits'] = activity_groups['Digits'].astype(str)
# activity_groups['Digits'] = activity_groups['Digits'].str.zfill(2)


# merge LISA with KvK and remove duplicates
all = pd.concat([LISA, KvK])
both = len(all.index)
all.drop_duplicates(subset=['key'], inplace=True)
print(both - len(all.index), 'overlaps have been found between KvK and LISA')

# merge with the activity groups
all['activenq'] = all['activenq'].astype(str)
all['activenq'] = all['activenq'].str.zfill(4)
NACE_table['Digits'] = NACE_table['Digits'].astype(str)
NACE_table['Digits'] = NACE_table['Digits'].str.zfill(4)
# all['digits'] = all['digits'].str.slice(stop=2)
all_ag = pd.merge(all, NACE_table[['Digits', 'AGcode']], how='left', left_on='activenq', right_on='Digits')

# check if all codes were present
errors = all_ag[all_ag['AGcode'].isna()]
if len(errors.index) > 0:
    print('WARNING! Errors in NACE codes have been found:')
    print(errors['activenq'].drop_duplicates())

all_ag.drop(columns=['Digits'])
# skip the ones that did not match with any NACE code (all should be coming from LISA)
all_ag = all_ag[all_ag['AGcode'].isna() == False]

all_ag.to_excel(priv_folder + 'all_LISA_KvK_part2.xlsx')
