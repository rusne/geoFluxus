# -*- coding: utf-8 -*-
"""
Built uppon
https://github.com/rusne/LMA-analysis/blob/master/lma_part3.py
Created on Wed Aug 22 09:17:31 2018

@author: geoFluxus Team

"""

import pandas as pd
import numpy as np

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

INPUT = "Input_{0}_part3/".format(scope)
EXPORT = "Exports_{0}_part3/".format(scope)

PART1 = "Exports_{0}_part1/".format(scope)
PART2 = "Exports_{0}_part2/".format(scope)

# _____________________________________________________________________________
# _____________________________________________________________________________
# P R E P A R I N G   F I L E S    F O R    G D S E
# _____________________________________________________________________________
# _____________________________________________________________________________

activity_groups_col = ['code', 'name']
activities_col = ['nace', 'name', 'ag']
actors_col = ['identifier', 'name', 'activity']
locations_col = ['identifier', 'geom', 'postcode', 'address', 'city', 'country',
                 'role', 'actor']
flow_chains_col = ['identifier', 'process', 'amount', 'trips', 'year', 'route',
                   'collector', 'waste', 'orig_description', 'source', 'clean',
                   'mixed', 'product', 'composition']
flows_col = ['origin', 'destination', 'flowchain']
extra_desc_col = ['type', 'desc', 'flowchain']
material_col = ['name']


LMA_part1 = pd.read_excel(priv_folder + PART1 + 'Export_LMA_Analysis_part1.xlsx')

activities = pd.read_excel(priv_folder + PART2 + 'All_actors.xlsx')

compositions = pd.read_excel()




# # ________________________________________________________________________________________________________________________________
# # ________________________________________________________________________________________________________________________________
# # 5 ) S E N S I T I V I T Y    C H E C K
# # ________________________________________________________________________________________________________________________________
# # ________________________________________________________________________________________________________________________________
#
# #######
# # STEP 5 a
# #######
#
# #sensitivity check for NACE code - take extra attention if a NACE code has very few BVDiD entries
# LMA_sens_check_nace=LMA_sens_check[['NACE','Ontdoener_BvDid']]
# LMA_sens_check_nace['Count']=1
# LMA_sens_check_nace_=LMA_sens_check_nace.groupby('NACE')
# LMA_sens_check_nace=LMA_sens_check_nace_.aggregate(np.sum).reset_index()
# LMA_sens_check_nace.sort_values('Count', ascending=True)
# LMA_sens_check_nace.loc[LMA_sens_check_nace['Count']<Sensitivity_boundary, 'Sensitive_NACE']='Yes'
# LMA_sens_check_nace.loc[LMA_sens_check_nace['Count']>=Sensitivity_boundary, 'Sensitive_NACE']='No'
#
# #######
# # STEP 5 b
# #######
# #and per postcode - find on how many differeent postcodes a certain Euralcode appears
# LMA_sens_check_postcode=LMA_sens_check[['EuralCode','Postcode']]
# LMA_sens_check_postcode['Count']=1 #count
# LMA_sens_check_postcode_=LMA_sens_check_postcode.groupby('EuralCode') # group all counts together
# LMA_sens_check_postcode=LMA_sens_check_postcode_.aggregate(np.sum).reset_index()
# LMA_sens_check_postcode.sort_values('Count', ascending=True)
# LMA_sens_check_postcode.loc[LMA_sens_check_postcode['Count']<Sensitivity_boundary, 'Sensitive_Postcode']='Yes'
# LMA_sens_check_postcode.loc[LMA_sens_check_postcode['Count']>=Sensitivity_boundary, 'Sensitive_Postcode']='No'
#
# #choose either one of these two options
# LMA_sens_information_nace=LMA_sens_check_nace.copy()
#
# #add two sensitivity columns - sensitivity on NACE and sensitivity on Postcode
# # sensitivity on NACE
# LMA_sens_information_nace['NACE']=LMA_sens_information_nace['NACE'].astype(str) #EDIT cleaning data
# LMA_sens_information_nace['NACE']=LMA_sens_information_nace['NACE'].str.rstrip('.0') #EDIT cleaning data
# LMA_w_BVDid=pd.merge(LMA,LMA_sens_information_nace,on='NACE', how='left')
# del LMA_w_BVDid['Count']
# LMA_w_BVDid.loc[LMA_w_BVDid['Sensitive_NACE']!='Yes', 'Sensitive_NACE']='No'
#
# # sensitivity on Postcode
# LMA_w_BVDid=pd.merge(LMA,LMA_sens_check_postcode,on='EuralCode', how='left')
# del LMA_w_BVDid['Count']
# LMA_w_BVDid.loc[LMA_w_BVDid['Sensitive_Postcode']!='Yes', 'Sensitive_Postcode']='No'
#
#
#
# #######
# # STEP 7
# #######
# #add our (english) categorization of the waste treatment process description
# WT_descr=pd.read_excel('Preprocessing_description.xlsx')
# WT_descr.drop_duplicates(inplace=True)
# LMA_w_BVDid = pd.merge(LMA_w_BVDid, WT_descr, on='VerwerkingsOmschrijving', how='left')
#
# # _____________________________________________________________________________
# # _____________________________________________________________________________
# # P R E P A R I N G   F I L E S    F O R    G D S E
# # _____________________________________________________________________________
# # _____________________________________________________________________________
#
# LMA_toGDSE=LMA_w_BVDid.copy()
# LMA_toGDSE.rename(columns={'MeldPeriodeJAAR': 'Year'}, inplace=True)
#
# #merge correspondance table
# LMA_toGDSE['BenamingAfval'].fillna('', inplace=True)
# LMA_toGDSE['Key'] = LMA_toGDSE['EuralCode'].map(str) + ' ' + LMA_toGDSE['BenamingAfval']
# LMA_toGDSE['Key'] = LMA_toGDSE['Key'].str.lower()
# LMA_toGDSE['Key'] = LMA_toGDSE['Key'].str.strip()
# LMA_toGDSE['Key'] = LMA_toGDSE['Key'].str.replace(u'\xa0', u' ')
#
# #clean the description
# corresp['Key'] = corresp['Key'].str.lower()
# corresp['Key'] = corresp['Key'].str.strip()
# corresp['Key'] = corresp['Key'].str.replace(u'\xa0', u' ')
# corresp.drop_duplicates(subset=['Key', 'Material'], inplace=True)
# LMA_toGDSE_corresp = pd.merge(LMA_toGDSE, corresp, on='Key', how='left')
#
# LMA_toGDSE_corresp.to_excel('Exports_{0}_part3/Export_LMA_Analysis_comprehensive_part3.xlsx'.format(scope))
#
# # _____________________________________________________________________________
# # _____________________________________________________________________________
# # C O M P O S I T I O N   T A B L E
# # _____________________________________________________________________________
# # _____________________________________________________________________________
#
# Composition_table = LMA_toGDSE_corresp[['NACE', 'Key', 'Material', 'Fraction', 'Avoidable', 'Haz', 'Processing description']]
#
#
#
#     Composition_table['Name'] = Composition_table['Key'] + " " + Composition_table['Processing description']
#     Composition_table['Source'] = 'lma2018'
#     Composition_table['Fraction'] = 1
#     Composition_table['Avoidable'] = 'FALSE'
#
# Composition_table['Hazardous'] = np.where(Composition_table['Haz'] == 'Hazardous', True, False)
#
# Composition_table.drop_duplicates(subset=(['Name', 'Avoidable']), inplace=True)
#
# Composition_table_output = Composition_table[['NACE', 'Name', 'Material', 'Fraction', 'Avoidable', 'Source', 'Hazardous']]
#
#
# Composition_table_output.to_excel('Exports_{0}_part3/Export_Composition_{0}.xlsx'.format(scope))
#
#
# # _____________________________________________________________________________
# # _____________________________________________________________________________
# # F L O W   T A B L E
# # _____________________________________________________________________________
# # _____________________________________________________________________________
#
#
# Flow_table = LMA_toGDSE.copy()
# if scope == 'FW':
#     Flow_table['Composition'] = Flow_table['Key'] + " " + Flow_table['Fraction'].astype(str) + " " + Flow_table['Processing description']
# else:
#     Flow_table['Composition'] = Flow_table['Key'] + " " + Flow_table['Processing description']
# Flow_table['Waste'] = True
# Flow_table['Source'] = 'lma2018'
#
#
# #Ontdoener  - Inzamelaar - Ontvanger - Verwerker
# Flow_table.replace(np.NaN, '',inplace=True)
# Flow_table.loc[Flow_table['Inzamelaar']!='', 'Chain1']='0-1'
# Flow_table.loc[Flow_table['Inzamelaar']=='', 'Chain1']='0-2'
# Flow_table.loc[(Flow_table['Inzamelaar']=='')&(Flow_table['Ontvanger']==''), 'Chain1']='0-3'
# Flow_table.loc[(Flow_table['Chain1']=='0-1')&(Flow_table['Ontvanger']!=''), 'Chain2']='1-2'
# Flow_table.loc[(Flow_table['Chain1']=='0-1')&(Flow_table['Ontvanger']==''), 'Chain2']='1-3'
# Flow_table.loc[(Flow_table['Chain1']=='0-2')|(Flow_table['Chain2']=='1-2')&(Flow_table['Verwerker']!=''), 'Chain3']='2-3'
#
# Flow_table_herkomst_inzamelaar=Flow_table[Flow_table['Chain1']=='0-1']
# Flow_table_herkomst_ontvanger=Flow_table[Flow_table['Chain1']=='0-2']
#
# Flow_table_inzamelaar_ontvanger=Flow_table[Flow_table['Chain2']=='1-2']
# Flow_table_inzamelaar_verwerker=Flow_table[Flow_table['Chain2']=='1-3'] #also empty
#
# Flow_table_ontvanger_verwerker=Flow_table[Flow_table['Chain3']=='2-3']
#
# def delete_columns(df):
#     del df['Chain1']
#     del df['Chain2']
#     del df['Chain3']
#     return df
#
# Flow_table_herkomst_inzamelaar=delete_columns(Flow_table_herkomst_inzamelaar)
# Flow_table_herkomst_ontvanger=delete_columns(Flow_table_herkomst_ontvanger)
# Flow_table_inzamelaar_ontvanger=delete_columns(Flow_table_inzamelaar_ontvanger)
# Flow_table_inzamelaar_verwerker=delete_columns(Flow_table_inzamelaar_verwerker)
# Flow_table_ontvanger_verwerker=delete_columns(Flow_table_ontvanger_verwerker)
#
# output_columns = ['Origin', 'Destination', 'Amount', 'Composition', 'Year', 'Waste', 'Source', 'Description', 'Process']
#
# Flow_table_herkomst_inzamelaar=Flow_table_herkomst_inzamelaar[['Ontdoener_BvDid', 'Inzamelaar_BvDid',
#                                                                'Gewicht_KG', 'Composition',
#                                                                'Year', 'Waste', 'Source',
#                                                                'BenamingAfval', 'Processing description']]
#
# Flow_table_herkomst_inzamelaar.columns = output_columns
#
#
# Flow_table_herkomst_ontvanger = Flow_table_herkomst_ontvanger[['Ontdoener_BvDid', 'Ontvanger_BvDid',
#                                                                'Gewicht_KG', 'Composition',
#                                                                'Year', 'Waste', 'Source',
#                                                                'BenamingAfval', 'Processing description']]
#
# Flow_table_herkomst_ontvanger.columns = output_columns
#
# Flow_table_inzamelaar_ontvanger = Flow_table_inzamelaar_ontvanger[['Inzamelaar_BvDid', 'Ontvanger_BvDid',
#                                                                    'Gewicht_KG', 'Composition',
#                                                                    'Year', 'Waste', 'Source',
#                                                                    'BenamingAfval', 'Processing description']]
#
# Flow_table_inzamelaar_ontvanger.columns = output_columns
#
# Flow_table_inzamelaar_verwerker = Flow_table_inzamelaar_verwerker[['Inzamelaar_BvDid', 'Verwerker_BvDid',
#                                                                    'Gewicht_KG', 'Composition',
#                                                                    'Year', 'Waste', 'Source',
#                                                                    'BenamingAfval', 'Processing description']]
#
# Flow_table_inzamelaar_verwerker.columns = output_columns
#
# Flow_table_ontvanger_verwerker = Flow_table_ontvanger_verwerker[['Ontvanger_BvDid', 'Verwerker_BvDid',
#                                                                  'Gewicht_KG', 'Composition',
#                                                                  'Year', 'Waste', 'Source',
#                                                                  'BenamingAfval', 'Processing description']]
#
# Flow_table_ontvanger_verwerker.columns = output_columns
#
# Flow_table_output = pd.concat([Flow_table_herkomst_inzamelaar,Flow_table_herkomst_ontvanger,Flow_table_inzamelaar_verwerker,Flow_table_inzamelaar_ontvanger,Flow_table_ontvanger_verwerker],ignore_index=True)
#
# Flow_table_output = Flow_table_output[Flow_table_output['Origin']!=Flow_table_output['Destination']]
#
# # Some of the actors participate in multiple flow chains
# # That creates duplicate flows (same origin-destination-composition), in that case the flows must be aggregated
# Flow_table_output['Amount'] = Flow_table_output.groupby(['Origin', 'Destination', 'Composition'])['Amount'].transform('sum')
# Flow_table_output['Amount'] = (Flow_table_output['Amount']/1000).round(0)
# Flow_table_output = Flow_table_output[Flow_table_output['Amount']>0]
# Flow_table_output.drop_duplicates(inplace=True)
#
# print len(Flow_table_output.index), 'separate flows have been exported'
#
# Flow_table_output.to_excel('Exports_{0}_part3/Export_Flows_{0}.xlsx'.format(scope))
