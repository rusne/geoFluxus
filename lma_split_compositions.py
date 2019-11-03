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

for scope in ('CDW', 'FW', 'CG'):
    print "filtering ", scope, 'keyflow.......'

    INPUT = "Input_{0}_part1/".format(scope)
    eural = pd.read_excel(pub_folder + INPUT + 'EURAL_codes_{0}.xlsx'.format(scope), dtype=object)

    eural['EuralCode'] = eural['EuralCode'].astype(str)
    eural['EuralCode'] = eural['EuralCode'].str.zfill(6)

    cat_scope = pd.merge(all_categ, eural, left_on='Euralcode', right_on='EuralCode')

    cat_scope.drop_duplicates(inplace=True)
    # check if cleaned descriptions do not refer to different categories
    grouped = cat_scope.groupby(['Beschrijving', 'Euralcode'])
    if len(cat_scope.index) != grouped.ngroups:
        print 'WARNING! There are descriptions that refer to different categorization'
        e = cat_scope[grouped['Beschrijving'].transform('count') > 1]
        for col in e.columns:
            if e[col].nunique() <= 1:
                e.drop(columns=col, inplace=True)
            else:
                continue
        print e

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

if total_codes < all_categ['Euralcode'].nunique():
    print 'WARNING! Not all categorization codes were present in keyflow division'
    print all_categ['Euralcode'].nunique() - total_codes
