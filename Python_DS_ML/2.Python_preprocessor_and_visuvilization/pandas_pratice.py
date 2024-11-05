import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:1])

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

import pandas as pd

data = [{'Geeks': 'Sibu', 'for': 'the','geeks':'great'},{'Geeks': 67, 'for': 78,'geeks':98}]
df1 = pd.DataFrame(data, index = ['1','2'],columns= ['Geeks','for'])
df2 = pd.DataFrame(data, index = ['1','2'])
print(df1)
print(df2)









