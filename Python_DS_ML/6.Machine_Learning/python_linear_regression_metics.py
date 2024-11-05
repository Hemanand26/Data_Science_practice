"""scikit-learn -pip install scikit-learn"""

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

# data = pd.read_csv(r"Walmart_sales.csv")
# print(data.head(5))
#
# x = data[["Temperature","Fuel_Price","CPI","Unemployment"]]
# y = data["Weekly_Sales"]
#
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
# print(x_train)
# print("-------------")
# print(x_test)
#
# model = LinearRegression() #creation of object for the model class
# model.fit(x_train,y_train)
# predictions = model.predict(x_test)
# print(predictions)

"""---------------------Example with our own data point for prediction -----------------------"""
# data = {"Year":[2020,2021,2022,2023],
#         "Tax":[100,300,490,780],
#         "House_Price":[1200,3400,5300,8000]}
# df = pd.DataFrame(data)
# print(df)
#
#
# x = df[['Year','Tax']]
# y = df["House_Price"]
#
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
# print(x_train)
# print("-------------------------")
# print(x_test)
# print("-----------y test-----------")
# print(y_test)
# """ValueError: X has 1 features, but LinearRegression is expecting 2 features as input."""
# model = LinearRegression()
# model.fit(x_train,y_train)
# prediction = model.predict([[2028,700]])
# print("-------------my_prediction------------------")
# print(prediction)
# print("------------------Co-Efficient-------------------")
# co_efficient = model.coef_
# np.set_printoptions(suppress=True,precision=10)
# print(co_efficient)
# print("-----------------Model Intercept------------------")
# # interception = model.intercept_
# # print(interception)
# print("----------------Metic: Mean Squared Error -------")
# mse = mean_squared_error(y_test,prediction)
# print(mse)

"""this code is to run the same with inbuilt y and x test"""
##data = {"Year":[2020,2021,2022,2023],
##        "Tax":[100,300,490,780],
##        "House_Price":[1200,3400,5300,8000]}
##df = pd.DataFrame(data)
### print(df)
##
##
##x = df[['Year','Tax']]
##y = df["House_Price"]
##
##x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
### print(x_train)
### print("-------------------------")
### print(x_test)
##print("-----------y test-----------")
##print(y_test)
##"""ValueError: X has 1 features, but LinearRegression is expecting 2 features as input."""
##model = LinearRegression()
##model.fit(x_train,y_train)
##prediction = model.predict(x_test)
##print("-------------my_prediction------------------")
##print(prediction)
##print("------------------Co-Efficient-------------------")
##co_efficient = model.coef_
##np.set_printoptions(suppress=True,precision=10)
### print(co_efficient)
### print("-----------------Model Intercept------------------")
### interception = model.intercept_
### print(interception)
##print("----------------Metic: Mean Squared Error -------")
### mse = mean_squared_error(y_test,prediction)
### print(mse)
##print("-----------------------r2 score-----------------")
##r2_score = r2_score(y_test, prediction)
##print(r2_score)


# ------------------------------------------------

data = {"Year":[2020,2021,2022,2023],
        "Tax":[100,300,490,780],
        "House_Price":[1200,3400,5300,8000]}
df = pd.DataFrame(data)
print(df)


x = df[['Year','Tax']]
y = df["House_Price"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print(x_train)
print("-------------------------")
print(x_test)
print("-----------y test-----------")
print(y_test)
"""ValueError: X has 1 features, but LinearRegression is expecting 2 features as input."""
model = LinearRegression()
model.fit(x_train,y_train)
prediction = model.predict([[2028,700]])
print("-------------my_prediction------------------")
print(prediction)
print("------------------Co-Efficient-------------------")
co_efficient = model.coef_
# np.set_printoptions(suppress=True,precision=10)
print(co_efficient)
print("-----------------------correlation-------------------")
correlation_output = np.corrcoef(y_test,prediction)
print(correlation_output)

