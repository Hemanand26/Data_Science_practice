import matplotlib.pyplot as plt
import numpy as np

# import seaborn as sns

# Below code is to one plot

# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
#
# plt.plot(x,y)
#
# plt.show()
#
# # Below code is to show multiply plot


x = [1,2,3,4,5]
y = [2,3,5,7,11]

x1 = [5,10,15,20,25]
y1 = [10,15,20,25,30]


"""in the below subplot functions (2,1) indicates 2 rows and 1 columns
Note: Need to use same number variable like (a,b,c) if we have subplots as (1,3)"""

# fig,(a,b) = plt.subplots(2,1)
# fig variable is used to set command attributes to both the plots
# fig.suptitle("Testing Two")
# it adjust prevent overlapping
# fig.tight_layout()
# a.plot(x,y)
# a.set_title("graph")
# a.set_xlabel("x lable")
# a.set_ylabel("y lable")
# b.plot(x1,y1, marker = "x", linestyle = "--", color = "Green")

# to save fig in local maching
# fig.savefig("hema1.png")

# plt.show()

# x = ["Dhoni", "Ashwin","Kohli","Raina"]
# y = [7,99,18,3]
# plt.bar(x,y)
# plt.show()

"""Below is to show histogram chart but with data generated from numpy np.random.randn(100) ---> This generate random 100 numbers that 
has mean = 0, std = 1"""

# data = np.random.randn(100)
# print(data)
# print(data.ndim)
# plt.hist(data,bins = 15, edgecolor = "black",color= "yellow")
# plt.show()

"""  Scatter plot  """

# x = np.random.rand(100)
# y = 2*x + np.random.rand(100)
#
# print (x)
# print (y)
#
# plt.scatter(x,y)
# plt.show()

""" Pie chart """

name = ["Dhoni", "Ashwin", "Raina", "Karthick"]
age =[42, 36, 38,37]
col = ["blue","pink","yellow","red"]
exp = [0,0,0.1,0]
plt.pie(age,colors = col,explode= exp, labels = name, autopct = "%1.2f%%" )
plt.show()

# autopct() function is to find the distribution in the pie chart eg: like vote share b/w dmk, admk, ntk





