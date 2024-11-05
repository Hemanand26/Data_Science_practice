import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv("cars.csv")
print(df.head())
print("++++++++++++++++++++++++++++")
LE = LabelEncoder()

df["Transmission"] = LE.fit_transform(df['Transmission'])
x = df[["Kilometers_Driven","Transmission","Mileage","Power","Engine"]]
y = df["Price"]

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

linear_model = LinearRegression()
linear_model.fit(x_train,y_train)


print('+++++++++++++++++++++++++++')
print("X-Train")
print(x_train)
print('+++++++++++++++++++++++++++')
print("X-Test")
print(x_test)
print('+++++++++++++++++++++++++++')
print("Y-Train")
print(y_train)
print('+++++++++++++++++++++++++++')
print("Y-Test")
print(y_test)
print('+++++++++++++++++++++++++++')


y_prediction = linear_model.predict(x_test)
print('Y_PREDICTION')
my_data = pd.DataFrame(y_prediction)
print(my_data)
print('+++++++++++++++++++++++++++')
mean_squared_error_check = mean_squared_error(y_test,y_prediction)
print(mean_squared_error_check)
print('+++++++++++++++++++++++++++')
r2_score_check = r2_score(y_test,y_prediction)
print(r2_score_check)
print('+++++++++++++++++++++++++++')

# df['Mileage'] = df['Mileage'].replace({'mi.':''},regex=True) ---> use to  replace particular thing in a charter

# y_prediction = linear_model.predict(my_df)
# print(y_prediction)
#
# my_df["price"] = y_prediction
# print(my_df)
# selected_column=df[["area","bedroom","age","price"]]
# print(selected_column)
# my_df=pd.concat([selected_column,my_df])
# my_df.to_csv("final_price.csv")

# for col in ["Kilometers_Driven","Mileage","Power","Engine"]:
#            a = LabelEncoder()
#           df[col] = a.fit_transform(df[col])


