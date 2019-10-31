# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 2019

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


# choose scope: Food Waste, Construction & Demolition Waste, Consumption Goods

while True:
    scope = raw_input('Choose scope: CDW / FW / CG\n')
    if scope == 'CDW' or scope == 'FW' or scope == 'CG':
        break
    else:
        print 'Wrong choice.'

priv_folder = "Private_data/"
pub_folder = "Public_data/"

INPUT = "Input_{0}_part2/".format(scope)
EXPORT = "Exports_{0}_part2/".format(scope)

PART1 = "Exports_{0}_part1/".format(scope)

# ______________________________________________________________________________
# Reading the LMA Verwerker list with their roles
# ______________________________________________________________________________


print 'Loading LMA actors.......'
LMA_actors = pd.read_excel(priv_folder + PART1 + 'Export_LMA_verwerker.xlsx')

print 'Loading comprehensive analysis table'
comprehensive = pd.read_excel(priv_folder + PART1 + 'Export_LMA_Analysis_part1.xlsx')

# ______________________________________________________________________________
# Preparing NACE codes for matching
# ______________________________________________________________________________

codes = comprehensive[['Verwerker_Key', 'VerwerkingsmethodeCode', 'VerwerkingsOmschrijving']]
codes.drop_duplicates(inplace=True)

codes.to_excel("codes.xlsx")
