import pandas as pd
my_data = {"Name": ["Dhoni", "Ashwin", "Raina", None],"Age": [42,38,None,22]}
print(my_data)
df = pd.DataFrame(my_data)
print(df)
print("++++++++++++++++++")

""" Below two lines will store 100 in all the places where data is not found"""

# df.fillna(100, inplace = True)
# print(df)
# print("++++++++++++++++++")

"""Below code will substitute the mean into the places where data is not found """

# df.fillna(df["Age"].mean(), inplace = True)
# print(df)
# print("++++++++++++++++++")

"""Below code is the latest way of doing the above one """

df.fillna({"Age":df["Age"].mean()}, inplace = True)
print(df)
print("++++++++++++++++++")
""" Below code will replace empty row with mean value only for age column """

# df["Age"].fillna(df["Age"].mean(), inplace = True)
# print(df)
#
# print("+++++++++++++++++++++++++")
"""Below code will replace the previous and next cell data from the given dataset"""

# df.fillna(method='bfill', inplace= True)
# print(df)
# print("+++++++++++++++++++++++++")

"""Below code will replace the previous and next cell data from the given dataset"""
# df.fillna(method='ffill', inplace= True)
# print(df)