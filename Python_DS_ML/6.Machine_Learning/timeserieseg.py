from dateutil.parser import parse
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

plt.rcParams.update({"figure.figsize":(10,7),"figure.dpi":120})
df = pd.read_csv("a10.csv",parse_dates=["date"],index_col = "date")
print(df.head(10))

print(df.index)
print("_______________________")
print(df["number"])
print(df.["number"].shape)
print(df.["number"].ndim)
print("-------------------------------")

def draw_plot(df,x,y,title="",xlable = "Date",ylable="Value",dpi=100):
    plt.plot(x,y,color = "tab:red")
    plt.gca().set(title=title,xlable=xlable,ylable=ylable)
    plt.show()
draw_plot(df,x=df.index,y=df["number"],title="testing time series")

"-------------------------Time series 2--------------------"
df = pd.read_csv("a10.csv",parse_dates=["date"],index_col="date")
df.reset_index(inplace = True)

df["Year"] = [x.year for x in df.date] #list comprehension is used here for fetcing year from the dataset
print(df)

df["month"] = [x.strftime("%b") for x in df.date] #list comprehension is used here for fetcing year from the dataset
print(df)

plt.figure(figsize = (16,12),dpi=80)
for i,y in enumerate(unique_years):
    if i>0:
        plt.plot("month","value",data = df.loc[df.year==y,:],color=my_colors[i],label =y)
        plt.text(df.loc[df.year ==y,:].shape[0]-.9,df.loc[df.year==y,"value"][-1:].values[0],y,fontsize=12)
plt.legend()
plt.show()

# converted_year = []
# for x in df.date:
#     converted_year.append(x.year)
# df["Year"] = converted_year
# print(df)