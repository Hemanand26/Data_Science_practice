# import pandas as pd
#
# data = {"festival_data": ["2024-01-01","2024-02-19","2024-03-24"],
#         "festival_time": ["2024-01-01 09:00:00","2024-02-19 12:30:00","2024-03-19 13:30:00"]
#         }
#
# df = pd.DataFrame(data)
# print(df)
#
# df["festival_data"] = pd.to_datetime(df["festival_data"])
# df["festival_time"] = pd.to_datetime(df["festival_time"])
#
# df["day_of_week"]= df["festival_data"].dt.dayofweek
# print(df["day_of_week"])
#
# df["month"] = df["festival_data"].dt.month
# print(df["month"])
#
# df["quarter"] = df["festival_data"].dt.quarter
# print(df["quarter"])
#
# df["day_of_month"] = df["festival_data"].dt.day
# print(df["quarter"])

""" Dimensionality Reduction  """
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")

df = df.drop(columns= ["PassengerId","Name","Ticket","Cabin"])
print(df.head())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print(df)

df = pd.get_dummies(df,columns= ["Sex","Embarked"], drop_first= True)
print(df)
#
# x = df.drop(columns= ["Survived"])
# y = df["Survived"]
#
# scaler = StandardScaler()
# x_scaled = scaler.fit_transform(x)
#
# pca = PCA(n_components= 2)
# x_pca = pca.fit_transform(x_scaled)
#
# pricipal_component = pca.components_
# print("_____________________________")
# print(pricipal_component)
# print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
#
# plt.figure(figsize= (10,7))
# sns.scatterplot(x = x_pca[:,0],y = x_pca[:,1],hue= y, palette= "viridis")
# plt.legend("Survived")
# plt.show()

# import pandas as pd
# import numpy as np
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df = pd.read_csv("train.csv")
#
# df = df.drop(columns= ["PassengerId","Name","Ticket","Cabin"])
# print(df.head())
#
# df["Age"] = df["Age"].fillna(df["Age"].median())
# df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode() [0] )
#
# print(df)
#
# df = pd.get_dummies(df,columns= ["Sex","Embarked"], drop_first= True)
# print(df)
#
# x = df.drop(columns= ["Survived"])
# y = df["Survived"]
#
# scaler = StandardScaler()
# x_scaled = scaler.fit_transform(x)
#
# cov_matrix = np.cov(x_scaled.T)
# print(cov_matrix)
# print("***************************")
# eigen_values , eigen_vector = np.linalg.eig(cov_matrix)
# print(eigen_values)
#
# sorted_indices = np.argsort(eigen_vector)[::-1]
# sorted_eigen_values = eigen_values(sorted_indices)
# sorted_eigen_vector = eigen_vector(:,sorted_indices)
#
# n_componenets = 2
# top_eigenvectors = sorted_eigen_vector[:,:n_componenets]
#
#
# x_pca = pca.fit_transform(x_scaled)
#
# plt.figure(figsize= (10,7))
# sns.scatterplot(x = x_pca[:,0],y = x_pca[:,1],hue= y, palette= "viridis")
# plt.legend("Survived")
# plt.show()



