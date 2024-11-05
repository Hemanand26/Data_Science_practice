import numpy as np

my_array = np.arange(12)
print(my_array)
print(my_array.shape)
print(my_array.ndim)

my_array1 = my_array.reshape(3,4)
print(my_array1)
print(my_array.shape)
print(my_array1.ndim)

reshaped_array = my_array.reshape(-1,1)
print(reshaped_array)
print(type(reshaped_array))
print(reshaped_array.shape)
print(reshaped_array.ndim)

import pandas as pd

data = {"Name":["a","b",None,"Kohli"],"Age":[4,6,26,None]}
my_df = pd.DataFrame(data)

print(my_df)
empty_data = my_df.isnull()
print("+++++++++++++++++++++")
print(empty_data)


