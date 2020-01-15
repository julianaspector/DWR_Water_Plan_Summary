library(openxlsx)
library(dplyr)

setwd('S:/DWR/VOL1/BayDeltaDRV/Public Trust Unit/Work Projects/P2_General/California Water Plan Statistics')


data <- NULL

for (i in 11:21){
  data <- bind_rows(data, read.xlsx(xlsxFile='2002-2015_GW_CO_PA_SUMMARY_10-02-18_ver4.xlsx',
                                    sheet=i,
                                    rows=1:57,
                                    cols = 19:27))
}

data$Year <- NULL

data$Year <- c(rep("2005",56),
               rep("2006", 56),
               rep("2007", 56),
               rep("2008", 56),
               rep("2009", 56),
               rep("2010", 56),
               rep("2011", 56),
               rep("2012", 56),
               rep("2013", 56),
               rep("2014", 56),
               rep("2015", 56))


for (j in 501:509){
  data[data$`PA.#` == j , 11] <- 'Sacramento River Region'
}

for (j in 511){
  data[data$`PA.#` == j , 11] <- 'Sacramento River Region'
}

for (j in 603:604){
  data[data$`PA.#` == j , 11] <- 'Delta Eastside Tributaries'
}

for (j in c(510, 602)){
  data[data$`PA.#` == j , 11] <- 'Delta Region'
}

for (j in 201:202){
  data[data$`PA.#` == j , 11] <- 'San Francisco Bay Area'
}

for (j in 301:302){
  data[data$`PA.#` == j , 11] <- 'Central Coast'
}

for (j in c(601, 605, 606, 607, 608, 609, 610)){
  data[data$`PA.#` == j , 11] <- 'San Joaquin Valley'
}

for (j in 701:710){
  data[data$`PA.#` == j , 11] <- 'San Joaquin Valley'
}

for (j in c(401, 402, 403, 404, 901, 902, 903, 904, 905, 1001, 1002, 1003, 1004, 1005, 1006)){
  data[data$`PA.#` == j , 11] <- 'Southern California'
}

data <- data %>% rename(Region=V11)

region_lo <- data %>% select('PA.#', 'Region')

region_lo <- unique(region_lo)

write.csv(region_lo, 'PA_Region_Lookup_Table.csv')

write.csv(data, 'Cleaned_Data.csv')