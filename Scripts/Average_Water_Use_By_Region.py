# import necessary library
import pandas as pd

# make this data available in same directory as script
data = pd.read_csv('Cleaned_Data_based_on_2018_Update.csv', usecols=range(1,12))
pa_region_lookup = pd.read_csv('PA_Region_Lookup_Table.csv', usecols=range(1,3))

cols = list(data.columns.values)

# select relevant columns
cols = cols[0:1] + cols[6:9] + cols[2:6] + cols[9:11]
data = data[cols]

# replace "." with " " in both datasets
data.columns = data.columns.str.replace(".", " ")
pa_region_lookup.columns=pa_region_lookup.columns.str.replace(".", " ")

# group data by desired years
grouped_2005_2010 = round(data[data['Year'].isin(['2005', '2006', '2007', '2008', '2009', '2010'])].groupby(['PA #']).mean(),1)

# Set planning area as index and group data by staff report region
table_2005_2010 = grouped_2005_2010.join(pa_region_lookup.set_index('PA #'), on='PA #')
table_2005_2010 = table_2005_2010.drop(columns=['Year'])
table_2005_2010 = table_2005_2010.groupby(['Region']).sum().reindex(["Sacramento River Region",
             "Delta Region",
             "Delta Eastside Tributaries",
              "San Joaquin Valley",
              "San Francisco Bay Area",
              "Central Coast",
              "Southern California"])

# calculations
table_2005_2010['Total Supply'] = table_2005_2010['Total Supply AG (includes Reuse)'] + table_2005_2010['Total Supply Urban (includes Reuse)'] + table_2005_2010['Total Supply MW (includes Reuse)']
table_2005_2010['Total Non-GW AG'] = table_2005_2010['Total Supply AG (includes Reuse)'] - table_2005_2010['Total GW AG']
table_2005_2010['Total Non-GW Urban'] = table_2005_2010['Total Supply Urban (includes Reuse)'] - table_2005_2010['Total GW Urban']
table_2005_2010['Total Non-GW MW'] = table_2005_2010['Total Supply MW (includes Reuse)'] - table_2005_2010['Total GW MW']
table_2005_2010['Total Non-GW Supply'] = table_2005_2010['Total Supply'] - table_2005_2010['Total GW Use']

# form final table
cols_final = list(table_2005_2010.columns.values)
cols_final = cols_final[0:3] + cols_final[7:8] + cols_final[3:7] + cols_final[8:]
table_2005_2010 = table_2005_2010[cols_final]

# same process as above for different years averaged
grouped_2005_2015 = round(data.groupby(['PA #']).mean(),1)
table_2005_2015 = grouped_2005_2015.join(pa_region_lookup.set_index('PA #'), on='PA #')
table_2005_2015 = table_2005_2015.drop(columns=['Year'])
table_2005_2015 = table_2005_2015.groupby(['Region']).sum().reindex(["Sacramento River Region",
             "Delta Region",
             "Delta Eastside Tributaries",
              "San Joaquin Valley",
              "San Francisco Bay Area",
              "Central Coast",
              "Southern California"])

table_2005_2015['Total Supply'] = table_2005_2015['Total Supply AG (includes Reuse)'] + table_2005_2015['Total Supply Urban (includes Reuse)'] + table_2005_2015['Total Supply MW (includes Reuse)']
table_2005_2015['Total Non-GW AG'] = table_2005_2015['Total Supply AG (includes Reuse)'] - table_2005_2015['Total GW AG']
table_2005_2015['Total Non-GW Urban'] = table_2005_2015['Total Supply Urban (includes Reuse)'] - table_2005_2015['Total GW Urban']
table_2005_2015['Total Non-GW MW'] = table_2005_2015['Total Supply MW (includes Reuse)'] - table_2005_2015['Total GW MW']
table_2005_2015['Total Non-GW Supply'] = table_2005_2015['Total Supply'] - table_2005_2015['Total GW Use']

cols_final = list(table_2005_2015.columns.values)
cols_final = cols_final[0:3] + cols_final[7:8] + cols_final[3:7] + cols_final[8:]
table_2005_2015 = table_2005_2015[cols_final]

# same process as above for 2014
grouped_2014 = round(data[data['Year'].isin(['2014'])].groupby(['PA #']).mean(),1)
table_2014 = grouped_2014.join(pa_region_lookup.set_index('PA #'), on='PA #')
table_2014 = table_2014.drop(columns=['Year'])
table_2014 = table_2014.groupby(['Region']).sum().reindex(["Sacramento River Region",
             "Delta Region",
             "Delta Eastside Tributaries",
              "San Joaquin Valley",
              "San Francisco Bay Area",
              "Central Coast",
              "Southern California"])

table_2014['Total Supply'] = table_2014['Total Supply AG (includes Reuse)'] + table_2014['Total Supply Urban (includes Reuse)'] + table_2014['Total Supply MW (includes Reuse)']
table_2014['Total Non-GW AG'] = table_2014['Total Supply AG (includes Reuse)'] - table_2014['Total GW AG']
table_2014['Total Non-GW Urban'] = table_2014['Total Supply Urban (includes Reuse)'] - table_2014['Total GW Urban']
table_2014['Total Non-GW MW'] = table_2014['Total Supply MW (includes Reuse)'] - table_2014['Total GW MW']
table_2014['Total Non-GW Supply'] = table_2014['Total Supply'] - table_2014['Total GW Use']

cols_final = list(table_2014.columns.values)
cols_final = cols_final[0:3] + cols_final[7:8] + cols_final[3:7] + cols_final[8:]
table_2014 = table_2014[cols_final]

# same prcess as above for 2015
grouped_2015 = round(data[data['Year'].isin(['2015'])].groupby(['PA #']).mean(),1)
table_2015 = grouped_2015.join(pa_region_lookup.set_index('PA #'), on='PA #')
table_2015 = table_2015.drop(columns=['Year'])
table_2015 = table_2015.groupby(['Region']).sum().reindex(["Sacramento River Region",
             "Delta Region",
             "Delta Eastside Tributaries",
              "San Joaquin Valley",
              "San Francisco Bay Area",
              "Central Coast",
              "Southern California"])

table_2015['Total Supply'] = table_2015['Total Supply AG (includes Reuse)'] + table_2015['Total Supply Urban (includes Reuse)'] + table_2015['Total Supply MW (includes Reuse)']
table_2015['Total Non-GW AG'] = table_2015['Total Supply AG (includes Reuse)'] - table_2015['Total GW AG']
table_2015['Total Non-GW Urban'] = table_2015['Total Supply Urban (includes Reuse)'] - table_2015['Total GW Urban']
table_2015['Total Non-GW MW'] = table_2015['Total Supply MW (includes Reuse)'] - table_2015['Total GW MW']
table_2015['Total Non-GW Supply'] = table_2015['Total Supply'] - table_2015['Total GW Use']

cols_final = list(table_2015.columns.values)
cols_final = cols_final[0:3] + cols_final[7:8] + cols_final[3:7] + cols_final[8:]
table_2015 = table_2015[cols_final]

# write tables to excel file (edit desired path for writing file)
with pd.ExcelWriter('PUT DESIRED PATH HERE INCLUDING FILE NAME') as writer:
    table_2005_2015.to_excel(writer, sheet_name='2005_2015')
    table_2005_2010.to_excel(writer, sheet_name='2005_2010')
    table_2014.to_excel(writer, sheet_name='2014')
    table_2015.to_excel(writer, sheet_name = '2015')
