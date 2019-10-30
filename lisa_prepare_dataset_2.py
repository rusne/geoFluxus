# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 2019

@author: geoFluxus Team

"""

import pandas as pd
import numpy as np

# reads separate LISA files (located & unlocated)
# combines them into a single one
# and merges with the NACE activity groups

priv_folder = "Private_data/"
pub_folder = "Public_data/"

print 'Loading LISA dataset....'


all_LISA = pd.read_excel(priv_folder + 'LISA_data/all_LISA_part1.xlsx')
LISA_unlocated = pd.read_csv(priv_folder + 'LISA_data/LISA_kml_RDnew.csv', sep=',')
LISA_located = pd.read_csv(priv_folder + 'LISA_data/LISA_located.csv')

print 'LISA dataset has been loaded'

activity_groups = pd.read_excel(pub_folder + 'NACE_activity_groups.xlsx')
activity_groups['digits'] = activity_groups['digits'].astype(str)
activity_groups['digits'] = activity_groups['digits'].str.zfill(2)

LISA_unlocated = LISA_unlocated[['WKT', 'key']]
LISA_unlocated.rename(columns={'WKT': 'wkt'}, inplace=True)

LISA_located = LISA_located[['wkt', 'key']]

LISA_loc = pd.concat([LISA_unlocated, LISA_located])
# LISA_loc.drop_duplicates(subset=['key'], inplace=True)

LISA = pd.merge(all_LISA, LISA_loc, how='left', on='key')
print len(LISA.index), len(LISA_loc.index)

# merge with the activity groups
LISA['digits'] = LISA['activenq'].astype(str)
LISA['digits'] = LISA['digits'].str.zfill(4)
LISA['digits'] = LISA['digits'].str.slice(stop=2)
LISA_ag = pd.merge(LISA, activity_groups, how='left', on='digits')

# check if all codes were present
errors = LISA[LISA_ag['AG'].isna()]
if len(errors.index) > 0:
    print 'WARNING! Errors in NACE codes have been found:'
    print errors[['activenq', 'digits']]

LISA_ag.drop(columns=['digits'])


if len(all_LISA.index) == len(LISA_ag.index):
    print 'Geolocating successful.\nWriting combined file.....'
    LISA_ag.to_excel(priv_folder + 'LISA_data/all_LISA_part2.xlsx')
    print 'Combined file has been written'
elif len(all_LISA.index) > len(LISA_ag.index):
    print 'WARNING! Not all actors could be located.'
    print 'Writing combined file.....'
    LISA_ag.to_excel(priv_folder + 'LISA_data/all_LISA_part2.xlsx')
    print 'Combined file has been written'
else:
    print 'ERROR! There are some duplicate entries, fix input files'
    print 'No combined file could be written'
