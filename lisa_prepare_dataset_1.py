# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 2019

@author: geoFluxus Team

"""

import pandas as pd
import time
from clean import clean_company_name
from clean import clean_address
from clean import clean_postcode
from clean import clean_nace
import variables as var

# TODO!!! update description
# Reads all the original LISA files year by year, filters the relevant columns,
# unifies NACE codes to 4 or 5 digits,
# filters out companies without a NACE code,
# prepares unlocated entries for the geoloaction

priv_folder = "Private_data/"
pub_folder = "Public_data/"

NACEtable = pd.read_excel(pub_folder + 'NACE_table.xlsx', sheet_name='NACE_nl')

all_years = []
active_in = dict()
for year in var.map_years:
    if year not in var.LISA_years:
        continue
    orig_LISA_dataset = priv_folder + "LISA_data/raw_data/mra{0}_wl.csv".format(year)

    # selection of the columns we want to include in our analysis
    LISA_columns = ['zaaknaam', 'straat', 'huisnr', 'postcode', 'plaats',
                    'activenq', 'xcoord', 'ycoord']

    print("\nLoading LISA dataset for {0}........".format(year))
    start_time = time.time()

    # Reading in the LISA data
    LISA = pd.read_csv(orig_LISA_dataset, dtype=object, sep=';', encoding="utf-8")
    LISA = LISA[LISA_columns]

    # for testing
    # LISA = LISA.head(100)

    print('LISA dataset for {0} has been loaded, '.format(year),)
    print('dataset length:', len(LISA.index), 'lines,',)
    m, s = divmod(time.time() - start_time, 60)
    print('time elapsed:', m, 'min', s, 's')

    # encoding as unicode (in case there are non-ascii characters)
    # LISA['zaaknaam'] = LISA['zaaknaam'].apply(lambda x: unicode(x))
    # LISA['straat'] = LISA['straat'].apply(lambda x: unicode(x))
    # LISA['plaats'] = LISA['plaats'].apply(lambda x: unicode(x))
    LISA['zaaknaam'] = LISA['zaaknaam'].astype(str)
    LISA['straat'] = LISA['straat'].astype(str)
    LISA['plaats'] = LISA['plaats'].astype(str)
    LISA['postcode'] = LISA['postcode'].astype(str)

    # filter incorrect NACE codes
    pre = len(LISA.index)
    # LISA['activenq'] = pd.to_numeric(LISA['activenq'], downcast='integer', errors="coerce")
    LISA['activenq'] = LISA['activenq'].astype(str)
    LISA['activenq'] = LISA['activenq'].apply(clean_nace)
    # LISA = LISA[LISA.activenq.notnull()]
    # LISA['activenq'] = LISA['activenq'].astype(int)

    LISA['activenq'] = LISA['activenq'].astype(str)
    LISA = LISA[LISA['activenq'].str.len() < 6]
    LISA = LISA[LISA['activenq'].str.len() > 3]

    LISA = LISA[LISA['activenq'].astype(int) > 100]
    LISA['activenq'] = LISA['activenq'].apply(lambda x: str(x)[:4])
    # unify NACE codes
    # LISA['activenq'] = LISA['activenq'].astype(str)
    # LISA['activenq'] = LISA['activenq'].str.zfill(4)

    # match with the list of NACE activities, skip if not present
    NACEtable['Digits'] = NACEtable['Digits'].astype(str)
    NACEtable['Digits'] = NACEtable['Digits'].str.zfill(4)
    LISA = pd.merge(LISA, NACEtable[['Digits']], left_on='activenq', right_on='Digits', validate='m:1', how='left')

    e = LISA[LISA['Digits'].isna()]
    print(e['activenq'].drop_duplicates())

    print(pre - len(LISA.index), 'lines have been filtered due to an invalid NACE')

    # filter invalid company names
    LISA['orig_zaaknaam'] = LISA['zaaknaam']  # copy of the orig name
    pre = len(LISA.index)
    LISA['zaaknaam'] = LISA['zaaknaam'].apply(clean_company_name)
    LISA = LISA[LISA['zaaknaam'].str.len() > 1]

    print(pre - len(LISA.index), 'lines have been filtered due to an invalid name')

    # clean addresses
    LISA['postcode'] = LISA['postcode'].apply(clean_postcode)
    LISA['straat'] = LISA['straat'].apply(clean_address)
    LISA['plaats'] = LISA['plaats'].apply(clean_address)

    # filter invalid postcodes
    pre = len(LISA.index)
    LISA = LISA[LISA['postcode'].str.len() == 6]

    print(pre - len(LISA.index), 'lines have been filtered due to an invalid postcode')

    # clean coordinates
    LISA['xcoord'] = pd.to_numeric(LISA['xcoord'], downcast='integer', errors="coerce")
    LISA['ycoord'] = pd.to_numeric(LISA['ycoord'], downcast='integer', errors="coerce")
    LISA = LISA[LISA.xcoord.notnull()]
    LISA['xcoord'].fillna(0, inplace=True)
    LISA['ycoord'].fillna(0, inplace=True)
    LISA['xcoord'] = LISA['xcoord'].astype(str)
    LISA['ycoord'] = LISA['ycoord'].astype(str)



    pre = len(LISA.index)
    # remove duplicate values that might have appeared due to cleaning and filtering
    LISA.drop_duplicates(subset=['zaaknaam', 'postcode', 'activenq'], inplace=True)

    print(pre - len(LISA.index), 'duplicates have been found and removed')

    # join address into a single column for easier geolocation
    LISA['adres'] = LISA['straat'] + ' ' + LISA['huisnr']

    # create a key for each separate actor (name + postcode)
    LISA['key'] = LISA['zaaknaam'].str.cat(LISA[['postcode']], sep=' ')

    # create a df to mark that the company has been active in that year
    year_col = 'in{0}'.format(year)
    LISA_copy = LISA[['key']].copy()
    LISA_copy.drop_duplicates(inplace=True)
    LISA_copy[year_col] = 'JA'
    active_in[year_col] = LISA_copy

    all_years.append(LISA.copy())

# ______________________________________________________________________________
#   Concatenating all the years into a single dataset
# ______________________________________________________________________________

# ASSUMPTION:
all_LISA = pd.concat(all_years)
all_LISA.drop_duplicates(subset=['key', 'activenq'], inplace=True)

print('\nAfter removing duplicates',)
print(len(all_LISA.index), 'actors remain in total')

pre = len(all_LISA.index)
# find out how many companies with the same postcode have different NACE
all_LISA['count'] = all_LISA.groupby(['zaaknaam', 'postcode'])['activenq'].transform('count')
duplicates = all_LISA[all_LISA['count'] > 1]
duplicates.to_excel(priv_folder + 'LISA_data/auxiliary/duplicates.xlsx')

# for companies that have more than one NACE code, choose randomly which one to use
all_LISA.drop_duplicates(subset=['zaaknaam', 'postcode'], inplace=True)

print(pre - len(all_LISA.index), 'companies have been assigned to more than one NACE code')
print(len(all_LISA.index), 'unique company name and postcode combinations remain')


for year in var.all_years:
    year_col = 'in{0}'.format(year)
    if year_col not in active_in.keys():
        all_LISA[year_col] = None
        continue
    all_LISA = pd.merge(all_LISA, active_in[year_col], how='left', on='key')

all_LISA_col = ['zaaknaam', 'orig_zaaknaam', 'postcode', 'adres', 'plaats',
                'activenq', 'key']
year_activity = ['in{0}'.format(year) for year in var.all_years]

all_LISA[all_LISA_col + year_activity].to_excel(priv_folder + 'LISA_data/all_LISA_part1.xlsx')

# ______________________________________________________________________________
#   Splitting dataset in separate files: located and not located ones
# ______________________________________________________________________________

all_LISA.drop_duplicates(subset=['key'], inplace=True)
located = all_LISA[all_LISA['xcoord'] != '0'].copy()  # assuming that ycoord is also not 0
unlocated = all_LISA[all_LISA['xcoord'] == '0'].copy()  # assuming that ycoord is also 0

located['wkt'] = 'POINT(' + located['xcoord'] + ' ' + located['ycoord'] + ')'
located = located[['key', 'wkt']]
located.drop_duplicates(inplace=True)
located.to_csv(priv_folder + 'LISA_data/LISA_located.csv'.format(year), encoding='utf8')
print(len(located.index), 'companies are already located')

unlocated = unlocated[['key', 'adres', 'postcode', 'plaats']]
unlocated.drop_duplicates(inplace=True)
unlocated.to_csv(priv_folder + 'LISA_data/LISA_unlocated.csv'.format(year), index=False, encoding='utf8')
print(len(unlocated.index), 'companies still need to be located')
