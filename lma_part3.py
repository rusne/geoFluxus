# -*- coding: utf-8 -*-
"""
Built uppon
https://github.com/rusne/LMA-analysis/blob/master/lma_part3.py
Created on Wed Aug 22 09:17:31 2018

@author: geoFluxus Team

"""

import pandas as pd
import variables as var

import warnings  # ignore unnecessary warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
pd.options.mode.chained_assignment = None

# ______________________________________________________________________________
# ______________________________________________________________________________

# P R E P A R A T I O N
# ______________________________________________________________________________
# ______________________________________________________________________________

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
INPUT_2 = "Input_{0}_part2/".format(scope)

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
locations_col = ['geom', 'postcode', 'address', 'city', 'actor']
flow_chains_col = ['identifier', 'process', 'amount', 'trips', 'year', 'route',
                   'collector', 'waste', 'orig_description', 'source', 'clean',
                   'mixed', 'direct_use']
flows_col = ['flowchain', 'origin', 'destination', 'origin_role',
             'destination_role']
extra_desc_col = ['type', 'desc', 'flowchain']
material_col = ['name', 'flowchain']
product_col = ['name', 'flowchain']
composite_col = ['name', 'flowchain']

print 'Reading input files........'

flows = pd.read_excel(priv_folder + PART1 + 'Export_LMA_Analysis_part1.xlsx')

actors = pd.read_excel(priv_folder + PART2 + 'Export_All_actors.xlsx')

locations = pd.read_csv(priv_folder + INPUT_2 + '{0}_locations_WGS84.csv'.format(scope), encoding='utf-8')
# !!!! temp fix - remove duplicates
locations.drop_duplicates(subset=['Key'], inplace=True)
# print locations.loc[locations['Key'] == 'A MANDELL GMBH']

compositions = pd.read_excel(pub_folder + INPUT + 'Categorization.xlsx')

# _____________________________________________________________________________
# Activities & Activity groups
# _____________________________________________________________________________

print 'Exporting Activities & Activity Groups.......'

NACEtable = pd.read_excel(pub_folder + 'NACE_table.xlsx', sheet_name='NACE_nl')

# all activities from matched actors,
# processing activities will be loaded separetely
actors['activenq'] = actors['activenq'].astype(str)
actors['activenq'] = actors['activenq'].str.zfill(4)
NACEtable['Digits'] = NACEtable['Digits'].astype(str)
NACEtable['Digits'] = NACEtable['Digits'].str.zfill(4)
act_activ = pd.merge(actors, NACEtable, how='left', left_on='activenq', right_on='Digits', validate='m:1')

# if len(e.index) > 0:
#     print 'WARNING! not all activity codes have been found in the NACE table'
#     print e['activenq'].drop_duplicates()

activity_groups = act_activ[['AGcode', 'ActivityGroup_nl']]
activity_groups.drop_duplicates(inplace=True)

activity_groups.columns = activity_groups_col
activity_groups.to_excel(priv_folder + EXPORT + '{0}_activity_groups.xlsx'.format(scope))
activity_groups.to_csv(priv_folder + EXPORT + '{0}_activity_groups.csv'.format(scope), encoding='utf-8')

activities = act_activ[['Code', 'Name_nl', 'AGcode']]
activities.drop_duplicates(inplace=True)

activities.columns = activities_col
activities.to_excel(priv_folder + EXPORT + '{0}_activities.xlsx'.format(scope))
activities.to_csv(priv_folder + EXPORT + '{0}_activities.csv'.format(scope), encoding='utf-8')

# _____________________________________________________________________________
# Actors & Locations
# _____________________________________________________________________________


print 'Merging flows with Actors and their Locations.......'

for role in var.map_roles:
    print role
    role_key = role + '_Key'
    role_id = role + '_id'

    # merge NACE code
    if role == 'Ontvanger':
        flows_updated = pd.merge(flows, act_activ[['Key', 'Orig_name']], how='left', left_on=role_key, right_on='Key', validate='m:1')
        flows_updated.rename(columns={'Orig_name': '{0}_name'.format(role),
                                      'Key': 'Ontvanger_loc_key'}, inplace=True)
        # give NACE according to hazardous or non-hazardous treatment
        flows_updated.loc[flows_updated['Haz'] == 'Non-hazardous', 'Ontvanger_nace'] = 'E-3821'
        flows_updated.loc[flows_updated['Haz'] == 'Hazardous', 'Ontvanger_nace'] = 'E-3822'
        # update actor key
        flows_updated[role_key] = flows_updated[role_key] + " " + flows_updated['Ontvanger_nace']
        flows = flows_updated.copy()

    elif role == 'Verwerker':
        flows_updated = pd.merge(flows, act_activ[['Key', 'Orig_name']], how='left', left_on=role_key, right_on='Key', validate='m:1')
        flows_updated.rename(columns={'Orig_name': '{0}_name'.format(role),
                                      'Key': 'Verwerker_loc_key'}, inplace=True)
        # give NACE according to processing method
        flows_updated['Verwerker_nace'] = flows_updated['VerwerkingsmethodeCode']
        # update actor key
        flows_updated[role_key] = flows_updated[role_key] + " " + flows_updated['Verwerker_nace']
        flows = flows_updated.copy()

    elif role != 'Herkomst':
        flows_updated = pd.merge(flows, act_activ[['Key', 'Code', 'Orig_name']], how='left', left_on=role_key, right_on='Key', validate='m:1')
        flows_updated.rename(columns={'Code': '{0}_nace'.format(role),
                                      'Orig_name': '{0}_name'.format(role)}, inplace=True)
        flows_updated.drop(columns=['Key'], inplace=True)
        flows = flows_updated.copy()

    # merge location
    if role == 'Verwerker' or role == 'Ontvanger':
        flows_updated = pd.merge(flows, locations, how='left', left_on='{0}_loc_key'.format(role), right_on='Key', validate='m:1')
        flows_updated.rename(columns={'WKT': '{0}_wkt'.format(role)}, inplace=True)
        flows_updated.drop(columns=['Key'], inplace=True)
        flows = flows_updated.copy()
    elif role != 'Ontdoener':
        flows_updated = pd.merge(flows, locations, how='left', left_on=role_key, right_on='Key', validate='m:1')
        flows_updated.rename(columns={'WKT': '{0}_wkt'.format(role)}, inplace=True)
        flows_updated.drop(columns=['Key'], inplace=True)
        flows = flows_updated.copy()

    # give id
    if role != 'Ontdoener':
        flows[role_id] = flows[role_key].apply(lambda x: '_'.join(x.split()))
    else:
        flows[role_id] = flows['Herkomst_Key'].apply(lambda x: '_'.join(x.split()))

    # reorder columns for better human readability of the output file
    cols = list(flows.columns)
    i = cols.index(role_key)
    end = cols.index('Verwerker_Key')
    col_order = cols[:i + 1] + cols[end + 1:] + cols[i + 1:end + 1]
    flows = flows[col_order]

flows.to_excel('overview.xlsx')

print 'Exporting Actors and their Locations.......'

# Actor identifier = name + postcode + nace (only for ontvangers & verwerkers)
#               stripped from extra symbols, "_" instead of spaces

loc_list = []
act_list = []

var.map_roles.remove('Herkomst')
for role in var.map_roles:
    name = '{0}_name'.format(role)
    nace = '{0}_nace'.format(role)
    key = '{0}_Key'.format(role)
    id = '{0}_id'.format(role)
    actors_export = flows[[id, name, nace]].copy()
    # actors_export['id'] = actors_export['id'] + '_' + actors_export[nace]
    actors_export.columns = actors_col

    if role == 'Ontdoener':
        geom_col = 'Herkomst_wkt'
        loc_key = 'Herkomst_Key'
    elif role == 'Ontvanger':
        geom_col = 'Ontvanger_wkt'
        loc_key = 'Ontvanger_loc_key'
    elif role == 'Verwerker':
        geom_col = 'Verwerker_wkt'
        loc_key = 'Verwerker_loc_key'
    else:
        geom_col = '{0}_wkt'.format(role)
        loc_key = key
    locs_export = flows[[geom_col, key, loc_key, id]]
    locs_export.columns = ['geom', 'actor_key', 'loc_key', 'actor']
    # locs_export['actor'] = locs_export['actor_key'].apply(lambda x: '_'.join(x.split()))

    act_list.append(actors_export)
    loc_list.append(locs_export)


actors_export = pd.concat(act_list)
actors_export.drop_duplicates(inplace=True)
# !!!!!!!!! mock up actor with no name in LMA
actors_export.loc[actors_export['name'].isna(), 'name'] = 'ONBEKEND'
actors_export.loc[actors_export['activity'].isna(), 'activity'] = 'WU-0000'
actors_export.to_excel(priv_folder + EXPORT + '{0}_actors.xlsx'.format(scope))
actors_export.to_csv(priv_folder + EXPORT + '{0}_actors.csv'.format(scope), encoding='utf-8')

addresses = pd.read_excel(priv_folder + PART1 + 'Export_LMA_locations.xlsx')
locations_export = pd.concat(loc_list)
locations_export.drop_duplicates(inplace=True)
locations_exp_add = pd.merge(locations_export, addresses, left_on='loc_key', right_on='Key', how='left')

locations_exp_add = locations_exp_add[['geom', 'Postcode', 'Adres', 'Plaats', 'actor']]
locations_exp_add.columns = locations_col
locations_exp_add.to_excel(priv_folder + EXPORT + '{0}_locations.xlsx'.format(scope))
locations_exp_add.to_csv(priv_folder + EXPORT + '{0}_locations.csv'.format(scope), encoding='utf-8')

# _____________________________________________________________________________
# Flows & Flow chains
# _____________________________________________________________________________

flows['id'] = flows['Afvalstroomnummer'] + '_' + flows['MeldPeriodeJAAR'].astype(str)

print 'Connecting flows with the waste classification........'

flows = pd.merge(flows, compositions, on=['EuralCode', 'BenamingAfval'], validate='m:1')

print 'Exporting flow chains.......'

flow_chains = flows[['id', 'VerwerkingsmethodeCode',
                     'Gewicht_KG', 'Aantal_vrachten', 'MeldPeriodeJAAR',
                     'RouteInzameling', 'Inzamelaarsregeling', 'EuralCode',
                     'BenamingAfval', 'clean', 'mixed', 'direct_use']].copy()

flow_chains['amount'] = flow_chains['Gewicht_KG'] / 1000
flow_chains.loc[flow_chains['RouteInzameling'] == 'J', 'RouteInzameling'] = True
flow_chains.loc[flow_chains['RouteInzameling'] == 'N', 'RouteInzameling'] = False
flow_chains.loc[flow_chains['Inzamelaarsregeling'] == 'J', 'Inzamelaarsregeling'] = True
flow_chains.loc[flow_chains['Inzamelaarsregeling'] == 'N', 'Inzamelaarsregeling'] = False
flow_chains['source'] = 'lma2019'

flow_chains.rename(columns={'id': 'identifier',
                            'VerwerkingsmethodeCode': 'process',
                            'Aantal_vrachten': 'trips',
                            'MeldPeriodeJAAR': 'year',
                            'RouteInzameling': 'route',
                            'Inzamelaarsregeling': 'collector',
                            'EuralCode': 'waste',
                            'BenamingAfval': 'orig_description'}, inplace=True)

flow_chains['clean'] = flow_chains['clean'].astype('str')
flow_chains['mixed'] = flow_chains['mixed'].astype('str')
flow_chains['direct_use'] = flow_chains['direct_use'].astype('str')
# pandas do not allow nullable boolean field, therefore this workaround
flow_chains.loc[flow_chains['clean'] == '1.0', 'clean'] = 'TRUE'
flow_chains.loc[flow_chains['clean'] == '0.0', 'clean'] = 'FALSE'
flow_chains.loc[flow_chains['clean'] == 'nan', 'clean'] = ''
flow_chains.loc[flow_chains['mixed'] == '1.0', 'mixed'] = 'TRUE'
flow_chains.loc[flow_chains['mixed'] == '0.0', 'mixed'] = 'FALSE'
flow_chains.loc[flow_chains['mixed'] == 'nan', 'mixed'] = ''
flow_chains.loc[flow_chains['direct_use'] == '1.0', 'direct_use'] = 'TRUE'
flow_chains.loc[flow_chains['direct_use'] == '0.0', 'direct_use'] = 'FALSE'
flow_chains.loc[flow_chains['direct_use'] == 'nan', 'direct_use'] = ''


flow_chains = flow_chains[flow_chains_col]

flow_chains.to_excel(priv_folder + EXPORT + '{0}_flowchains.xlsx'.format(scope))
flow_chains.to_csv(priv_folder + EXPORT + '{0}_flowchains.csv'.format(scope), encoding='utf-8')


print 'Splitting chains into separate flows.......'


def chain(seq, roles):

    ch = []
    for i in range(len(seq)):
        if seq[i] != ' ':
            ch.append(roles[i])

    return ch


role_keys = ['{0}_Key'.format(r) for r in var.map_roles]
flows['chain'] = flows[role_keys].apply(lambda x: chain(x, var.map_roles), axis=1)

fp = {'flowchain': [],
      'origin': [],
      'destination': [],
      'origin_role': [],
      'destination_role': []}

for index, row in flows.iterrows():
    for i in range(len(row['chain']) - 1):
        orig = row['chain'][i]
        dest = row['chain'][i + 1]
        fp['flowchain'].append(row['id'])
        fp['origin'].append(row['{0}_id'.format(orig)])
        fp['destination'].append(row['{0}_id'.format(dest)])
        fp['origin_role'].append(orig)
        fp['destination_role'].append(dest)

flowparts = pd.DataFrame.from_dict(fp)
flowparts.to_excel(priv_folder + EXPORT + '{0}_flows.xlsx'.format(scope))
flowparts.to_csv(priv_folder + EXPORT + '{0}_flows.csv'.format(scope), encoding='utf-8')

# _____________________________________________________________________________
# Materials, products and compositions
# _____________________________________________________________________________


print 'Exporting materials, products and compositions......'


mat_1 = flows[['material', 'id']]
mat_1.columns = material_col
mat_2 = flows[['mat 2', 'id']]
mat_2.columns = material_col
mat_3 = flows[['mat 3', 'id']]
mat_3.columns = material_col
mat_4 = flows[['mat 4', 'id']]
mat_4.columns = material_col

materials = pd.concat([mat_1, mat_2, mat_3, mat_4])
materials.dropna(inplace=True)
materials.drop_duplicates(inplace=True)

materials.to_excel(priv_folder + EXPORT + '{0}_materials.xlsx'.format(scope))
materials.to_csv(priv_folder + EXPORT + '{0}_materials.csv'.format(scope), encoding='utf-8')

comp_1 = flows[['composite', 'id']]
comp_1.columns = material_col
comp_2 = flows[['composite 2', 'id']]
comp_2.columns = material_col

composites = pd.concat([comp_1, comp_2])
composites.dropna(inplace=True)
composites.drop_duplicates(inplace=True)

composites.to_excel(priv_folder + EXPORT + '{0}_composites.xlsx'.format(scope))
composites.to_csv(priv_folder + EXPORT + '{0}_composites.csv'.format(scope), encoding='utf-8')

products = flows[['product', 'id']]
products.columns = material_col
products.dropna(inplace=True)
products.drop_duplicates(inplace=True)

products.to_excel(priv_folder + EXPORT + '{0}_products.xlsx'.format(scope))
products.to_csv(priv_folder + EXPORT + '{0}_products.csv'.format(scope), encoding='utf-8')


descriptions = ['reason', 'origin', 'colour', 'state', 'size', 'consistency',
                'other', 'm-type', 'c-type', 'p-type']

descs = []
desc_col = ['desc', 'flowchain']
for d in descriptions:
    desc = flows[[d, 'id']]
    desc.columns = desc_col
    desc['type'] = d
    descs.append(desc)

extra_descriptions = pd.concat(descs)
extra_descriptions.dropna(inplace=True)
extra_descriptions.drop_duplicates(inplace=True)

extra_descriptions.to_excel(priv_folder + EXPORT + '{0}_extra_descriptions.xlsx'.format(scope))
extra_descriptions.to_csv(priv_folder + EXPORT + '{0}_extra_descriptions.csv'.format(scope), encoding='utf-8')

# _____________________________________________________________________________
#   Final analysis table
# _____________________________________________________________________________


print 'Exporting analysis table......'


flows.to_excel(priv_folder + EXPORT + '{0}_LMA_Analysis_part3.xlsx'.format(scope))

# TODO
# check why not all the actors got a nace code
# validate everything



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
