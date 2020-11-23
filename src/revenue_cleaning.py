# Title: Flag on the Play revenue cleaning
# Author: Doug Hart
# Date Created: 11/23/2020
# Last Updated: 11/23/2020

import numpy as np
import pandas as pd

#data obtained from: 
#https://www.forbes.com/sites/mikeozanian/2020/05/18/the-stadium-revenue-each-nfl-team-will-lose-if-games-are-played-without-fans/?sh=6dec1c56691a

# data note: values will be given in millions of dollars after cleaning/formatting 
revenue= pd.read_csv('data/team_revenues_18.csv')

# Extracting numeric values from string descriptors
revenue['total_revenue'] = None
revenue['from_stadium'] = None
for i in range(revenue.shape[0]):
    revenue['total_revenue'][i] = float(revenue.total[i][1:4])
    
    revenue['from_stadium'][i] = float(revenue.stadium[i][1:4])

revenue.drop()
#Dropping rank from team column
for i in range(9):
    revenue.team[i] = revenue.team[i][3:]
for i in range(9,revenue.shape[0]):
    revenue.team[i] = revenue.team[i][4:]
# Dropping string versions of revenue columns now that float versions created
revenue.drop('total',axis=1, inplace = True)
revenue.drop('stadium',axis=1, inplace = True)

# To save clean version to new csv:
# revenue.to_csv('data/filename_here',index=False)

'''NEW CSV WITH CLEANED DATA IS NOW READY FOR USE'''