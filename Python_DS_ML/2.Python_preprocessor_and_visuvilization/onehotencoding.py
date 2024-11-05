import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {"Degree":["Masters","PHD","Bachelor","Masters","PHD"],"Name":["Kohli","ashwin","rahul","raina","dhoni"] }

df = pd.DataFrame(data)
print(df)
print("before changing")

one_hot_encoder = OneHotEncoder(sparse_output= False)
encoded_data = one_hot_encoder.fit_transform(df[['Degree']])
print(encoded_data)

df_encoded = pd.DataFrame(encoded_data, columns= one_hot_encoder.get_feature_names_out(["Degree"]))
print(df_encoded)

final_encoded_data = pd.concat([df, df_encoded], axis=1)
print(final_encoded_data)
