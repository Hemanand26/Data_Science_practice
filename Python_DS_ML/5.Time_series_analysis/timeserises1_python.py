import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

data = pd.read_csv('apple_data.csv', parse_dates=['Date'],index_col='Date')
print(data)
# data = pd.to_datetime(data.index)
"""
Parse data

Point 1: This is to let python know which column to pick as data time columns. If not we may have to do the conversion manually
from string to date time

Point 2: Conversation during the parse_dates is more efficient and time saving process

Point 3: This will lead to better usage various pandas based data time functions

index_col
"""
"Below code picks the location of the particular data 02-08-2020 from the given dataset"
row = data.loc['02/25/2020']r
print(row)

" Below code is kind of slicing that picks the date between these start and end range "
data = data.sort_index()
subset = data['01-03-2020':'01-28-2020']
print(subset)

"Below code is to print only the row data from the given data set"
print(data.columns)
print(data)

""
data.reset_index(inplace= True)
print(data.columns)
print('-------------------------')

"Below code is to print only the row data from the given data set"
print(data.index)

" Visualization to see the data in the form of graph "
# plt.figure(figsize= (10,8))
# for column in data.columns:
#     plt.plot(data.index, data[column], labels=column)
#
# plt.title('Time series Data')
# plt.xlabel('Date')
# plt.ylabel('Value')
# plt.show()

"above plot will through an error because we were using all the column to plot and some column has non number data"
data[" Close/Last"] = data[" Close/Last"].str.replace("$","").astype(float)
plt.figure(figsize=(10,8))
plt.plot(data[" Close/Last"])

plt.title('Time series analysis')
plt.xlabel('Data')
plt.ylabel('Value')
plt.show()


