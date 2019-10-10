# -*- coding: utf-8 -*-
"""
Created on Mon Oct 7 2019

@author: geoFluxus Team

"""

import pandas as pd
import numpy as np
import time

# Reads all the original LMA output files, merges them, removes the duplicates
# and partitions into smaller files per keyflow & year


priv_folder = "Private_data/"
pub_folder = "Public_data/"

orig_LMA_dataset = "Private_data/LMA_data/Raw_data/Hfsdt 03_17_20.xlsx"
# orig_LMA_dataset = "Private_data/LMA_data/Raw_data/Test_data.xlsx"


# selection of the columns we want to include in our analysis
LMA_columns = ['Afvalstroomnummer', 'VerwerkingsmethodeCode',
               'VerwerkingsOmschrijving', 'RouteInzameling',
               'Inzamelaarsregeling', 'ToegestaanbijInzamelaarsregeling',
               'EuralCode', 'BenamingAfval', 'MeldPeriodeJAAR',
               'MeldPeriodeMAAND', 'Gewicht_KG', 'Aantal_vrachten',
               # Ontdoener
               'Ontdoener', 'Ontdoener_Postcode', 'Ontdoener_Plaats',
               'Ontdoener_Straat', 'Ontdoener_Huisnr',
               # Herkomst
               'Herkomst_Postcode', 'Herkomst_Straat', 'Herkomst_Plaats',
               'Herkomst_Huisnr',
               # Afzender
               'Afzender', 'Afzender_Postcode', 'Afzender_Straat',
               'Afzender_Plaats', 'Afzender_Huisnummer',
               # Inzamelaar
               'Inzamelaar', 'Inzamelaar_Postcode', 'Inzamelaar_Straat',
               'Inzamelaar_Plaats', 'Inzamelaar_Huisnr',
               # Bemiddelaar
               'Bemiddelaar', 'Bemiddelaar_Postcode', 'Bemiddelaar_Straat',
               'Bemiddelaar_Plaats', 'Bemiddelaar_Huisnr',
               # Handelaar
               'Handelaar', 'Handelaar_Postcode', 'Handelaar_Straat',
               'Handelaar_Plaats', 'Handelaar_Huisnummer',
               # Ontvanger
               'Ontvanger', 'Ontvanger_Postcode', 'Ontvanger_Straat',
               'Ontvanger_Plaats', 'Ontvanger_Huisnummer',
               # Verwerker
               'Verwerker', 'Verwerker_Postcode', 'Verwerker_Straat',
               'Verwerker_Plaats', 'Verwerker_Huisnummer']

print "Loading LMA dataset......."
start_time = time.time()

# Reading in the LMA data
LMA_1 = pd.read_excel(orig_LMA_dataset, sheet_name='1.OM Ontvangers in MRA', dtype=object)
LMA_1 = LMA_1[LMA_columns]

print '1.OM Ontvangers in MRA have been loaded, ',
print 'dataset length:', len(LMA_1.index), 'lines,',
m, s = divmod(time.time() - start_time, 60)
print 'time elapsed:', m, 'min', s, 's'

LMA_2 = pd.read_excel(orig_LMA_dataset, sheet_name='2. OM Ontdoeners in MRA', dtype=object)
LMA_2 = LMA_2[LMA_columns]
print '2. OM Ontdoeners in MRA in MRA have been loaded, ',
print 'dataset length:', len(LMA_2.index), 'lines,',
m, s = divmod(time.time() - start_time, 60)
print 'time elapsed:', m, 'min', s, 's'

# LMA_3 = pd.read_excel(orig_LMA_dataset, sheetname='3. Afgiftemelding')
# LMA_3 = LMA_3[LMA_columns]
# print '3. Afgiftemelding have been loaded'

# Concatenating 3 sheets into one dataset
LMA = pd.concat([LMA_1, LMA_2]) # , LMA_3]) # skipping Afgiftemelding for now
combined = len(LMA.index)

# Removing duplicates
LMA.drop_duplicates(inplace=True)
cleaned = len(LMA.index)

print combined - cleaned, 'duplicate lines have been found and removed'
print 'Final dataset consists of ', len(LMA.index), ' lines'

# clean empty fields to avoid errors in merging
LMA.replace(np.NaN, '', inplace=True)

LMA.rename(columns={"Afzender_Huisnummer": "Afzender_Huisnr",
                   "Handelaar_Huisnummer": "Handelaar_Huisnr",
                   "Ontvanger_Huisnummer": "Ontvanger_Huisnr",
                   "Verwerker_Huisnummer": "Verwerker_Huisnr"}, inplace = True)


# ______________________________________________________________________________
#       Filtering by keyflow based on the EuralCode
# _______________________________________________________________________________

LMA['EuralCode'] = LMA['EuralCode'].astype(str)

for scope in ('CDW', 'FW', 'CG'):
    print "filtering ", scope, 'keyflow.......'

    INPUT = "Input_{0}_part1/".format(scope)
    EXPORT = "LMA_data/{0}_data/".format(scope)

    Eural = pd.read_excel(pub_folder + INPUT + 'EURAL_codes_{0}.xlsx'.format(scope), dtype=object)
    # data cleaning
    Eural['EuralCode'] = Eural['EuralCode'].astype(str)
    Eural['EuralCode'] = Eural['EuralCode'].str.replace(' ', '')
    Eural['EuralCode'] = Eural['EuralCode'].str.replace('*', '')

    LMA_filt = pd.merge(LMA, Eural, on='EuralCode')

    print 'After filtering for the relevant EWC codes', scope,
    print 'dataset consists of ', len(LMA_filt.index), ' lines'

    LMA_filt.to_excel(priv_folder + EXPORT + 'LMA_{0}_all.xlsx'.format(scope))

# ______________________________________________________________________________
#       Splitting dataset in separate files per year
# ______________________________________________________________________________

    for year in [2013, 2014, 2015, 2016, 2017, 2018]:
        LMA_filt_year = LMA_filt[LMA_filt['MeldPeriodeJAAR'] == year]
        print scope, 'dataset for', year, 'consists of ',
        print len(LMA_filt_year), 'lines'

        LMA_filt_year.to_excel(priv_folder + EXPORT + 'LMA_{0}_{1}.xlsx'.format(scope, year))

m, s = divmod(time.time() - start_time, 60)
print 'total time elapsed:', m, 'min', s, 's'
