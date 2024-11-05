import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

my_data = {"Score":[10,20,30,40,50],"Average":[0.1,0.2,0.3,0.4,0.5]}
df = pd.DataFrame(my_data)
print(df)
print ("+++++++++++++++++++++++")
min_max_scalar = MinMaxScaler()
scaled_min_max = min_max_scalar.fit_transform(df)
print(scaled_min_max)
print ("+++++++++++++++++++++++")
standard_scalar = StandardScaler()
scaled_standard = standard_scalar.fit_transform(df)
print(scaled_standard)
print ("+++++++++++++++++++++++")
df_min_max_scalar = pd.DataFrame(scaled_min_max,columns= df.columns)
df_scaled_standard_scaled = pd.DataFrame(scaled_standard,columns= df.columns)

final_combined_data = pd.concat([df, df_min_max_scalar, df_scaled_standard_scaled], axis=1)
print(final_combined_data)

"""Finding Mean and Standard Deviation"""
# data_mean = df["Score"].mean()
# print(data_mean)
#
# data_mean = df["Score"].std()
# print(data_mean)
#
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.compose import ColumnTransformer
# import pandas as pd
#
# my_data = {"Score":[10,20,30,40,50],"Average":[0.1,0.2,0.3,0.4,0.5]}
# df = pd.DataFrame(my_data)
# print(df)
#
# col_transform = ColumnTransformer([("minmax",MinMaxScaler(),['Score'])],remainder= "passthrought")
#
# min_max_scalar = col_transform.fit_transform(df)
# print(type(min_max_scalar))
#
# df_min_max_scalar = pd.DataFrame(min_max_scalar,columns= df.columns)
# print(df_min_max_scalar)
#
# final_data = pd.concat([df,df_min_max_scalar],axis=1)
# print("+++++++++++++")
# print(final_data)