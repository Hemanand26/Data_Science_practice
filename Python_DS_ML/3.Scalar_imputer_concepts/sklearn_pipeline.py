import pandas as pd
import numpy as np

data = pd.read_csv("train.csv")
print(data.head())
print(type(data))
my_df = data.copy()  #shallow copy
nan_data = my_df.isnull().sum()
print(nan_data)
"""simple imputer is the library of sklearn used to fill the nan data in the interger column"""
print("After imputer")

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
"""default value that gets filled in the empty row is "MEAN" OF THE ACTUAL COLUMN"""

imputer = SimpleImputer(strategy='mean')
data[["Age"]] = imputer.fit_transform(data[["Age"]])
print(data.isnull().sum())
print(data)

""" How to apply for two columns """

imputer = SimpleImputer(strategy='mean')
data[["Age"]] = imputer.fit_transform(data[["Age"]])
print(data.isnull().sum())
print(data)

data1 = ["Age","Cabin"]
imputer.fit(data[data1])
imputer_values = imputer.transform(data[data1])
data[data1] = imputer_values
print(imputer_values)

a= LabelEncoder()
data["new_cab"] = a.fit_transform(data[["Cabin"]])






