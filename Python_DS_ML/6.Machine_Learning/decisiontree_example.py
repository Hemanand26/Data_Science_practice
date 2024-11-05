from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

housing_data = pd.read_csv("housing.csv")
# print(housing_data.head(10))
""" Below two line of code is for regression  """
x = housing_data.drop("median_house_value",axis = 1)
y_regression = housing_data['median_house_value']/100000

LE = LabelEncoder()
x['ocean_proximity'] = LE.fit_transform(x[['ocean_proximity']])
x = x.fillna(x['ocean_proximity'].mean())

x_train,x_test,y_train,y_test = train_test_split(x,y_regression,test_size = 0.2, random_state = 42)

regressor = DecisionTreeRegressor()
regressor.fit(x_train,y_train)
y_predictor = regressor.predict(x_test)
# print(y_predictor)

mse = mean_squared_error(y_test,y_predictor)
# print(mse)

# print("++++++++++++++++++++++++++++++++++++")
# print(x)
# print(y_regression)
"""Below lines is to convert actual input of regression into classification"""
bins = [0,2,4,6,np.inf]
labels = [1,2,3,4]

y_classification = pd.cut(y_regression,bins=bins,labels=labels)

x_train,x_test,y_train,y_test = train_test_split(x,y_classification,test_size = 0.2, random_state = 42)

classifier = DecisionTreeClassifier()
classifier.fit(x_train,y_train)
y_predictor1 = classifier.predict(x_test)
print(y_predictor1)

mse1 = mean_squared_error(y_test,y_predictor1)
print(mse1)
acc = accuracy_score(y_test,y_predictor1)
print(acc)

# print("Classification target value")
# print(y_classification.unique())
# print(y_classification[:15])
# print("Regression target value")
# print(y_regression[:15])


