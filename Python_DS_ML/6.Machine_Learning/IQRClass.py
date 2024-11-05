import matplotlib.pyplot as plt
import pandas as pd


data = {"Values":[10,20,30,40,50,60,70,80,90,100]}
df = pd.DataFrame(data)
print(df)

q1 = df["Values"].quantile(0.25)
q2 = df["Values"].median()
q3 = df["Values"].quantile(0.75)
print('\n')
print(q1)
print(q2)
print(q3)
print('\n')
iqr = q3-q1
print(iqr)

lower_fence = q1 - 1.5*iqr
higher_fence = q3 + 1.5*iqr
print('\n')
print("lower_fence",lower_fence)
print("higher_fence",higher_fence)

plt.figure(figsize=(8,6))
plt.boxplot(df["Values"],vert = True)
plt.show()
