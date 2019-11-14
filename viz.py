# -*- coding: utf-8 -*-
# v. python 3.7
"""
Created on Mon Nov 11 2019

@author: geoFluxus Team

"""

import pandas as pd
import matplotlib.pyplot as plt
import time
import variables as var

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

priv_folder = "Private_data/"
pub_folder = "Public_data/"


if True:
    # scope = 'FW'
    # title = 'Organic Waste'
    # scope = 'CG'
    # title = 'Consumption Goods'
    scope = 'CDW'
    title = 'Construction & Demolition Waste'

    EXPORT = "Exports_{0}_part3/".format(scope)

    analysis = pd.read_excel(priv_folder + 'Viz_{0}/{0}_analysis.xlsx'.format(scope))

    # TREATMENT PER YEAR, CHOSEN KEYFLOW
    # ______________________________________________________________________________
    if False:

        processing = analysis[['VerwerkingsOmschrijving']].drop_duplicates()
        for year in var.all_years:
            sub_year = sub[sub['MeldPeriodeJAAR'] == year].copy()
            sub_year.rename(columns={'amount': year}, inplace=True)
            sub_year = sub_year.groupby(['VerwerkingsOmschrijving'], as_index=False)[year].sum()
            processing = pd.merge(processing, sub_year, on='VerwerkingsOmschrijving', how='left')

        processing = processing.fillna(0)
        processing.set_index('VerwerkingsOmschrijving', inplace=True)

        # BAR CHART
        processing.plot.bar(subplots=True, colormap='viridis', legend=True, title=title)

        # LINE PER YEAR
        # processing = processing.transpose()
        # processing.plot.line(colormap=colors, legend=True, title=title)

        plt.show()

    # IN / OUT -- AMA / AMS, CHOSEN KEYFLOW
    # ______________________________________________________________________________
    if True:
        # STACKED BAR CHARTS
        total = analysis[['year', 'amount', 'H_in_AMA', 'V_in_AMA', 'H_in_AMS', 'V_in_AMS']].copy()
        # stacked = pd.DataFrame(data={'direction': ['produced in AMS'] * 3 + ['treated in AMS']* 3,
        #                              'origin/dest': ['outside AMA', 'in AMA, outside AMS', 'in AMS'] * 2})
        # produced in AMS
        produced_in_AMS = total[total['H_in_AMS'] == 'JA'].copy()
        produced_in_AMS.loc[produced_in_AMS['V_in_AMA'] != 'JA', 'origin/dest'] = 'outside AMA'
        produced_in_AMS.loc[(produced_in_AMS['V_in_AMA'] == 'JA') & (produced_in_AMS['V_in_AMS'] != 'JA'), 'origin/dest'] = 'in AMA, outside AMS'
        produced_in_AMS.loc[produced_in_AMS['V_in_AMS'] == 'JA', 'origin/dest'] = 'in AMS'
        # produced_in_AMS = produced_in_AMS.groupby(['year', 'origin/dest'], as_index=False)['amount'].sum()
        produced_in_AMS['direction'] = 'produced in AMS'

        # treated in AMS
        treated_in_AMS = total[total['V_in_AMS'] == 'JA'].copy()
        treated_in_AMS.loc[treated_in_AMS['H_in_AMA'] != 'JA', 'origin/dest'] = 'outside AMA'
        treated_in_AMS.loc[(treated_in_AMS['H_in_AMA'] == 'JA') & (treated_in_AMS['H_in_AMS'] != 'JA'), 'origin/dest'] = 'in AMA, outside AMS'
        treated_in_AMS.loc[treated_in_AMS['H_in_AMS'] == 'JA', 'origin/dest'] = 'in AMS'
        # treated_in_AMS = treated_in_AMS.groupby(['year', 'origin/dest'], as_index=False)['amount'].sum()
        treated_in_AMS['direction'] = 'treated in AMS'

        # for year in var.all_years:
        #     pro = produced_in_AMS[produced_in_AMS['year'] == year]
        #     tre = treated_in_AMS[treated_in_AMS['year'] == year]
        #     # stacked = pd.merge(stacked, pd.concat([pro, tre]), on=['direction', 'origin/dest'])
        #     # stacked.rename(columns={'amount': year}, inplace=True)
        #     # stacked.drop(columns=['year'], inplace=True)
        #     stacked = pd.concat([pro, tre])
        #     stacked = stacked.groupby(['direction', 'origin/dest'])['amount'].sum()
        #     print(stacked)
        #     stacked.unstack().plot(kind='bar', stacked=True, colormap=colors, title=year)
        stacked = pd.concat([produced_in_AMS, treated_in_AMS])
        stacked = stacked.groupby(['year', 'direction', 'origin/dest'])['amount'].sum()

        stacked = stacked.unstack()

        categories = ['in AMS', 'in AMA, outside AMS', 'outside AMA']
        stacked.columns = pd.CategoricalIndex(stacked.columns.values,
                                              ordered=True,
                                              categories=categories)
        stacked = stacked.sort_index(axis=1)
        print(stacked)

        stacked.plot(kind='bar', stacked=True, colormap=colors)

        plt.show()


# TOTAL PER YEAR, ALL KEYFLOWS
# ______________________________________________________________________________

if False:
    anls = dict()
    for scope in var.scopes:
        anl = pd.read_excel(priv_folder + 'Viz_{0}/{0}_analysis.xlsx'.format(scope))
        anls[scope] = anl

    overview = pd.DataFrame(data={'year': var.all_years})
    for scope in var.scopes:
        total = anls[scope][['year', 'amount']].copy()
        total = total.groupby(['year'], as_index=False)['amount'].sum()
        total.rename(columns={'amount': var.titles[scope]}, inplace=True)
        overview = pd.merge(overview, total, on='year')
    overview.set_index('year', inplace=True)

    # # LINE PLOT
    # overview.plot.line(colormap=colors, legend=True)

    # # PIE PLOT
    # overview = overview.transpose()
    # print overview
    # # ALL YEARS SEPARETELY
    # overview.plot.pie(subplots=True, colormap=colors, autopct='%1.1f', fontsize='xx-small', labels=None)
    # # ALL YEARS SUMMED
    # overview['sum'] = overview.sum(axis=1)
    # overview['label'] = overview.index + ' ' + overview['sum'].apply(lambda x: str(int(round(x, 0)))) + 't'
    # overview.plot.pie(y='sum', colormap=colors, labels=overview['label'], legend=False)

# ----------------------------
# AMA
# ----------------------------
    overview = pd.DataFrame(data={'year': var.all_years})
    for scope in var.scopes:
        print(var.titles[scope])
        total = anls[scope][['year', 'amount', 'H_in_AMA', 'V_in_AMA']].copy()

        # produced in AMA
        pAMA = total[total['H_in_AMA'] == 'JA'].copy()
        pAMA = pAMA.groupby(['year'], as_index=False)['amount'].sum()
        pAMA.rename(columns={'amount': scope + ' produced in AMA'}, inplace=True)
        overview = pd.merge(overview, pAMA, on='year')

        # treated in AMA
        tAMA = total[total['V_in_AMA'] == 'JA'].copy()
        tAMA = tAMA.groupby(['year'], as_index=False)['amount'].sum()
        tAMA.rename(columns={'amount': scope + ' treated in AMA'}, inplace=True)
        overview = pd.merge(overview, tAMA, on='year')

        # produced & treated in AMA
        ptAMA = total[(total['V_in_AMA'] == 'JA') & (total['H_in_AMA'] == 'JA')].copy()
        ptAMA = ptAMA.groupby(['year'], as_index=False)['amount'].sum()
        ptAMA.rename(columns={'amount': scope + ' produced & treated in AMA'}, inplace=True)
        overview = pd.merge(overview, ptAMA, on='year')

# ----------------------------
# AMS
# ----------------------------
    # overview = pd.DataFrame(data={'year': var.all_years})
    for scope in var.scopes:
        print(var.titles[scope])
        total = anls[scope][['year', 'amount', 'H_in_AMS', 'V_in_AMS']].copy()

        # produced in AMS
        pAMS = total[total['H_in_AMS'] == 'JA'].copy()
        pAMS = pAMS.groupby(['year'], as_index=False)['amount'].sum()
        pAMS.rename(columns={'amount': scope + ' produced in AMS'}, inplace=True)
        overview = pd.merge(overview, pAMS, on='year')

        # treated in AMS
        tAMS = total[total['V_in_AMS'] == 'JA'].copy()
        tAMS = tAMS.groupby(['year'], as_index=False)['amount'].sum()
        tAMS.rename(columns={'amount': scope + ' treated in AMS'}, inplace=True)
        overview = pd.merge(overview, tAMS, on='year')

        # produced & treated in AMS
        ptAMS = total[(total['V_in_AMS'] == 'JA') & (total['H_in_AMS'] == 'JA')].copy()
        ptAMS = ptAMS.groupby(['year'], as_index=False)['amount'].sum()
        ptAMS.rename(columns={'amount': scope + ' produced & treated in AMS'}, inplace=True)
        overview = pd.merge(overview, ptAMS, on='year')

    overview.set_index('year', inplace=True)

    # LINE PLOT
    # overview.plot.line(colormap=colors, legend=True)

    plt.show()

# REDUCE DATA
# ______________________________________________________________________________
if False:
    cols = ['process', 'ewc', 'year', 'amount', 'nace',
            'H_in_AMA', 'H_in_AMS', 'V_in_AMA', 'V_in_AMS']

    for scope in var.scopes:
        EXPORT = "Exports_{0}_part3/".format(scope)
        analysis = pd.read_excel(priv_folder + EXPORT + '{0}_LMA_Analysis_part4.xlsx'.format(scope))
        analysis = analysis[['VerwerkingsOmschrijving', 'EuralCode', 'MeldPeriodeJAAR',
                             'Gewicht_KG', 'Ontdoener_nace', 'herkomst_in_AMA',
                             'herkomst_in_AMS', 'verwerker_in_AMA', 'verwerker_in_AMS']]
        analysis.columns = cols
        analysis['amount'] = analysis['amount'] / 1000

        analysis.to_excel(priv_folder + 'Viz_{0}/{0}_analysis.xlsx'.format(scope))
