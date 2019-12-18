# -*- coding: utf-8 -*-
# v. python 3.7
"""
Created on Fri Nov 22 2019

@author: geoFluxus Team

"""

import pandas as pd
import matplotlib.pyplot as plt
import variables as var
import sankey

priv_folder = "Private_data/"
pub_folder = "Public_data/"
RES = "results/"

# il_links = '/Users/rusnesileryte/Google Drive/geoFluxus/nulmetingAMA/nulmeting sketch links/'

params = {'legend.fontsize': 'xx-small',
          'axes.labelsize': 'xx-small',
          'axes.titlesize': 'x-small',
          'xtick.labelsize': 'xx-small',
          'ytick.labelsize': 'xx-small',
          }
plt.rcParams.update(params)
plt.rc('legend', **{'fontsize': 'xx-small'})
colors = 'viridis'
# colors = 'nipy_spectral'
# colors = 'winter'

analysis = []
# for scope in ['FW']:
for scope in var.scopes:
    EXPORT = "Exports_{0}_part3/".format(scope)
    anl_scope = pd.read_excel(priv_folder + EXPORT + '{0}_LMA_Analysis_part4.xlsx'.format(scope))
    anl_scope['scope'] = scope
    analysis.append(anl_scope)

analysis = pd.concat(analysis)

# convert into tonnes
analysis['amount'] = analysis['Gewicht_KG'] / 1000

# ______________________________________________________________________________
# RELATIONAL TABLES
# ______________________________________________________________________________

NACEtable = pd.read_excel(pub_folder + 'NACE_table.xlsx', sheet_name='NACE_nl')
sankey_table = NACEtable[['ActivityBranch_nl', 'FW_sankey', 'CG_sankey', 'CDW_sankey']].copy()
sankey_table.rename(columns={'ActivityBranch_nl': 'branch'}, inplace=True)
NACEtable = NACEtable[['Code', 'Name_nl', 'AGcode', 'ActivityGroup_nl', 'ActivityBranch_nl']]
NACEtable.drop_duplicates(inplace=True)
NACEtable.rename(columns={'Code': 'activity',
                          'Name_nl': 'activity_name',
                          'AGcode': 'activity_group',
                          'ActivityGroup_nl': 'activity_group_name',
                          'ActivityBranch_nl': 'branch'}, inplace=True)

# add names of activity groups and activities
# analysis['activity group'] = analysis['Ontdoener_nace'].apply(lambda x: str(x)[0])
# analysis['activity'] = analysis['Ontdoener_nace']
analysis = pd.merge(analysis, NACEtable, left_on='Ontdoener_nace', right_on='activity')
processes = NACEtable[['activity', 'activity_group_name']]
processes.rename(columns={'activity': 'VerwerkingsCode',
                          'activity_group_name': 'VerwerkingsMethode'}, inplace=True)
analysis = pd.merge(analysis, processes, left_on='VerwerkingsmethodeCode', right_on='VerwerkingsCode')


# ______________________________________________________________________________
# FUNCTIONS
# ______________________________________________________________________________

def get_choices(column, dataframe):
    # extracts all the unique entries from a chosen dataframe column

    choices_key = list(dataframe[column].drop_duplicates())
    choices_key = [str(k) for k in choices_key]
    choices_key.sort()
    return choices_key


def make_matrix(subset, x_axis, y_axis):
    # takes a dataframe and turns into a matrix based on two chosen columns

    x_choices = get_choices(x_axis, subset)
    x_frame = pd.DataFrame({x_axis: x_choices})
    x_frame[x_axis] = x_frame[x_axis].astype(str)
    y_choices = get_choices(y_axis, subset)
    for y in y_choices:
        y_frame = subset[subset[y_axis].astype(str) == str(y)].copy()
        y_frame.rename(columns={'amount': y}, inplace=True)
        y_frame = y_frame.groupby([x_axis], as_index=False)[y].sum()
        y_frame[x_axis] = y_frame[x_axis].astype(str)
        x_frame = pd.merge(x_frame, y_frame, on=x_axis, how='left')

    x_frame = x_frame.fillna(0)
    x_frame.set_index(x_axis, inplace=True)

    return x_frame


def cutoff(aggset, factor, transpose=True):
    # takes a dataframe sorts and aggregates small values into the "other" field
    if transpose:
        aggset = aggset.transpose()
    aggset['sum'] = aggset.sum(axis=1)
    aggset.sort_values(by='sum', inplace=True)
    total = 0
    maxval = list(aggset['sum'])[-1] * factor
    # print(maxval)
    for index, row in aggset.iterrows():
        total += row['sum']
        aggset.loc[index, 'cutoff'] = total

    aggset.reset_index(inplace=True)
    index_col = aggset.columns[0]
    aggset.loc[aggset['cutoff'] < maxval, index_col] = 'Other'
    aggset.drop(columns=['sum', 'cutoff'], inplace=True)
    aggset = aggset.groupby(index_col).sum()

    if transpose:
        aggset = aggset.transpose()
    return aggset


def agg_mat(mats):
    mats = list(mats)
    composite = []
    mats.reverse()
    for mat in mats:
        if str(mat) != 'nan':
            composite.append(str(mat))
    comp = 'bevat ' + ' & '.join(composite)
    return comp


def get_materials(dataset, combined=False):
    # extracts materials and their corresponding amounts (with overlap)
    # outputs a barchart
    if combined:
        dataset['comb'] = dataset[['material', 'mat 2', 'mat 3', 'mat 4']].apply(lambda x: agg_mat(x), axis=1)
        materials = dataset[['comb', 'amount']]
        materials.rename(columns={'comb': 'material'}, inplace=True)
    else:
        materials = []
        for col in ['mat 4', 'mat 3', 'mat 2', 'material']:
            submat = dataset[['amount', col]].copy()
            submat.rename(columns={col: 'material'}, inplace=True)
            materials.append(submat)
        materials = pd.concat(materials)
    material_plot = materials[['amount', 'material']].groupby(['material']).sum()
    material_plot = cutoff(material_plot, 0.2, transpose=False)
    material_plot.sort_values(by='amount', inplace=True)

    return material_plot


def get_products(dataset):
    # extracts products and their corresponding amounts
    # outputs a barchart

    products = dataset[['amount', 'product']].copy()
    product_plot = products[['amount', 'product']].groupby(['product']).sum()
    product_plot = cutoff(product_plot, 0.2, transpose=False)
    product_plot.sort_values(by='amount', inplace=True)

    return product_plot


def get_ewc(dataset):
    # extracts ewc and their corresponding amounts
    # outputs a barchart

    ewc = dataset[['amount', 'EuralCode']].copy()
    ewc_plot = ewc[['amount', 'EuralCode']].groupby(['EuralCode']).sum()
    ewc_plot = cutoff(ewc_plot, 0.2, transpose=False)
    ewc_plot.sort_values(by='amount', inplace=True)

    return ewc_plot


# # _________________________________________________
# # comparison with the municipal waste
# # _________________________________________________
#
# municipal = pd.read_excel(pub_folder + 'Huishoudelijk_afval_per_gemeente.xlsx', sheet_name='totaal2018')
# municipal['AMA'] = municipal['AMA'].astype('int')
# municipal['Amsterdam'] = municipal['Amsterdam'].astype('int')
#
# # _________________________________________________
# # AA1 position in context
# # _________________________________________________
#
# analysis18 = analysis[analysis['MeldPeriodeJAAR'] == 2018]
# analysis18_AMA = analysis18[analysis18['herkomst_in_AMA'] == 'JA']
# # analysis18_AMA_noroute = analysis18_AMA[analysis18_AMA['RouteInzameling'] == 'N']
# # analysis18_AMA_noroute_noreg = analysis18_AMA_noroute[analysis18_AMA_noroute['Inzamelaarsregeling'] == 'N']
# # analysis18_AMA_primary = analysis18_AMA[analysis18_AMA['activity_group'] != 'E']
# # analysis18_AMA_primary = analysis18_AMA_primary[analysis18_AMA_primary['activity_group'] != 'X']
#
# totals = analysis18_AMA.groupby(['scope'])['amount'].sum()
#
#
# # overige18 = pd.DataFrame({'amount': [3000000]}, index=['overige'])
# totals.loc['overige'] = 1811653   # WITHOUT ROUTE INZAMELING
# totals.loc['municipal'] = 1107319
#
# title = 'All primary and secondary waste produced in AMA, in 2018.'
# print(totals)
# totals.plot.pie(y='amount', colormap=colors, legend=True, title=title, figsize=(5, 5))
# plt.savefig(RES + 'images/AA1.png', dpi=300, bbox_inches='tight')
# plt.show()
# totals.to_excel(RES + 'data/AA1.xlsx')
#
# analysis18['amount'] = analysis18['amount'].astype('int')
# analysis18_AMA = analysis18[analysis18['herkomst_in_AMA'] == 'JA']
# analysis18_AMS = analysis18[analysis18['herkomst_in_AMS'] == 'JA']
#
# totalsAMA = analysis18_AMA.groupby(['scope'], as_index=False)['amount'].sum()
# totalsAMS = analysis18_AMS.groupby(['scope'], as_index=False)['amount'].sum()
#
# # _________________________________________________
# # AA2 comparison with the municipal waste AMA
# # _________________________________________________
#
# # exclude total numbers
# municipal = municipal[municipal['keyflow'] != 'TOTAAL']
#
# municipal_AMA = municipal[['keyflow', 'AMA']]
# municipal_AMA.columns = ['keyflow', 'amount']
# municipal_AMA['scope'] = 'municipal'
#
# totalsAMA['keyflow'] = totalsAMA['scope']
# combined_AMA = pd.concat([totalsAMA, municipal_AMA], sort=True)
# combined_AMA = combined_AMA.groupby(['scope', 'keyflow'])['amount'].sum()
#
# print(combined_AMA)
# stacked_AMA = combined_AMA.unstack()
# title = 'Municipal vs. industrial waste produced in AMA, 2018'
#
# stacked_AMA.plot(kind='bar', stacked=True, colormap=colors, title=title, figsize=(5, 5))
# plt.savefig(RES + 'images/AA2.png', dpi=300, bbox_inches='tight')
# plt.show()
#
# # AA3 comparison with the municipal waste AMS
# # _________________________________________________
#
# municipal_AMS = municipal[['keyflow', 'Amsterdam']]
# municipal_AMS.columns = ['keyflow', 'amount']
# municipal_AMS['scope'] = 'municipal'
#
# totalsAMS['keyflow'] = totalsAMS['scope']
# combined_AMS = pd.concat([totalsAMS, municipal_AMS], sort=True)
# combined_AMS = combined_AMS.groupby(['scope', 'keyflow'])['amount'].sum()
#
# print(combined_AMS)
# stacked_AMS = combined_AMS.unstack()
# title = 'Municipal vs. industrial waste produced in Amsterdam, 2018'
#
# stacked_AMS.plot(kind='bar', stacked=True, colormap=colors, title=title, figsize=(5, 5))
# plt.savefig(RES + 'images/AA3.png', dpi=300, bbox_inches='tight')
# plt.show()
#
# combined_AMA['produced_in'] = 'AMA'
# combined_AMS['produced_in'] = 'Amsterdam'
# combined = pd.concat([combined_AMA, combined_AMS], sort=True)
# print(combined)
# combined.to_excel(RES + 'data/AA2-AA3.xlsx')
#
# # _________________________________________________
# # AA4 historical trends
# # _________________________________________________
#
# # all waste produced in AMA
# producedinAMA = analysis[analysis['herkomst_in_AMA'] == 'JA'].copy()
# prod_matrix = make_matrix(producedinAMA, 'MeldPeriodeJAAR', 'scope')
# prod_matrix.rename(columns={'FW': 'FW produced in AMA',
#                             'CG': 'CG produced in AMA',
#                             'CDW': 'CDW produced in AMA'}, inplace=True)
#
# # all waste treated in AMA
# treatedinAMA = analysis[analysis['verwerker_in_AMA'] == 'JA'].copy()
# treat_matrix = make_matrix(treatedinAMA, 'MeldPeriodeJAAR', 'scope')
# treat_matrix.rename(columns={'FW': 'FW treated in AMA',
#                              'CG': 'CG treated in AMA',
#                              'CDW': 'CDW treated in AMA'}, inplace=True)
#
# historical = pd.merge(prod_matrix, treat_matrix, left_index=True, right_index=True)
#
# title = 'Historical trends, all waste scopes, 2013-2018'
# historical.plot.line(colormap=colors, legend=True, title=title, figsize=(5, 5))
#
# print(historical)
# plt.savefig(RES + 'images/AA4.png', dpi=300, bbox_inches='tight')
# plt.show()
# historical.to_excel(RES + 'data/AA4.xlsx')
#
# #
# # producedinAMA_18 = producedinAMA[producedinAMA['MeldPeriodeJAAR'] == 2018]
# # unknown_ewc = get_ewc(producedinAMA_18)
# # print(unknown_ewc)
# # unknown_ewc.plot.bar(colormap=colors, legend=True, figsize=(5, 5))
# # # plt.savefig(RES + 'images/{0}3.6.png'.format(scope), dpi=300, bbox_inches='tight')
# # plt.show()
# # unknown_ewc.to_excel(RES + 'ewc.xlsx'.format(scope))
# #
# # _________________________________________________
# # spatial trends
# # _________________________________________________
# #
# # produced in
# analysis18.loc[analysis18['herkomst_in_AMA'] != 'JA', 'produced in'] = 'not AMA'
# analysis18.loc[(analysis18['herkomst_in_AMA'] == 'JA') & (analysis18['herkomst_in_AMS'] != 'JA'), 'produced in'] = 'AMA not AMS'
# analysis18.loc[analysis18['herkomst_in_AMS'] == 'JA', 'produced in'] = 'AMS'
#
# # treated in
# analysis18.loc[analysis18['verwerker_in_AMA'] != 'JA', 'treated in'] = 'not AMA'
# analysis18.loc[(analysis18['verwerker_in_AMA'] == 'JA') & (analysis18['verwerker_in_AMS'] != 'JA'), 'treated in'] = 'AMA not AMS'
# analysis18.loc[analysis18['verwerker_in_AMS'] == 'JA', 'treated in'] = 'AMS'
#
# spatial = analysis18[['amount', 'produced in', 'treated in', 'scope']].copy()
#
# spatial.loc[(spatial['produced in'] == 'not AMA') & (spatial['treated in'] == 'AMA not AMS'), 'trend'] = 1
# spatial.loc[(spatial['produced in'] == 'AMA not AMS') & (spatial['treated in'] == 'AMS'), 'trend'] = 2
# spatial.loc[(spatial['produced in'] == 'not AMA') & (spatial['treated in'] == 'AMS'), 'trend'] = 3
# spatial.loc[(spatial['produced in'] == 'AMS') & (spatial['treated in'] == 'AMS'), 'trend'] = 4
# spatial.loc[(spatial['produced in'] == 'AMA not AMS') & (spatial['treated in'] == 'AMA not AMS'), 'trend'] = 5
# spatial.loc[(spatial['produced in'] == 'AMS') & (spatial['treated in'] == 'not AMA'), 'trend'] = 6
# spatial.loc[(spatial['produced in'] == 'AMS') & (spatial['treated in'] == 'AMA not AMS'), 'trend'] = 7
# spatial.loc[(spatial['produced in'] == 'AMA not AMS') & (spatial['treated in'] == 'not AMA'), 'trend'] = 8
#
# spatial = spatial.groupby(['trend', 'scope'], as_index=False)['amount'].sum()
#
# spatial = spatial.pivot(index='trend', columns='scope')
# spatial.columns = spatial.columns.droplevel(0)
# spatial = spatial.reset_index()
#
# spatial['all'] = spatial['CDW'] + spatial['CG'] + spatial['FW']
#
# print(spatial)
# title = 'Spatial trends, all waste scopes, 2018'
# spatial.plot.bar(colormap=colors, legend=True, title=title, figsize=(5, 5))
# plt.savefig(RES + 'images/AA5.png', dpi=300, bbox_inches='tight')
# plt.show()
#
# spatial = spatial.astype('int')
# spatial.to_excel(RES + 'data/AA5.xlsx', index=False)
#
# # extract materials for Daan
#
# # organic_materials = analysis[analysis['scope'] == 'FW'].copy()
# # organic_materials = organic_materials[['mat 4', 'mat 3', 'mat 2', 'material']]
# # organic_materials.drop_duplicates(inplace=True)
# # organic_materials.to_excel('organic_materials.xlsx')
#
for scope in var.scopes:
# for scope in ['FW']:
# if False:
    # RESULTS = "results/{0}_results".format(scope)
    # analysis = pd.read_excel(priv_folder + EXPORT + '{0}_LMA_Analysis_part4.xlsx'.format(scope))
    analysis_sc = analysis[analysis['scope'] == scope].copy()

    # fill empty fields with unknown values
    analysis_sc[['mixed', 'clean', 'direct_use']] = analysis_sc[['mixed', 'clean', 'direct_use']].fillna('unknown')

    analysis_sc['clean'] = analysis_sc['clean'].astype('str')
    analysis_sc['mixed'] = analysis_sc['mixed'].astype('str')
    analysis_sc['direct_use'] = analysis_sc['direct_use'].astype('str')
    analysis_sc['product'] = analysis_sc['product'].astype('str')
    analysis_sc['composite'] = analysis_sc['composite'].astype('str')
    # pandas do not allow nullable boolean field, therefore this workaround
    analysis_sc.loc[analysis_sc['clean'] == '1.0', 'clean'] = 'clean'
    analysis_sc.loc[analysis_sc['clean'] == '0.0', 'clean'] = 'polluted'
    analysis_sc.loc[analysis_sc['clean'] == 'nan', 'clean'] = 'unknown'
    analysis_sc.loc[analysis_sc['mixed'] == '1.0', 'mixed'] = 'mixed'
    analysis_sc.loc[analysis_sc['mixed'] == '0.0', 'mixed'] = 'pure'
    analysis_sc.loc[analysis_sc['mixed'] == 'nan', 'mixed'] = 'unknown'
    analysis_sc.loc[analysis_sc['direct_use'] == '1.0', 'direct_use'] = 'direct'
    analysis_sc.loc[analysis_sc['direct_use'] == '0.0', 'direct_use'] = 'indirect'
    analysis_sc.loc[analysis_sc['direct_use'] == 'nan', 'direct_use'] = 'unknown'
    analysis_sc.loc[analysis_sc['product'] != 'nan', 'is_product'] = 'product'
    analysis_sc.loc[(analysis_sc['composite'] != 'nan') & ((analysis_sc['product'] == 'nan') | (analysis_sc['product'] == 'composiet')), 'is_product'] = 'composite'
    analysis_sc.loc[(analysis_sc['composite'] == 'nan') & (analysis_sc['product'] == 'nan'), 'is_product'] = 'unknown'

    # # _________________________________________________
    # # SC1.1 distribution of economic activities over time
    #
    # analysisAMA = analysis_sc[analysis_sc['herkomst_in_AMA'] == 'JA'].copy()
    #
    # nace_year = make_matrix(analysisAMA, 'MeldPeriodeJAAR', 'activity_group_name')
    # nace_year = cutoff(nace_year, 0.2)
    #
    # print(nace_year)
    # title = 'Contribution of economic activities to the total {0} waste produced in AMA, per year'.format(scope)
    # nace_year.plot.area(colormap=colors, title=title, legend=True, figsize=(8, 5))
    # plt.savefig(RES + 'images/{0}1.1.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # nace_year.to_excel(RES + 'data/{0}1.1.xlsx'.format(scope))
    #
    # # _________________________________________________
    # # SC1.2 distribution of processing methods over time
    #
    # analysisAMAtreat = analysis_sc[analysis_sc['verwerker_in_AMA'] == 'JA'].copy()
    #
    # process_year = make_matrix(analysisAMAtreat, 'MeldPeriodeJAAR', 'VerwerkingsOmschrijving')
    # process_year = cutoff(process_year, 0.2)
    # print(process_year)
    # title = 'Contribution of processing methods to the total {0} waste treated in AMA, per year'.format(scope)
    # process_year.plot.area(colormap=colors, title=title, legend=True, figsize=(8, 5))
    # plt.savefig(RES + 'images/{0}1.2.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # process_year.to_excel(RES + 'data/{0}1.2.xlsx'.format(scope))

    # # _________________________________________________
    # # SC1.3 Sankey
    #
    # sankey = analysis_AMA[['activity_group_name', 'VerwerkingsMethode', 'amount']].copy()
    # sankey = sankey.groupby(['activity_group_name', 'VerwerkingsMethode'])['amount'].sum()
    # print(sankey)
    # sankey.to_excel(RES + 'data/{0}1.3.xlsx'.format(scope))

    # _________________________________________________
    # SC2 MATERIALS
    # _________________________________________________

    # only regard the year of 2018 for the further analysis
    analysis18 = analysis_sc[analysis_sc['MeldPeriodeJAAR'] == 2018].copy()

    # _________________________________________________
    # total amount of waste produced and treated in AMA
    total = analysis18['amount'].sum()

    print('{0} ton {1} in de Metropoolregio Amsterdam (2018)'.format(total, var.titles_NL[scope]))

    # _________________________________________________
    # SC2.1 Clean vs Polluted waste

    # title = 'Ratio of clean vs. polluted {0} produced and treated in AMA in 2018'.format(var.titles[scope])
    # clean_plot = analysis18[['amount', 'clean']].groupby(['clean']).sum()
    # print(clean_plot)
    # clean_plot.plot.pie(y='amount', colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}2.1.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # clean_plot.to_excel(RES + 'data/{0}2.1.xlsx'.format(scope))

    polluted = analysis18[analysis18['clean'] == 'polluted']
    clean = analysis18[(analysis18['clean'] == 'unknown') | (analysis18['clean'] == 'clean')]

    analysis18.loc[analysis18['clean'] == 'polluted', 'status'] = 'polluted'

    # _________________________________________________
    # SC2.2 Mixed vs Pure waste

    # title = 'Ratio of mixed vs. pure Clean {0} produced and treated in AMA in 2018'.format(var.titles[scope])
    # mixed_plot = clean[['amount', 'mixed']].groupby(['mixed']).sum()
    # print(mixed_plot)
    # mixed_plot.plot.pie(y='amount', colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}2.2.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # mixed_plot.to_excel(RES + 'data/{0}2.2.xlsx'.format(scope))

    pure = clean[clean['mixed'] == 'pure']
    mixed = clean[(clean['mixed'] == 'unknown') | (clean['mixed'] == 'mixed')]

    analysis18.loc[(analysis18['clean'] != 'polluted') & (clean['mixed'] == 'pure'), 'status'] = 'pure'

    # _________________________________________________
    # SC2.3 Product vs Composite vs Unknown

    # title = 'Ratio of Products vs. Composites {0} produced and treated in AMA in 2018'.format(var.titles[scope])
    # product_plot = mixed[['amount', 'is_product']].groupby(['is_product']).sum()
    # print(product_plot)
    # product_plot.plot.pie(y='amount', colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}2.3.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # product_plot.to_excel(RES + 'data/{0}2.3.xlsx'.format(scope))

    product = mixed[mixed['is_product'] == 'product']
    composite = mixed[mixed['is_product'] == 'composite']
    unknown = mixed[mixed['is_product'] == 'unknown']

    analysis18.loc[(analysis18['clean'] != 'polluted') & (clean['mixed'] != 'pure') & (mixed['is_product'] == 'composite'), 'status'] = 'composite'
    analysis18.loc[(analysis18['clean'] != 'polluted') & (clean['mixed'] != 'pure') & (mixed['is_product'] == 'unknown'), 'status'] = 'unknown'

    # _________________________________________________
    # SC2.4 Direct vs Indirect use products

    # title = 'Ratio of directly vs. indirectly usable Clean Mixed {0} produced and treated in AMA in 2018'.format(var.titles[scope])
    # direct_plot = product[['amount', 'direct_use']].groupby(['direct_use']).sum()
    # print(direct_plot)
    # direct_plot.plot.pie(y='amount', colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}2.4.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # direct_plot.to_excel(RES + 'data/{0}2.4.xlsx'.format(scope))

    direct = product[product['direct_use'] == 'direct']
    indirect = product[product['direct_use'] == 'indirect']
    unknown = mixed[mixed['direct_use'] == 'unknown']

    analysis18.loc[(analysis18['clean'] != 'polluted') & (clean['mixed'] != 'pure') & (mixed['is_product'] == 'product') & (product['direct_use'] == 'direct'), 'status'] = 'direct product'
    analysis18.loc[(analysis18['clean'] != 'polluted') & (clean['mixed'] != 'pure') & (mixed['is_product'] == 'product') & (product['direct_use'] == 'indirect'), 'status'] = 'indirect product'

    # # _________________________________________________
    # # master pie
    #
    # master_pie = analysis18[['amount', 'status']].groupby(['status']).sum()
    # print(master_pie)
    # master_pie.plot.pie(y='amount', colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}_masterpie.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # master_pie.to_excel(RES + 'data/{0}_masterpie.xlsx'.format(scope))

    # _________________________________________________
    # master sankey

    # analysis18['Processing'] = analysis18['VerwerkingsmethodeCode'] + ' ' + analysis18['VerwerkingsOmschrijving']

    # master_sankey = analysis18[['branch', 'status', 'Processing', 'amount']].copy()
    # sankey_col = '{0}_sankey'.format(scope)
    # sankey_table_sc = sankey_table[['branch', sankey_col]].drop_duplicates()
    # master_sankey = pd.merge(master_sankey, sankey_table_sc, on='branch')
    #
    # # master_sankey.to_excel(RES + 'testsankey.xlsx'.format(scope))
    # master_sankey = master_sankey.groupby([sankey_col, 'status', 'Processing'], as_index=False)['amount'].sum()
    # sankey.draw_sankey(master_sankey)
    # master_sankey.to_excel(RES + 'data/{0}_mastersankey.xlsx'.format(scope))


    # _________________________________________________
    # SC3.1 Polluted

    if scope == 'CDW':
        polluted_materials = get_materials(polluted)
        polluted_materials['status'] = 'vervuild materialen'
        # print(polluted_materials)
        # polluted_materials.plot.bar(colormap=colors, legend=True, figsize=(5, 5))
        # plt.savefig(RES + 'images/{0}3.1.png'.format(scope), dpi=300, bbox_inches='tight')
        # plt.show()
        # polluted_materials.to_excel(RES + 'data/{0}3.1.xlsx'.format(scope))

        # polluted_sankey = polluted[['activity_group_name', 'VerwerkingsMethode', 'amount']].copy()
        # polluted_sankey = polluted_sankey.groupby(['activity_group_name', 'VerwerkingsMethode'])['amount'].sum()
        # polluted_sankey.to_excel(RES + 'data/{0}4.2.xlsx'.format(scope))
    else:
        polluted_materials = pd.DataFrame()

    # _________________________________________________
    # SC3.2 Pure

    pure_materials = get_materials(pure)
    pure_materials.rename(columns={'amount': 'pure materialen'}, inplace=True)
    # print(pure_materials)
    # pure_materials.plot.bar(colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}3.2.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # pure_materials.to_excel(RES + 'data/{0}3.2.xlsx'.format(scope))

    # pure_sankey = pure[['activity_group_name', 'VerwerkingsMethode', 'amount']].copy()
    # pure_sankey = pure_sankey.groupby(['activity_group_name', 'VerwerkingsMethode'])['amount'].sum()
    # pure_sankey.to_excel(RES + 'data/{0}4.2.xlsx'.format(scope))
    #
    # _________________________________________________
    # SC3.3 Composite

    comp_materials = get_materials(composite, combined=True)
    comp_materials.rename(columns={'amount': 'composieten'}, inplace=True)
    # print(comp_materials)
    # comp_materials.plot.bar(colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}3.3.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # comp_materials.to_excel(RES + 'data/{0}3.3.xlsx'.format(scope))

    # comp_sankey = composite[['activity_group_name', 'VerwerkingsMethode', 'amount']].copy()
    # comp_sankey = comp_sankey.groupby(['activity_group_name', 'VerwerkingsMethode'])['amount'].sum()
    # comp_sankey.to_excel(RES + 'data/{0}4.3.xlsx'.format(scope))

    # _________________________________________________
    # SC3.4 Direct product

    direct_materials = get_materials(direct, combined=True)
    direct_materials.rename(columns={'amount': 'materialen in direct gebruikbare producten'}, inplace=True)
    # print(direct_materials)
    # direct_materials.plot.bar(colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}3.4.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # direct_materials.to_excel(RES + 'data/{0}3.4.xlsx'.format(scope))

    direct_products = get_products(direct)
    direct_products.rename(columns={'amount': 'direct gebruikbare producten'}, inplace=True)
    # print(direct_products)
    # direct_products.plot.bar(colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}5.4.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # direct_products.to_excel(RES + 'data/{0}5.4.xlsx'.format(scope))

    # direct_sankey = direct[['activity_group_name', 'VerwerkingsMethode', 'amount']].copy()
    # direct_sankey = direct_sankey.groupby(['activity_group_name', 'VerwerkingsMethode'])['amount'].sum()
    # direct_sankey.to_excel(RES + 'data/{0}4.4.xlsx'.format(scope))

    # _________________________________________________
    # SC3.5 Indirect product

    indirect_materials = get_materials(indirect, combined=True)
    indirect_materials.rename(columns={'amount': 'materialen in indirect gebruikbare producten'}, inplace=True)
    # print(indirect_materials)
    # indirect_materials.plot.bar(colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}3.5.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # indirect_materials.to_excel(RES + 'data/{0}3.5.xlsx'.format(scope))

    indirect_products = get_products(indirect)
    indirect_products.rename(columns={'amount': 'indirect gebruikbare producten'}, inplace=True)
    # print(indirect_products)
    # indirect_products.plot.bar(colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}5.5.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # indirect_products.to_excel(RES + 'data/{0}5.5.xlsx'.format(scope))

    # indirect_sankey = indirect[['activity_group_name', 'VerwerkingsMethode', 'amount']].copy()
    # indirect_sankey = indirect_sankey.groupby(['activity_group_name', 'VerwerkingsMethode'])['amount'].sum()
    # indirect_sankey.to_excel(RES + 'data/{0}4.5.xlsx'.format(scope))

    # _________________________________________________
    # SC3.6 Unknown

    unknown_ewc = get_ewc(unknown)
    unknown_ewc.rename(columns={'amount': 'onbekend'}, inplace=True)
    # print(unknown_ewc)
    # unknown_ewc.plot.bar(colormap=colors, legend=True, figsize=(5, 5))
    # plt.savefig(RES + 'images/{0}3.6.png'.format(scope), dpi=300, bbox_inches='tight')
    # plt.show()
    # unknown_ewc.to_excel(RES + 'data/{0}3.6.xlsx'.format(scope))

    # unknown_sankey = unknown[['activity_group_name', 'VerwerkingsMethode', 'amount']].copy()
    # unknown_sankey = unknown_sankey.groupby(['activity_group_name', 'VerwerkingsMethode'])['amount'].sum()
    # unknown_sankey.to_excel(RES + 'data/{0}4.6.xlsx'.format(scope))

    all = pd.concat([polluted_materials, unknown_ewc, comp_materials, indirect_materials, indirect_products, direct_materials, direct_products, pure_materials])
    all.plot.barh(stacked=True, colormap=colors, legend=True, figsize=(12, 6))
    plt.savefig(RES + 'images/{0}_bars.png'.format(scope), dpi=300, bbox_inches='tight')
    plt.show()
    all.to_excel(RES + 'data/{0}_bars.xlsx'.format(scope))

# _________________________________________________
# _________________________________________________
# V A L I D A T I O N
# _________________________________________________
# _________________________________________________

# list the biggest producers and if they belong to the right NACE code
# only for the producers in AMA, others do not have a NACE code
# check all years

# valid = analysis[['Ontdoener_Key', 'Ontdoener_nace', 'Ontdoener_name', 'scope', 'amount']].copy()
# valid = valid[valid['Ontdoener_nace'] != 'W-0001']
# valid = valid[valid['Ontdoener_nace'] != 'X-0002']
# FW = valid[valid['scope'] == 'FW']
# CG = valid[valid['scope'] == 'CG']
# CDW = valid[valid['scope'] == 'CDW']
# FW['amount'] = FW.groupby(['Ontdoener_Key', 'Ontdoener_nace', 'Ontdoener_name'])['amount'].transform(sum)
# CG['amount'] = CG.groupby(['Ontdoener_Key', 'Ontdoener_nace', 'Ontdoener_name'])['amount'].transform(sum)
# CDW['amount'] = CDW.groupby(['Ontdoener_Key', 'Ontdoener_nace', 'Ontdoener_name'])['amount'].transform(sum)
#
# FW.drop_duplicates(inplace=True)
# CG.drop_duplicates(inplace=True)
# CDW.drop_duplicates(inplace=True)
#
# FW = FW.sort_values('amount', ascending=False).head(20)
# CG = CG.sort_values('amount', ascending=False).head(20)
# CDW = CDW.sort_values('amount', ascending=False).head(20)
#
# FW.to_excel(priv_folder + 'FW_actor_validation.xlsx')
# CG.to_excel(priv_folder + 'CG_actor_validation.xlsx')
# CDW.to_excel(priv_folder + 'CDW_actor_validation.xlsx')
