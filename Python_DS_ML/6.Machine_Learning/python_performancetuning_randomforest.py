from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder

model = RandomForestClassifier()
housing_data = pd.read_csv("housing.csv")
print(housing_data.head(10))

LE =LabelEncoder()
housing_data['ocean_proximity'] = LE.fit_transform(housing_data['ocean_proximity'])

""" Below two line of code is for regression  """
x = housing_data.drop("median_house_value",axis = 1)
y_regression = housing_data['median_house_value']

x_train,x_test,y_train,y_test = train_test_split(x,y_regression,test_size = 0.2, random_state = 42)

random_forest_regressor = RandomForestRegressor(n_estimators=100, random_state= 42)
random_forest_regressor.fit(x_train,y_train)
prediction = random_forest_regressor.predict(x_test)
print(prediction)

