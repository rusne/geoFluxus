# -*- coding: utf-8 -*-
"""
Built uppon
https://github.com/rusne/LMA-analysis/blob/master/lma_part1.py
Created on Wed Aug 22 09:17:31 2018

@author: geoFluxus Team

"""

import pandas as pd
import numpy as np

import warnings  # ignore unnecessary warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
pd.options.mode.chained_assignment = None


def clean_white_space(string):
    return ' '.join(string.split())

# ______________________________________________________________________________
# ______________________________________________________________________________

# 0)  P R E P A R A T I O N
# ______________________________________________________________________________
# ______________________________________________________________________________

# choose scope: Food Waste, Construction&Demolition Waste OR Consumption Goods
while True:
    scope = raw_input('Choose scope: CDW / FW / CG\n')
    if scope == 'CDW' or scope == 'FW' or scope == 'CG':
        break
    else:
        print 'Wrong choice.'


priv_folder = "Private_data/"
pub_folder = "Public_data/"

INPUT = "Input_{0}_part1/".format(scope)
EXPORT = "Exports_{0}_part1/".format(scope)

LMA_dataset = priv_folder + "LMA_data/{0}_data/LMA_{0}_all.xlsx".format(scope)

LMA = pd.read_excel(LMA_dataset)

LMA.rename(columns={"Afzender_Huisnummer": "Afzender_Huisnr",
                   "Handelaar_Huisnummer": "Handelaar_Huisnr",
                   "Ontvanger_Huisnummer": "Ontvanger_Huisnr",
                   "Verwerker_Huisnummer": "Verwerker_Huisnr"}, inplace=True)

# ______________________________________________________________________________
# ______________________________________________________________________________
# T R A N S F O R M I N G   D A T A   F I L E S   F O R   A N A L Y S I S
# ______________________________________________________________________________
# ______________________________________________________________________________


# Remove those data entries that do not have year specified
LMA_filt_year = LMA[LMA.MeldPeriodeJAAR.notnull()]
print len(LMA.index) - len(LMA_filt_year.index),
print 'lines do not have a year specified and have been removed'


# Find the aggregated weight per year for each Afvalstroomnummer (as now the waste is reported per month)

ASN_massa = LMA_filt_year[['Afvalstroomnummer', 'MeldPeriodeJAAR', 'Gewicht_KG', 'Aantal_vrachten']].groupby(['Afvalstroomnummer', 'MeldPeriodeJAAR']).sum()


del LMA_filt_year['MeldPeriodeMAAND']
del LMA_filt_year['Gewicht_KG']
del LMA_filt_year['Aantal_vrachten']
LMA_filt_year.drop_duplicates(inplace=True)

#add the total waste per year back to each Afvalstroomnummer
LMA_agg = pd.merge(LMA_filt_year, ASN_massa, on=['Afvalstroomnummer', 'MeldPeriodeJAAR'], how='left')

# check if afvalstroomnummer & year combination is unique per unique entry
if len(ASN_massa.index) != len(LMA_agg.index):
    print 'WARNING!'
    print 'afvalstroomnummer & year combination is not unique per unique entry'
    LMA_agg.to_excel("LMA_agg.xlsx")

total_flow_chains = len(LMA_agg)
print "Data has been aggregated per afvalstroomnummer,"
print "the total number of flow chains is", total_flow_chains


# there are four different 'Waste' locations
#   Ontdoener  -  the company that generated the waste
#   Herkomst   -  the actual location the waste is picked up
#   Afzender   -  the company/responsible to arrange the pick-up
#   Verwerker  -  the company that does waste treatment

# if waste originates at ontdoener, the 'Herkomst field is empty'
# if waste originates elsewhere, herkomst field is filled
# if herkomst field is empty, we fill it with the ontdoener location
# then herkomst means that the waste has been picked up at that location

# clean empty fields to avoid errors in merging
LMA_agg.replace(np.NaN, '', inplace=True)

LMA_agg.loc[LMA_agg['Herkomst_Postcode'] == '', 'Herkomst_Postcode'] = LMA_agg['Ontdoener_Postcode']
LMA_agg.loc[LMA_agg['Herkomst_Huisnr'] == '', 'Herkomst_Huisnr'] = LMA_agg['Ontdoener_Huisnr']
LMA_agg.loc[LMA_agg['Herkomst_Straat'] == '', 'Herkomst_Straat'] = LMA_agg['Ontdoener_Straat']
LMA_agg.loc[LMA_agg['Herkomst_Plaats'] == '', 'Herkomst_Plaats'] = LMA_agg['Ontdoener_Plaats']


# clean the BenamingAfval field for both streams
LMA_agg['BenamingAfval'] = LMA_agg['BenamingAfval'].astype('unicode')
LMA_agg['BenamingAfval'] = LMA_agg['BenamingAfval'].str.lower()
LMA_agg['BenamingAfval'] = LMA_agg['BenamingAfval'].str.strip()
LMA_agg['BenamingAfval'] = LMA_agg['BenamingAfval'].str.replace(u'\xa0', u' ')
LMA_agg['BenamingAfval'] = LMA_agg['BenamingAfval'].apply(clean_white_space)


# _____________________________________________________________________________
# _____________________________________________________________________________
# E X P O R T I N G     A L L    A C T O R S
# _____________________________________________________________________________
# _____________________________________________________________________________

comprehensive = LMA_agg.copy()

# export all actors participating in flows
# this list is meant for matching actors with LISA database,
# therefore ontdoener location is used as ontdoener address instead of Herkomst

actor_data_cols = ['Name', 'Postcode', 'Plaats', 'Straat', 'Huisnr', 'Jaar', 'Who']

actorsets = []
for role in ['Ontdoener', 'Inzamelaar', 'Ontvanger', 'Verwerker']:

    postcode = '{0}_Postcode'.format(role)
    plaats = '{0}_Plaats'.format(role)
    straat = '{0}_Straat'.format(role)
    huisnr = '{0}_Huisnr'.format(role)

    # data cleaning
    comprehensive[postcode] = comprehensive[postcode].astype('unicode')
    comprehensive[postcode] = comprehensive[postcode].str.replace(' ','')
    comprehensive[postcode] = comprehensive[postcode].str.upper()

    comprehensive[role] = comprehensive[role].astype('unicode')
    comprehensive[role] = comprehensive[role].str.upper()
    comprehensive[role] = comprehensive[role].str.replace('BV', '')
    comprehensive[role] = comprehensive[role].str.replace('B.V.', '')
    comprehensive[role] = comprehensive[role].str.replace('B.V.', '')
    comprehensive[role] = comprehensive[role].apply(clean_white_space)

    comprehensive[plaats] = comprehensive[plaats].astype('unicode')
    comprehensive[plaats] = comprehensive[plaats].str.strip()
    comprehensive[plaats] = comprehensive[plaats].str.upper()
    comprehensive[plaats] = comprehensive[plaats].apply(clean_white_space)

    comprehensive[straat] = comprehensive[straat].astype('unicode')
    comprehensive[straat] = comprehensive[straat].str.strip()
    comprehensive[straat] = comprehensive[straat].str.upper()
    comprehensive[straat] = comprehensive[straat].apply(clean_white_space)

    actorset = comprehensive[[role, postcode, plaats, straat, huisnr, 'MeldPeriodeJAAR']]
    actorset['Who'] = role
    actorset.columns = actor_data_cols

    actorsets.append(actorset)


actors = pd.concat(actorsets)

actors.drop_duplicates(subset=['Name', 'Postcode', 'Who'], inplace=True)
actors = actors[actors['Name'] != '']


# find out how many actors have multiple roles within the chain
actor_roles = actors[['Name', 'Postcode', 'Who']]
actor_roles['LMA_key'] = actor_roles['Name'] + ' ' + actor_roles['Postcode']
grouped_roles = actor_roles.groupby('LMA_key')
grouped_roles = grouped_roles.agg(lambda x: ', '.join(x)).reset_index()

roles = grouped_roles.groupby('Who')['LMA_key'].count()
roles.reset_index(name='count')
roles.rename(columns={'LMA_key': 'count'}, inplace=True)
roles.to_excel(pub_folder + EXPORT + 'actor_roles_summary.xlsx')


actors.to_excel(priv_folder + EXPORT + 'Export_LMA_actors.xlsx')

actors_without_postcode = actors[actors['Postcode'] == '']


if len(actors_without_postcode.index) > 0:
    actors_without_postcode.to_excel(priv_folder + EXPORT + 'Export_LMA_actors_without_postcode.xlsx')
    print len(actors_without_postcode.index), 'actors do not have a postcode'
else:
    print 'All actors have a postcode'


# _____________________________________________________________________________
# _____________________________________________________________________________
# E X P O R T I N G     A L L    C O M P O S I T I O N S
# _____________________________________________________________________________
# _____________________________________________________________________________

# export all compositions that need to be matched with the material hierarchy

compositions = comprehensive[['EuralCode', 'BenamingAfval']]
compositions.drop_duplicates(inplace=True)
print len(compositions.index), 'unique waste compositions (ewc + BenamingAfval) have been found'
compositions.to_excel(pub_folder + EXPORT + 'Export_LMA_compositions.xlsx')

# _____________________________________________________________________________
# _____________________________________________________________________________
# E X P O R T I N G    A N A L Y S I S    F I L E
# _____________________________________________________________________________
# _____________________________________________________________________________


comprehensive.to_excel(priv_folder + EXPORT + 'Export_LMA_Analysis_part1.xlsx')
