# -*- coding: utf-8 -*-
"""
Created on Sun Nov 3 2019

@author: geoFluxus Team

"""

import pandas as pd
import numpy as np
from clean import clean_description

# reads the classification of waste materials,
# unifies the descriptions and splits into keyflows

import warnings  # ignore unnecessary warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
pd.options.mode.chained_assignment = None

priv_folder = "Private_data/"
pub_folder = "Public_data/"


print "Loading full categorization......."
all_categ = pd.read_excel(priv_folder + 'Hfsdt_02_03_04_17_20_categories.xlsx', sheet_name='Data')


all_categ['Euralcode'] = all_categ['Euralcode'].astype(str)
all_categ['Euralcode'] = all_categ['Euralcode'].str.zfill(6)

# clean all text fields
for col in all_categ.columns:
    all_categ[col] = all_categ[col].astype('unicode')
    all_categ[col] = all_categ[col].apply(clean_description)

# control if all codes are used
total_codes = 0
codes = []

cat_orig_columns = ['reden', 'oorsprong', 'kleur', 'staat', 'afmeting',
                    'consistentie', 'Andere code', 'materiaal 4', 'materiaal 3',
                    'materiaal 2', 'materiaal', 'm-type', 'composiet 2',
                    'composiet 1', 'c-type', 'product', 'direct',
                    'p-type', 'gemengd/puur',
                    'schoon/vervuild', 'Euralcode', 'Beschrijving']

cat_cols = ['reason', 'origin', 'colour', 'state', 'size',
            'consistency', 'other', 'mat 4', 'mat 3',
            'mat 2', 'material', 'm-type', 'composite 2',
            'composite', 'c-type', 'product', 'direct_use', 'p-type', 'mixed',
            'clean', 'EuralCode', 'BenamingAfval']

for scope in ('CDW', 'FW', 'CG'):
    print "filtering ", scope, 'keyflow.......'

    INPUT = "Input_{0}_part1/".format(scope)
    EXPORT = "Input_{0}_part3/".format(scope)
    eural = pd.read_excel(pub_folder + INPUT + 'EURAL_codes_{0}.xlsx'.format(scope), dtype=object)

    eural['EuralCode'] = eural['EuralCode'].astype(str)
    eural['EuralCode'] = eural['EuralCode'].str.zfill(6)

    cat_scope = pd.merge(all_categ, eural, left_on='Euralcode', right_on='EuralCode')

    cat_scope.drop_duplicates(inplace=True)
    # check if cleaned descriptions do not refer to different categories
    grouped = cat_scope.groupby(['Beschrijving', 'Euralcode'])
    if len(cat_scope.index) != grouped.ngroups:
        print 'WARNING! There are descriptions that refer to different categorization'
        e = cat_scope[grouped['Beschrijving'].transform('count') > 1].copy()
        e.drop(columns=['EuralNaam', 'EuralCode'], inplace=True)
        for col in e.columns:
            if e[col].nunique() <= 1:
                e.drop(columns=col, inplace=True)
            else:
                continue
        print e

# ______________________________________________________________________________
#       Restructure column values
# ______________________________________________________________________________

    cat_scope.loc[cat_scope['indirect product'].isna(), 'product'] = cat_scope['direct product']
    cat_scope.loc[cat_scope['direct product'].isna(), 'product'] = cat_scope['indirect product']
    cat_scope.loc[cat_scope['indirect product'].notna(), 'direct'] = False
    cat_scope.loc[cat_scope['direct product'].notna(), 'direct'] = True

    cat_scope.loc[cat_scope['gemengd/puur'] == 'gemengd', 'gemengd/puur'] = True
    cat_scope.loc[cat_scope['gemengd/puur'] == 'puur', 'gemengd/puur'] = False

    cat_scope.loc[cat_scope['schoon/vervuild'] == 'schoon', 'schoon/vervuild'] = True
    cat_scope.loc[cat_scope['schoon/vervuild'] == 'vervuild', 'schoon/vervuild'] = False

# ______________________________________________________________________________
#       Output categorisation per keyflow
# ______________________________________________________________________________

    cat_scope = cat_scope[cat_orig_columns]
    cat_scope.columns = cat_cols
    cat_scope.to_excel(pub_folder + EXPORT + 'Categorization.xlsx')

# ______________________________________________________________________________
#       Control consistency between the different files
# ______________________________________________________________________________

    if eural['EuralCode'].nunique() != cat_scope['EuralCode'].nunique():
        print 'WARNING! Not all EWC codes were present in the categorization:'
        cat = cat_scope[['EuralCode']].copy()
        cat.drop_duplicates(inplace=True)
        div = eural[['EuralCode']].copy()
        div.drop_duplicates(inplace=True)
        diff = div[(div['EuralCode'].isin(cat['EuralCode']) == False)]
        print diff

    n_codes = cat_scope['EuralCode'].nunique()
    total_codes += n_codes
    print n_codes, 'EWC codes have been filtered'
    codes.append(cat_scope[['EuralCode']].copy())

if total_codes < all_categ['Euralcode'].nunique():
    print 'WARNING! Not all categorization codes were present in keyflow division'
    print all_categ['Euralcode'].nunique() - total_codes
    categ = all_categ[['Euralcode']].copy()
    categ.drop_duplicates(inplace=True)
    division = pd.concat(codes)
    division.drop_duplicates(inplace=True)
    diff = categ[(categ['Euralcode'].isin(division['EuralCode']) == False)]
    print diff
