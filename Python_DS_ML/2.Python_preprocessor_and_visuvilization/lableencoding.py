import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

data = {"Team":["CSK","RR","RCB","KKR","LSG","DC","PBKS","MI"]}
df= pd.DataFrame(data)
print(df)
print("--------------------------")


a = LabelEncoder()
df ["new _Team"] = a.fit_transform(df["Team"])
print(df)
print("--------------------------")


# df ["new _Team"] = df["Team"].map({"CSK":7,"MI":99,"RR":90,"LSG":5,"KKR":6,"PBKS":9,"GT":44})
# print(df)
# df.fillna(100, inplace = True)
# print(df)
#
data = {"Degree":["Masters","PHD","Bachelor","Masters","PHD"],"Name":["Kohli","ashwin","rahul","raina","dhoni"] }
df =pd.DataFrame(data)
print(df)
print("---------------------------------------------")
#
encoded_df = pd.get_dummies(df["Degree"],prefix="changed_")
print(encoded_df)
print("after concatation")
print("---------------------------------------------")
final_df = pd.concat([df, encoded_df],axis=1)
print(final_df)