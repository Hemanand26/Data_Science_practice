import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

data = pd.read_csv('apple_data.csv', parse_dates=['Date'])
print(data)

stationary_data_check = adfuller(data['Date'])
print(stationary_data_check[0])
print(stationary_data_check[1])

p=5 # p is auto reggressive order
d=1 # d is differiencial order
q=0 # q is moving order
model = ARIMA(data,order=(p,d,q))
modelFit = model.fit()
final_data = modelFit.forecast(steps=10)