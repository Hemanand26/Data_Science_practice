import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = {
    'Name': ['Dhoni','Kohli','Ash','Raina'],
    'Tamil': [85,90,99,65],
    'Maths':[75,70,99,80],
    'English':[95,98,99,90] }

df = pd.DataFrame(data)
print(df)
print('\n')
Feature = ["Tamil","Maths","English"]
x = df.loc[:,Feature].values
print(x)
print('\n')
x = StandardScaler().fit_transform(x)
print(x)
print('\n')
pca = PCA(n_components=2)
pca_model = pca.fit_transform(x)

final_df = pd.DataFrame(data = pca_model, columns=["PC1","PC2"])
output = pd.concat([df[["Name"]],final_df],axis=1)
print(output)
print('\n')
print("Variance Ratio")
print('\n')
print(pca.explained_variance_ratio_)

