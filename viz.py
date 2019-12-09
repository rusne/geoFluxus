# -*- coding: utf-8 -*-
# v. python 3.7
"""
Created on Mon Nov 11 2019

@author: geoFluxus Team

"""

import pandas as pd
import matplotlib.pyplot as plt
import variables as var

# ______________________________________________________________________________
# FUNCTIONS
# ______________________________________________________________________________


def get_choices(keyword, keyflowset):
    choices_key = list(keyflowset[keyword].drop_duplicates())
    choices_key = [str(k) for k in choices_key]
    choices_key.sort()
    return choices_key


def enum_choices(choices):
    # enumerate choices for easier selection
    map = dict()
    printable = ''
    for i in range(len(choices)):
        map[i] = choices[i]
        # make a printable version
        printable += '{0} - {1}\n'.format(i, choices[i])
    return map, printable


def filtered(keyword, dataset):

    choices = get_choices(keyword, dataset)
    choice_is_not_made = True

    while choice_is_not_made:
        map, printable = enum_choices(choices)
        choice = input('Choose {0}:\n{1}\nor [ALL]\n'.format(keyword, printable))
        if choice == 'ALL' or choice == '':
            return dataset

        chosen = [int(i) for i in choice.split(' ')]
        valid = True
        for item in chosen:
            if item not in map.keys():
                print('Wrong choice:', item)
                valid = False
        if valid:
            choice_is_not_made = False

    print(chosen, 'were chosen')
    sub = []
    for key in chosen:
        item = map[key]
        sub.append(dataset[dataset[keyword].astype(str) == str(item)])
    dataset = pd.concat(sub)
    return dataset

# ______________________________________________________________________________
# PARAMETERS
# ______________________________________________________________________________


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


axis_names = ['process group', 'process', 'activity group', 'activity', 'ewc', 'year',
              'scope', 'produced in', 'treated in']
axis_dict, axis = enum_choices(axis_names)

# ______________________________________________________________________________
# LOADING ALL ANALYSIS ONCE
# ______________________________________________________________________________

analysis = []
# for scope in ['FW']:
for scope in var.scopes:
    EXPORT = "Exports_{0}_part3/".format(scope)
    anl_scope = pd.read_excel(priv_folder + 'Viz_{0}/{0}_analysis.xlsx'.format(scope))
    anl_scope['scope'] = scope
    analysis.append(anl_scope)

analysis = pd.concat(analysis)

# ______________________________________________________________________________
# FILTERS
# ______________________________________________________________________________

while True:
    # run until the break
    choice = input("""Choose Visualisation type:
                1 - Bar Chart
                2 - Pie Plot
                3 - Line Plot
                4 - Stacked Bar Chart
                5 - Printout
                0 -- quit
                """)
    if choice == '0':
        break

    viz_types = {'1': 'bar', '4': 'stacked', '3': 'line', '2': 'pie', '5': 'printout'}
    viz = viz_types[choice]

    subset = analysis.copy()
    subset = filtered('scope', subset)
    subset = filtered('year', subset)
    subset = filtered('produced in', subset)
    subset = filtered('treated in', subset)
    subset = filtered('process group', subset)
    subset = filtered('process', subset)
    subset = filtered('activity group', subset)
    subset = filtered('activity', subset)
    subset = filtered('ewc', subset)

# ______________________________________________________________________________
# VISUALISATIONS
# ______________________________________________________________________________

    if viz == 'bar' or viz == 'line' or viz == 'pie':

        x_axis = axis_dict[int(input('Choose x axis:\n' + axis))]
        y_axis = axis_dict[int(input('Choose y axis:\n' + axis))]

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

        # BAR CHART
        title = "{0} per {1}".format(x_axis, y_axis)
        # x_frame.plot.bar(subplots=True, colormap='viridis', legend=True, title=title)
        if viz == 'bar':
            x_frame.plot.bar(colormap=colors, legend=True, title=title)
        if viz == 'line':
            x_frame.plot.line(colormap=colors, legend=True, title=title)
        if viz == 'pie':
            x_frame.plot.pie(subplots=True, colormap=colors, legend=True, title=title)

        print(x_frame)
        plt.show()

    if viz == 'stacked':

        x_axis = axis_dict[int(input('Choose x axis:\n' + axis))]
        y_axis = axis_dict[int(input('Choose y axis:\n' + axis))]
        z_axis = axis_dict[int(input('Choose z axis:\n' + axis))]
        stacked = subset.groupby([x_axis, y_axis, z_axis])['amount'].sum()

        print(stacked)
        stacked = stacked.unstack()
        stacked.plot(kind='bar', stacked=True, colormap=colors)

        plt.show()

    if 'viz' == 'printout':
        for key in subset:
            print(subset[key])


# REDUCE DATA
# ______________________________________________________________________________
if False:
    cols = ['process group', 'process', 'ewc', 'year', 'amount', 'activity',
            'H_in_AMA', 'H_in_AMS', 'V_in_AMA', 'V_in_AMS']

    for scope in var.scopes:
        EXPORT = "Exports_{0}_part3/".format(scope)
        analysis = pd.read_excel(priv_folder + EXPORT + '{0}_LMA_Analysis_part4.xlsx'.format(scope))
        analysis = analysis[['VerwerkingsmethodeCode',
                             'VerwerkingsOmschrijving', 'EuralCode', 'MeldPeriodeJAAR',
                             'Gewicht_KG', 'Ontdoener_nace', 'herkomst_in_AMA',
                             'herkomst_in_AMS', 'verwerker_in_AMA', 'verwerker_in_AMS']]
        analysis.columns = cols
        analysis['amount'] = analysis['amount'] / 1000
        analysis['activity group'] = analysis['activity'].apply(lambda x: str(x)[0])
        analysis['process group'] = analysis['process group'].apply(lambda x: str(x)[0])

        # produced in
        analysis.loc[analysis['H_in_AMA'] != 'JA', 'produced in'] = '3 not AMA'
        analysis.loc[(analysis['H_in_AMA'] == 'JA') & (analysis['H_in_AMS'] != 'JA'), 'produced in'] = '2 AMA not AMS'
        analysis.loc[analysis['H_in_AMS'] == 'JA', 'produced in'] = '1 AMS'

        # treated in
        analysis.loc[analysis['V_in_AMA'] != 'JA', 'treated in'] = '3 not AMA'
        analysis.loc[(analysis['V_in_AMA'] == 'JA') & (analysis['V_in_AMS'] != 'JA'), 'treated in'] = '2 AMA not AMS'
        analysis.loc[analysis['V_in_AMS'] == 'JA', 'treated in'] = '1 AMS'

        analysis.to_excel(priv_folder + 'Viz_{0}/{0}_analysis.xlsx'.format(scope))
