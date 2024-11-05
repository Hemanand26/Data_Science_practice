import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from statsmodels.tsa.arima.model import ARIMA

data = {
    'Date': ['2024-01-03','2024-01-01','2024-01-02'],
    'Open': [183.25, 182.71,182.92],
    'High': [184.73, 183.24, 183.74],
    'Low': [182.62, 180.63, 181.21],
    'Close':[184.02,182.01,182.47],
    'Volume':[25871300,33556700,28907300]
}
# creating a dataframe
df = pd.DataFrame(data)
# Parsing the 'Date' column as datetime and setting it as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace= True)
print(df)
print("after sorting")
# Sorting the Dataframe by its index to ensure the DatetimeIndex is monotonic
df = df.sort_index()
print(df)

#Now,you can perform slicing operations
#Example: Slicing data for the date range '2024-01-01' to '2024-01-02'
subset = df['2024-01-01':'2024-01-02']
print(subset)

