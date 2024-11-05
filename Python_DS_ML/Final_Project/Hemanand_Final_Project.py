"""IMPORTING LIBRARY"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import plotly.express as px

"""DATA VALIDATION"""
data = pd.read_csv('https://raw.githubusercontent.com/amankharwal/Website-data/master/TravelInsurancePrediction.csv')
df = pd.DataFrame(data)
print(df.head())
print('/n')
print(df.isnull().sum())
print('/n')
print(df.info())
print('/n')
print(df.describe())

"""CONVERT OBJECT TO INTEGER"""

a = LabelEncoder()
df['Employment Type'] = a.fit_transform(df['Employment Type'])
# print(df['Employment Type'])
df['GraduateOrNot'] = a.fit_transform(df['GraduateOrNot'])
# print(df['GraduateOrNot'])
df['FrequentFlyer'] = a.fit_transform(df['FrequentFlyer'])
# print(df['FrequentFlyer'])
df['EverTravelledAbroad'] = a.fit_transform(df['EverTravelledAbroad'])
# print(df['EverTravelledAbroad'])

"""INFORMATION OF THE DATA """
print(df.info())
print('/n')

"""DATA VISUVALIZATION"""
figure = px.histogram(df, x = "Age",
                      color = "TravelInsurance",
                      title= "Factors Affecting Purchase of Travel Insurance: Age")
figure.show()

figure = px.histogram(data, x = "Employment Type",
                      color = "TravelInsurance",
                      title= "Factors Affecting Purchase of Travel Insurance: Employment Type")
figure.show()

figure = px.histogram(data, x = "AnnualIncome",
                      color = "TravelInsurance",
                      title= "Factors Affecting Purchase of Travel Insurance: Income")
figure.show()

"""FINAL DATASET"""
x = np.array(df[["Age","Employment Type","GraduateOrNot","AnnualIncome","ChronicDiseases","FrequentFlyer","EverTravelledAbroad"]])
y = np.array(df["TravelInsurance"])

"""TRAIN AND TEST THE MODEL"""
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print(x_test)
print('/n')
print(x_train)
print('/n')
print(y_test)
print('/n')
print(y_train)

"""IMPLEMENTING LOGICAL REGRESSION MODEL"""
clf = LogisticRegression(random_state=0)
clf.fit(x_train, y_train)

"""PREDICTION AND OUTCOME"""

Y_Prediction = clf.predict(x_test)
print(Y_Prediction)
Accuracy = accuracy_score(y_test,Y_Prediction)
print("Logistic Regression model accuracy (in %):", Accuracy*100)
