import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('adidas.csv')
df = pd.DataFrame(data)
print('\n')
print(df.head(5))
print('\n')
print(df.tail(5))
print('\n')
print(df.shape)
print('\n')
print(df.columns)
print('\n')
print(df.dtypes)
print('\n')
print(df.nunique())
print('\n')
print(df.describe())
print('\n')
print(df.isnull())
print('\n')
# print(df['Total Sales'])
# New = df['Total Sales'].str.split("$", n=1, expand=True)
# df['del Total sales'] = New[0]
# df['New Total Sales'] = New[1]
# df.drop(columns=["Total Sales"], inplace=True)
# df.drop(columns=['del Total sales'], inplace=True)
# print(df['New Total Sales'])
#
# df['Total Sales'] = pd.to_numeric(df['Total Sales'])
# df['Operating Margin'] = pd.to_numeric(df['Operating Margin'])

#
total_sales = df["Total Sales"].sum()
total_profit = df["Operating Profit"].sum()
avg_price = df["Price per Unit"].mean()
total_unit_sold = df["Units Sold"].sum()
print("Total Sales",total_sales)
print('\n')
print("Total Profit",total_profit)
print('\n')
print("Average Price",avg_price)
print('\n')
print("Total unit sold",total_unit_sold)

#Create a pie chart to visualize overall sales comparision

lables = ['Total Sales','Total Profit','Average_Price','Total unit sold']
values = [total_sales,total_profit,avg_price,total_unit_sold]
plt.figure(figsize=(8,8))
plt.pie(values,labels = lables,autopct = '%1.1f%%',startangle=140)
plt.title('Overall Sales Metrics')
plt.show()

profit_by_retailer = df.groupby('Retailer')['Operating Profit'].sum().sort_values()
top_retailers = profit_by_retailer.head(10)

#Create a bar chart to visualize profit by retailer
plt.figure(figsize=(10,6))
top_retailers.plot(kind = 'bar',color='skyblue')
plt.title('Profit by retailer')
plt.xlabel('Retailer')
plt.ylabel('Operating profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Sales trend overtime
# Step 1: Convert 'Invoice Date' to datetime, handling errors
df['Invoice Date'] = pd.to_datetime(df['Invoice Date'], errors='coerce')

# Step 2: Drop rows with invalid 'Invoice Date' values
df = df.dropna(subset=['Invoice Date'])

# Step 3: Resample and sum 'Total Sales' by month
monthly_sales = df.resample('ME', on='Invoice Date')['Total Sales'].sum()
#create a line chart to visualize sales trend overtime
plt.figure(figsize=(12,6))
monthly_sales.plot(kind='line',marker='o',color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid()
plt.show()


#Product category sales distribution
category_sales = df.groupby('Product')['Total Sales'].sum().sort_values()
#Create a bar chart to visulize product category sales distribution
plt.figure(figsize=(10,6))
category_sales.plot(kind='bar',color ='purple')
plt.title('Product Category Sales Distribution')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Units sold by product category and gender type:
unit_sold_by_gender = df.groupby(['Product', 'Gender type'])['Units Sold'].sum()
plt.figure(figsize=(10,6))
unit_sold_by_gender.plot(kind='bar',stacked=True)
plt.xlabel('Product')
plt.ylabel('Total unit sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Regional Sales analysis
region_sales = df.groupby(['Region', 'State', 'City'])['Total Sales'].sum().reset_index()
top_city_profit = region_sales.sort_values('Total Sales', ascending=False)
#create a bar chart
plt.figure(figsize=(10,6))
plt.bar(top_city_profit['City'],top_city_profit['Total Sales'],color='Blue')
plt.title('Top Performing Cities by profit Top(5)')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Sales trend over time
yearly_sales = df.resample('YE',on='Invoice Date')['Total Sales'].sum()
#Create a line chart
plt.figure(figsize=(12,6))
yearly_sales.plot(kind='line',marker='o',color='blue')
plt.title('Yearly Sales Trend')
plt.xlabel('Year')
plt.ylabel('Total sales')
plt.grid()
plt.show()