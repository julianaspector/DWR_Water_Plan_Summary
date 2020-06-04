# import necessary libraries
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:.0f}'.format 
# display numbers as integers

# import data
data = pd.read_csv('Data_Regional_Exports_Imports_20200415.csv', skiprows=2,
                  usecols=[0,3,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26],
                  nrows=45, index_col=1)

# only include relevant rows to Sac/Delta supplies
relevant_data = data[(data.Include=='Yes')]

entering = relevant_data.groupby('Hydrologic Region').sum()

leaving = relevant_data.groupby('Leaving').sum()

balance = entering-leaving
balance = balance.round(decimals=0)
balance = balance.drop(['Sacramento River Region'])

balance = balance.assign(mean=balance.mean(axis=1))

balance_2005_2015 = balance.iloc[:, [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
balance_2005_2015 = balance_2005_2015.assign(mean=balance_2005_2015.mean(axis=1))


with pd.ExcelWriter('PUT DESIRED PATH HERE INCLUDING FILE NAME') as writer:
    balance.to_excel(writer, sheet_name='All Years')
    balance_2005_2015.to_excel(writer, sheet_name='2005_2015')
