# Importing Libraries
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt  

# Reading the data
json_file = open('loan_data_json.json')
data = json.load(json_file)

# Transform to DataFrame
loandata = pd.DataFrame(data)

# Finding the unique values for the purpose column
loandata['purpose'].unique()

# Descriping the data for some specific columns
loandata['int.rate'].describe
loandata['fico'].describe
loandata['dti'].describe

# using exp() to get the annual income
annual_income = np.exp(loandata['log.annual.inc'])
loandata.insert(4, 'annual_income', annual_income)

# Fico score
# fico >= 300 and < 400:'Very Poor'
# fico >= 400 and ficoscore < 600:'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 700:'Good'
# fico >=700:'Excellent'

# Using for loops to categorize fico
length = len(loandata['fico'])
ficocat = []
for x in range(0, length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >= 700:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
loandata.insert(8, 'fico_category', ficocat)

# df.loc as conditional statements
# df.loc[df[column_name] condition, newcolumn_name] = 'value if the condition is met'

# for interest rates, a new column is wanted, rate > 0.12 then high, else: low
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

# number of loans/rows by fico.category
catplot = loandata.groupby(['fico_category']).size()
catplot.plot.bar(color = 'green', width = 0.3)
plt.show

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.5)
plt.show

# Scatter plots
xpoint = loandata['annual_income']
ypoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

# Export into CSV file
loandata.to_csv('loan_cleaned.csv', index= True)













