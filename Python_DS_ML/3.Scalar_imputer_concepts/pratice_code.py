import pandas as pd
# import numpy as np

data = pd.read_csv("train.csv")
print(data.head())
print(type(data))
my_df = data.copy()  #shallow copy
nan_data = my_df.isnull().sum()
print(nan_data)

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

imputer = SimpleImputer(strategy='constant')
a= LabelEncoder()
data["Cabin"] = a.fit_transform(data[["Cabin"]])
print(data["Cabin"])
data[["Age","Cabin"]] = imputer.fit_transform(data[["Age","Cabin"]])
print(data.isnull().sum())
print(data)

