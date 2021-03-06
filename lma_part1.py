# -*- coding: utf-8 -*-
"""
Built uppon
https://github.com/rusne/LMA-analysis/blob/master/lma_part1.py
Created on Wed Aug 22 09:17:31 2018

@author: geoFluxus Team

"""

import pandas as pd
import numpy as np
import clean
import variables as var
import math

import warnings  # ignore unnecessary warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
pd.options.mode.chained_assignment = None

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

print 'Loading LMA data.......'
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

# add the total waste per year back to each Afvalstroomnummer
LMA_agg = pd.merge(LMA_filt_year, ASN_massa, on=['Afvalstroomnummer', 'MeldPeriodeJAAR'], how='left')

# check if afvalstroomnummer & year combination is unique per unique entry
if len(ASN_massa.index) != len(LMA_agg.index):
    print 'WARNING!'
    print 'afvalstroomnummer & year combination is not unique per unique entry'
    LMA_agg.to_excel("LMA_agg.xlsx")

total_flow_chains = len(LMA_agg)
print "Data has been aggregated per afvalstroomnummer,"
print "the total number of flow chains is", total_flow_chains

# correct the anomaly in the specific afvalstroomnummer as agreed with LMA
LMA_agg.loc[LMA_agg['Afvalstroomnummer'] == '070080100223', 'Gewicht_KG'] = LMA_agg['Gewicht_KG'] / 10000
LMA_agg.loc[LMA_agg['Afvalstroomnummer'] == '070080100404', 'Gewicht_KG'] = LMA_agg['Gewicht_KG'] / 10000
LMA_agg.loc[LMA_agg['Afvalstroomnummer'] == '070080100444', 'Gewicht_KG'] = LMA_agg['Gewicht_KG'] / 10000
LMA_agg.loc[LMA_agg['Afvalstroomnummer'] == '070080100548', 'Gewicht_KG'] = LMA_agg['Gewicht_KG'] / 10000



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

# LMA_agg[LMA_agg.columns[:18]].to_excel('herkomst.xlsx')

LMA_agg.loc[LMA_agg['Herkomst_Postcode'] == '', 'Herkomst_Postcode'] = LMA_agg['Ontdoener_Postcode']
LMA_agg.loc[LMA_agg['Herkomst_Huisnr'] == '', 'Herkomst_Huisnr'] = LMA_agg['Ontdoener_Huisnr']
LMA_agg.loc[LMA_agg['Herkomst_Straat'] == '', 'Herkomst_Straat'] = LMA_agg['Ontdoener_Straat']
LMA_agg.loc[LMA_agg['Herkomst_Plaats'] == '', 'Herkomst_Plaats'] = LMA_agg['Ontdoener_Plaats']


# clean the BenamingAfval field
LMA_agg['BenamingAfval'] = LMA_agg['BenamingAfval'].astype('unicode')
LMA_agg['BenamingAfval'] = LMA_agg['BenamingAfval'].apply(clean.clean_description)

# _____________________________________________________________________________
# _____________________________________________________________________________
# E X P O R T I N G     A L L    A C T O R S
# _____________________________________________________________________________
# _____________________________________________________________________________

comprehensive = LMA_agg.copy()

# export all actors participating in flows
# this list is meant for matching actors with LISA database,
# therefore ontdoener location is used as ontdoener address instead of Herkomst

actor_data_cols = ['Name', 'Orig_name', 'Postcode', 'Plaats', 'Straat', 'Huisnr',
                   'Jaar', 'Key', 'Activity', 'Who']

actorsets = []
for role in var.map_roles:

    postcode = '{0}_Postcode'.format(role)
    plaats = '{0}_Plaats'.format(role)
    straat = '{0}_Straat'.format(role)
    huisnr = '{0}_Huisnr'.format(role)
    key = '{0}_Key'.format(role)
    orig_name = '{0}_Origname'.format(role)

    # data cleaning
    comprehensive[postcode] = comprehensive[postcode].astype('unicode')
    comprehensive[postcode] = comprehensive[postcode].apply(clean.clean_postcode)

    if role != 'Herkomst':
        # preserve the original name
        comprehensive[orig_name] = comprehensive[role].copy()
        comprehensive[role] = comprehensive[role].astype('unicode')
        comprehensive[role] = comprehensive[role].apply(clean.clean_company_name)

    comprehensive[plaats] = comprehensive[plaats].astype('unicode')
    comprehensive[plaats] = comprehensive[plaats].apply(clean.clean_address)

    comprehensive[straat] = comprehensive[straat].astype('unicode')
    comprehensive[straat] = comprehensive[straat].apply(clean.clean_address)

    comprehensive[huisnr] = comprehensive[huisnr].astype('unicode')
    comprehensive[huisnr] = comprehensive[huisnr].apply(clean.clean_huisnr)

    if role == 'Herkomst':
        comprehensive[key] = comprehensive['Ontdoener'] + ' ' + comprehensive[postcode]
        comprehensive[key] = comprehensive[key].apply(lambda x: x.strip())
        comprehensive['Activity'] = ''
        actorset = comprehensive[['Ontdoener', 'Ontdoener_Origname', postcode, plaats, straat, huisnr, 'MeldPeriodeJAAR', key, 'Activity']]
    elif role == 'Verwerker':
        comprehensive[key] = comprehensive[role] + ' ' + comprehensive[postcode]
        # remove whitespace in case name or postcode are not present
        comprehensive[key] = comprehensive[key].apply(lambda x: x.strip())
        comprehensive['Activity'] = comprehensive['VerwerkingsmethodeCode']
        actorset = comprehensive[[role, orig_name, postcode, plaats, straat, huisnr, 'MeldPeriodeJAAR', key, 'Activity']]
    else:
        comprehensive[key] = comprehensive[role] + ' ' + comprehensive[postcode]
        comprehensive[key] = comprehensive[key].apply(lambda x: x.strip())
        comprehensive['Activity'] = ''
        if role == 'Ontdoener':
            comprehensive.loc[comprehensive['RouteInzameling'] == 'J', key] = comprehensive[key] + ' route'
        actorset = comprehensive[[role, orig_name, postcode, plaats, straat, huisnr, 'MeldPeriodeJAAR', key, 'Activity']]
    actorset['Who'] = role
    actorset.columns = actor_data_cols

    actorsets.append(actorset)


actors = pd.concat(actorsets)

# actors = actors[actors['Name'] != '']
actors.drop_duplicates(subset=['Key', 'Who', 'Jaar', 'Activity'], inplace=True)

actors['Adres'] = actors['Straat'] + ' ' + actors['Huisnr']


# find out how many actors have multiple roles within the chain
actor_roles = actors[['Key', 'Who']]
# actor_roles['LMA_key'] = actor_roles['Name'] + ' ' + actor_roles['Postcode']
grouped_roles = actor_roles.groupby('Key')
grouped_roles = grouped_roles.agg(lambda x: ', '.join(x)).reset_index()

roles_summary = grouped_roles.groupby('Who')['Key'].count()
roles_summary.reset_index(name='count')
roles_summary.rename(columns={'Key': 'count'}, inplace=True)
roles_summary.to_excel(pub_folder + EXPORT + 'actor_roles_summary.xlsx')

# _____________________________________________________________________________
# _____________________________________________________________________________
# E X P O R T I N G     A L L    A C T O R S   B Y   R O L E
# _____________________________________________________________________________
# _____________________________________________________________________________

# export all actors for matching with NACE code
export_actors = actors.copy()
export_actors.to_excel(priv_folder + EXPORT + 'Export_LMA_all_actors.xlsx')
print export_actors['Key'].nunique(), 'unique actors in total'

# NACE assignment has a hierarchy:
# first verwerker, then ontvanger, then ontdoener, then the rest
# e.g. if an actor is a verwerker,
# then it gets assigned to the NACE code as a verwerker and not as others

hier_roles = list(var.map_roles)
roles = []
roles.append(hier_roles.pop(hier_roles.index('Verwerker')))
roles.append(hier_roles.pop(hier_roles.index('Ontvanger')))
roles.append(hier_roles.pop(hier_roles.index('Ontdoener')))
# except for herkomst as this depends on the ontdoener
hier_roles.remove('Herkomst')
roles += hier_roles

for role in roles:

    exp = export_actors[export_actors['Who'] == role]
    exp.to_excel(priv_folder + EXPORT + 'Export_LMA_{0}.xlsx'.format(role))

    print exp['Key'].nunique(), '{0}s have been exported for NACE matching'.format(role)

    export_actors = export_actors[(export_actors['Key'].isin(exp['Key']) == False)]


# find out if there are any actors without postcode
actors_without_postcode = actors[actors['Postcode'] == '']

if len(actors_without_postcode.index) > 0:
    actors_without_postcode.to_excel(priv_folder + EXPORT + 'Export_LMA_actors_without_postcode.xlsx')
    print len(actors_without_postcode.index), 'actors do not have a postcode'
else:
    print 'All actors have a postcode'

# export locations separately
locations = actors[['Key', 'Postcode', 'Plaats', 'Adres']].copy()
locations['Key'] = locations['Key'].apply(lambda x: str(x).strip(' route'))
locations.drop_duplicates(subset=['Key'], inplace=True)

# check if all actors can be geolocated at once
if len(locations.index) > 25000:
    parts = int(math.ceil(len(locations.index) / 25000.0))
    for i in range(parts):
        start = i * 25000
        end = (i + 1) * 25000
        if end > len(locations.index):
            end = len(locations.index)
        print start, end
        part = locations[start:end]
        part.to_excel(priv_folder + EXPORT + 'Export_LMA_locations_{0}.xlsx'.format(end), index=False)

locations.to_excel(priv_folder + EXPORT + 'Export_LMA_locations.xlsx', index=False)

print len(locations.index), 'locations have been exported'

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

comprehensive_columns = ['Afvalstroomnummer', 'VerwerkingsmethodeCode',
                         'VerwerkingsOmschrijving', 'RouteInzameling',
                         'Inzamelaarsregeling', 'ToegestaanbijInzamelaarsregeling',
                         'EuralCode', 'BenamingAfval', 'MeldPeriodeJAAR',
                         'EuralNaam', 'Haz', 'Gewicht_KG', 'Aantal_vrachten']

comprehensive_columns += ['{0}_Key'.format(role) for role in var.map_roles]

comprehensive = comprehensive[comprehensive_columns]
comprehensive.to_excel(priv_folder + EXPORT + 'Export_LMA_Analysis_part1.xlsx')
