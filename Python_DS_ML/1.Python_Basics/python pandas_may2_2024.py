import pandas as pd

var = ["a","B","C"]
print(var)
print(type(var))
my_series = pd.Series(var)
print(my_series)
print(type(my_series))
print("++++++++++++++++++++++++")

my_data = {"Name":["dhoni","rahul","dk"],"Team":["csk","lsg","rcb"]}
print(my_data)
print(type(my_data))
print(my_data)
df = pd.DataFrame(my_data)
print(df)
print(type(df))
df.to_csv("goat.csv")
print("++++++++++++++++++++++++")

my_data = pd.read_csv("goat.csv",index_col=0)
print(my_data)
my_data = pd.read_csv("goat.csv",index_col=2)
print(my_data)
print("++++++++++++++++++++++++")

var = ["a","B","C"]
my_series = pd.DataFrame(var)
print(my_series)
print("++++++++++++++++++++++++")


my_data = {"Name":["Dhoni","ashwin","rahul"],"Team":["csk","rr","lsg"]}
print(my_data)
df = pd.DataFrame(my_data, index = ["a","b","c"])
print(df)
df.to_csv("dd.csv")
print(type(df))
print("++++++++++++++++++++++++")


my_data = pd.read_csv("hemanand.csv")
print(my_data)
print(type(my_data))
print("++++++++++++++++++++++++")


my_data = pd.read_csv("hemanand.csv", index_col = 0)
print(my_data)
print(type(my_data))
print("++++++++++++++++++++++++")


import numpy as np

my_list = np.array([2,4,6,8])
output = my_list/2
print(output)
print("++++++++++++++++++++++++")


output = my_list[0]*2
print(output)
print("++++++++++++++++++++++++")


my_data = {"name":["dhoni","virat","rohit"],"Age":["42","36","37"]}
print(my_data)
print(type(my_data))
print("++++++++++++++++++++++++")

my_data_frame = pd.DataFrame(my_data,index=["a","b","c"])
print(my_data_frame)
print("++++++++++++++++++++++++")



