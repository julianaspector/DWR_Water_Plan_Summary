# import necessary library
import pandas as pd

# make this data available in same directory as script
data = pd.read_csv('Cleaned_Data_based_on_2018_Update.csv', usecols=range(1,12))
pa_region_lookup = pd.read_csv('PA_Region_Lookup_Table.csv', usecols=range(1,3))
sj_river_data = pd.read_csv('San_Joaquin_River_Donut.csv', skiprows=3, nrows=16, usecols=[1,10,11,12,13,14,15,16,17,18,19,20])
tulare_data = pd.read_csv('Tulare_Lake_Donut.csv', skiprows=3,nrows=16, usecols=[1,10,11,12,13,14,15,16,17,18,19,20])

sj_river_data_type = sj_river_data[sj_river_data['Type'].isin(['Urban', 'Irrigated Agriculture', 
                                                               'Managed Wetlands'])]
sj_river_data_type = sj_river_data_type.assign(mean=sj_river_data_type.mean(axis=1))

tulare_data_type = tulare_data[tulare_data['Type'].isin(['Urban', 'Irrigated Agriculture', 
                                                               'Managed Wetlands'])]
tulare_data_type = tulare_data_type.assign(mean=tulare_data_type.mean(axis=1))

cols = list(data.columns.values)

# select relevant columns
cols = cols[0:1] + cols[6:9] + cols[2:6] + cols[9:11]

# replace "." with " " in both datasets
data.columns = data.columns.str.replace(".", " ")
pa_region_lookup.columns=pa_region_lookup.columns.str.replace(".", " ")

# filter data for PA's 603 and 604
grouped_2005_2015 = round(data[data['PA #'].isin(['602','603', '604'])].groupby(['PA #']).mean(),1)
table_2005_2015 = grouped_2005_2015
table_2005_2015 = table_2005_2015.drop(columns=['Year'])
table_2005_2015['Total Supply'] = table_2005_2015['Total Supply AG (includes Reuse)'] + table_2005_2015['Total Supply Urban (includes Reuse)'] + table_2005_2015['Total Supply MW (includes Reuse)']

cols_final = list(table_2005_2015.columns.values)
cols_final = cols_final[0:3] + cols_final[7:8] + cols_final[3:7] + cols_final[8:]
table_2005_2015 = table_2005_2015[cols_final]

table_2005_2015 = table_2005_2015.drop(columns=['Total GW AG', 'Total GW Urban', 'Total GW MW', 'Total GW Use'])

table_2005_2015.loc["Total"] = table_2005_2015.sum()

table_2005_2015 = table_2005_2015.rename(columns={"Total Supply AG (includes Reuse)" : "Total Supply AG",
                                                 "Total Supply Urban (includes Reuse)" : "Total Supply Urban",
                                        "Total Supply MW (includes Reuse)" : "Total Supply MW"})

urban = sj_river_data_type['mean'].iloc[0] + tulare_data_type['mean'].iloc[0]-table_2005_2015['Total Supply Urban'].iloc[3]

ag = sj_river_data_type['mean'].iloc[1] + tulare_data_type['mean'].iloc[1]-table_2005_2015['Total Supply AG'].iloc[3]

mw = sj_river_data_type['mean'].iloc[2] + tulare_data_type['mean'].iloc[2]-table_2005_2015['Total Supply MW'].iloc[3]

total = sum(sj_river_data_type['mean']) + sum(tulare_data_type['mean'])-table_2005_2015['Total Supply'].iloc[3]

d = {'Total': [ag, urban, mw, total]}
index = ['Agriculture', 'Municipal', 'Wetland/Refuge', 'All Sectors']
table = pd.DataFrame(data=d, index=index)
index = table.index
index.name = "Sector"

print(round(table['Total'],1))