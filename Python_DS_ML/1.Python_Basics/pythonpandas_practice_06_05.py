import pandas as pd

#basis program

# my_car = {"cars":["BMW","Honda","Audi"],"posision":[1,2,3]}
# my_vehical = pd.DataFrame(my_car)
# print(my_vehical)

#Series program and print lable

# a = [1,7,2]
# b = pd.Series(a)
# print(b)
# print(b[0])

# Create index

# a = [1,7,2]
# b = pd.Series(a, index = ["x","y","z"])
# print(b)

# Data Frame

# data = {"Cal":[380,789,567],"duration":[50,40,45]}
# print(data)
# data1 = pd.DataFrame(data)
# print(data1)

# Locate Row using loc() function

# print(data1.loc[1:])

# Add index to DF

# data = {"Cal":[380,789,567],"duration":[50,40,45]}
# print(data)
# data1 = pd.DataFrame(data, index= ["Lays","Cheetos","Timepass"])
# print(data1)
# print(data1.loc["Lays"])

# Load Files into CSV
#
# data2 = data1.to_csv(r"D:\LMES\DS and ML data1.csv")
# data3 = pd.read_csv('DS and ML data1.csv')

# head () is used to print top rows from starting from top and tail() is used to print

df = pd.read_csv('data1.csv')
# print(df.head(1))
# print(df.tail(1))

# info () gives information about data

print(df.info())


