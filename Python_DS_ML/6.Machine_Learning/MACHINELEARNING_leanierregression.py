import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("Walmart_sales.csv")
print(df.head())

x = df[["Temperature","Fuel_Price","CPI","Unemployment"]]
y = df["Weekly_Sales"]

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

linear_model = LinearRegression()
linear_model.fit(x_train,y_train)

y_prediction = linear_model.predict(x_test)
print(y_prediction)

mean_squared_error_check = mean_squared_error(y_test,y_prediction)
print(mean_squared_error_check)

r2_score_check = r2_score(y_test,y_prediction)
print(r2_score_check)

# "Mean"
#
# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.model_selection import train_test_split
#
# data = {
#     'Temperature': [60,70,80,90,100],
#     'Fuel_Price': [3.5,3.7,3.6,3.8,4.0],
#     'CPI': [220, 221, 222, 223, 224],
#     'Unemployment': [20000,21000,22000,23000,24000]
# }
#
# df = pd.DataFrame(data)
#
# x = df[["Temperature","Fuel_Price","CPI","Unemployment"]]
# y = df["Weekly_Sales"]
#
# print(x)
# print(y)
#
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
#
# linear_model = LinearRegression()
# linear_model.fit(x_train,y_train)
#
# y_prediction = linear_model.predict(x_test)
# print(y_prediction)
#
# mean_squared_error_check = mean_squared_error(y_test,y_prediction)
# print(mean_squared_error_check)
#
# df_new = pd.DataFrame(x_test)
# df_new["Actual"] = y_test.values
# df_new["Predicted"] = y_prediction
# df_new["Squared_Error"] = (df_new["Actual"] - df_new["Predicted"]) ** 2
# df_new["Error"] = df_new["Actual"] - df_new["Predicted"]
# print(mean_squared_error_check)
# print(df_new)
# print("+++++++++++++++++++++++++++++++++")
# print(df_new["Actual"],df_new["Predicted"])
