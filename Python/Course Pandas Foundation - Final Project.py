#Final Project - Analyzing Sales Data
###Date: 30 December 2021

###Author: Keereerat

###Course: Pandas Foundation

# import data
import pandas as pd
import numpy as np
df = pd.read_csv("https://raw.githubusercontent.com/Sirrender-krr/dsb-batch10/refs/heads/main/Python/sample-store.csv")

# preview top 5 rows
df.head(10)

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# example of pd.to_datetime() function
pd.to_datetime(df['Order Date'].head(), format='%m/%d/%Y')

# TODO - convert order date and ship date to datetime in the original dataframe
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Year'] = df['Order Date'].dt.year
df[['Ship Date','Order Date']].info()

# TODO - count nan in postal code column
pd.DataFrame([df['Postal Code'].isna().sum()], columns=["Postal Code NA"])

# TODO - filter rows with missing values
df[df['Postal Code'].isna()]

# TODO 01 - how many columns, rows in this dataset
df.shape

# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?
d = { 'col_name':df.columns,'sum_na':df.isna().sum()}
pd.DataFrame(d).reset_index(drop=True)

# TODO 03 - your friend ask for `California` data, filter it and export csv for him
California = df.query('State == "California"').sort_values('Order Date', ascending= True)
California.to_csv('California.csv',index=False)

# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
Cal_Tex_2017 = df.query('State == "California" | State == "Texas"')\
    .loc[(df['Order Date'] >= '2017-01-01')& (df['Order Date'] < '2018-01-01')]\
    .sort_values('Order Date', ascending= False)
Cal_Tex_2017.to_csv('Cal_Tex_2017.csv',index=False)

# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
df['Year'] = df['Order Date'].dt.year
df17 = df.loc[df['Year']== 2017]
df17_sum = df17.groupby('Year')['Sales'].agg(['sum','mean','std']).reset_index()
df17_sum.columns=['Year','Total Sales','Average Sales','Std']
df17_sum

# TODO 06 - which Segment has the highest profit in 2018
df18 = df[df['Year'] == 2018]
df18.groupby(['Year','Segment'])['Profit'].sum().reset_index().sort_values('Profit', ascending=False)

# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
df_fix = df[(df['Order Date'] >= '2019-04-15') & (df['Order Date'] <= '2019-12-31')]
df_fix.groupby('State')['Sales'].sum().reset_index().sort_values('Sales').head(5).reset_index(drop=True)

# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
df19 = df[df['Year'] == 2019]
total19 = df19['Sales'].sum()
df19_reg = df19.groupby('Region')['Sales'].sum().reset_index()
df19_reg = df19_reg.assign(MKT_share = df19_reg['Sales']/total19*100)
display(df19_reg)
display(df19_reg.query('Region == "West" | Region == "Central"').sum())

# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020

# Top 10 most ordered
df19_20 = df[(df['Year']==2019)|(df['Year']==2020)]
top_count = df19_20['Product Name'].value_counts().reset_index()
top_count.columns = ['Product','Order Count']
top_count = top_count.sort_values('Order Count',ascending=False).head(10)


# Top 10 most sales
top_sales = df19_20.groupby('Product Name')['Sales'].sum().reset_index()
top_sales.columns = ['Product','Total Sales']
top_sales = top_sales.sort_values('Total Sales',ascending=False).head(10).reset_index(drop=True)
top_sales = top_sales.style.format({'Total Sales':"{:,.2f}"})

# Display both
display(top_count)
display(top_sales)

# TODO 10 - plot at least 2 plots, any plot you think interesting :)
# 10.1 Sales By year
df_yearly = df.groupby('Year')['Sales'].sum()
df_yearly.plot(kind='bar',title='Yealy Sales',rot=0);

# TODO 10 - plot at least 2 plots, any plot you think interesting :)
# 10.2 Sales By Catagory Y2020
df20 = df[df['Year'] == 2020]
df20.groupby('Category')['Sales'].sum().plot.pie(y='Sales',autopct='%.2f%%',figsize=(5,5),title='Cat Mkt Share 2020');

# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions
# Created tables compare profit and loss, and top 5 profit and top 5 loss in 2020
df20 = df[df['Year'] == 2020]

# Create a Profit comparison table
profit = df20.groupby('Product Name')['Profit'].sum().reset_index()
profit.columns = ['Product','Profit']
profit['Is Profit'] = np.where(profit['Profit']>0,'gain','loss')

# Sum Profit and loss
display(profit.groupby('Is Profit')['Profit'].sum().reset_index()\
    .style.format({'Profit':"{:,.2f}"}))

# top 5 profit and top 5 loss
top5 = profit.groupby('Product')['Profit'].sum().reset_index()\
    .sort_values('Profit',ascending=False).head(5).reset_index(drop=True)\
    .style.format({'Profit':"{:,.2f}"})
bottom5 = profit.groupby('Product')['Profit'].sum().reset_index()\
    .sort_values('Profit',ascending=True).head(5).reset_index(drop=True)\
    .style.format({'Profit':"{:,.2f}"})
display(top5)
display(bottom5)
