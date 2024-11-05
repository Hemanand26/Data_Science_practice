import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print("++++++++++++++++++++")
data = {"Name":["a","b",None,"Kohli"],"Age":[4,6,26,None]}
data = pd.DataFrame(data)
print(data)
print("++++++++++++++++++++")
empty_data = data.isnull()
print(empty_data)
print("+++++++++++++++++++++")

my_data = pd.read_csv("match_data.csv")
print(my_data)

empty_data = my_data.isnull()
print(empty_data)

empty_data_column = my_data['other_player_dismissed'].isnull()
print(empty_data_column)

my_data['other_player_dismissed'] = my_data['other_player_dismissed'].fillna(200, inplace= True)
my_data['other_player_dismissed'] = my_data['other_player_dismissed'].fillna(200)


delete1 = my_data.dropna(axis=1, how="all")

print(delete1)



