import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Zomato data .csv")  #Reads the data from file#
def handlerate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

data['rate'] = data['rate'].apply(handlerate) # Splits / from rate column

df = pd.DataFrame(data)   #converts the datainto 2D#
# print(df.to_string())    #prints all the data in output screen#

print(df.info())  # Gets information about dataset, we can see any null values present and type of datatype

sns.countplot(x=df['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.show()

# Here we use seaborn library to visualize the type of restaurant people prefer

grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame(grouped_data)
plt.plot(result, c ="green", marker = "o")
plt.xlabel("Type of Restaundant" ,c="red",size = 20)
plt.ylabel("Votes",c="red",size=20)
plt.show()

# Here we showed the plot to understand higest no of votes for type of resturdant

max_votes = df['votes'].max()
restaurant_with_max_votes = df.loc[df['votes'] == max_votes, 'name']

print("Restaurant(s) with the maximum votes:")
print(restaurant_with_max_votes)

# The above code prints the maximum votes by hotel name

sns.countplot(x=data['online_order'])
plt.show()

# This suggests that a majority of the restaurants do not accept online orders

plt.hist(df['rate'],bins = 5)
plt.title("Rating Distributed")
plt.show()

# The majority of restaurants received ratings ranging from 3.5 to 4

couple_data =df['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show()

# The majority of couples prefer restaurants with an approximate cost of 300 rupees.

plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = df)
plt.show()

# Offline orders received lower ratings in comparison to online orders, which obtained excellent ratings

pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()




