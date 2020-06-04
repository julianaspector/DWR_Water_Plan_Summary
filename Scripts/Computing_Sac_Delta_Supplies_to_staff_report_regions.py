# import necessary libraries
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:.0f}'.format # display numbers as integers

# import data and lookup table for planning areas/regions
data = pd.read_csv('Data_Regional_Exports_Imports_20200415.csv', skiprows=2,
                  usecols=[2,5,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26],
                  nrows=46)
pa_region_lookup = pd.read_csv('PA_Region_Lookup_Table.csv', usecols=range(1,4))

# filter data for Sac/Delta supplies only
relevant_data = data[(data.Include=='Yes')]

# determine water supplies entering regions
entering = relevant_data.groupby('PA Entering').sum()
entering = entering.drop(['PA Leaving'], axis=1)
entering = entering.join(pa_region_lookup.set_index('PA Entering'), on='PA Entering')
entering = entering.drop(['PA Leaving'], axis=1)
entering = entering.groupby(['Region']).sum().reindex(["Sacramento River Region",
             "Delta Region",
             "Delta Eastside Tributaries",
              "San Joaquin Valley",
              "San Francisco Bay Area",
              "Central Coast",
              "Southern California"])

entering = entering.fillna(value=0)

# determine water supplies leaving regions
leaving = relevant_data.groupby('PA Leaving').sum()
leaving = leaving.drop(['PA Entering'], axis=1)
leaving = leaving.join(pa_region_lookup.set_index('PA Leaving'), on='PA Leaving')
leaving = leaving.drop(['PA Entering'], axis=1)
leaving = leaving.groupby(['Region']).sum().reindex(["Sacramento River Region",
             "Delta Region",
             "Delta Eastside Tributaries",
              "San Joaquin Valley",
              "San Francisco Bay Area",
              "Central Coast",
              "Southern California"])

leaving = leaving.fillna(value=0)

# computer balance
balance = entering-leaving
balance = balance.round(decimals=0)

# compute mean
balance = balance.assign(mean=balance.mean(axis=1))

# balances for just 2005-2015
balance_2005_2015 = balance.iloc[:, [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]


balance_2005_2015 = balance_2005_2015.assign(mean=balance_2005_2015.mean(axis=1))

# write results
with pd.ExcelWriter('PUT DESIRED PATH HERE INCLUDING FILE NAME') as writer:
    balance.to_excel(writer, sheet_name='All Years')
    balance_2005_2015.to_excel(writer, sheet_name='2005_2015')
