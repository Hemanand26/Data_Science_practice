from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import warnings


x_train, x_test, y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state=42)
print(x_train)
print("--------------")
print(x_test)
print("---------------")
print(y_test)

model = LinearRegression()
model.fit(x_train,y_train)
prediction = model.predict([[2028,700]])
print("---------------my_prediction____________")
print(prediction)
print("------------Co_effiecient_______________")
co_efficient = model.coef_
print(co_efficient)
print("---------------------------")
