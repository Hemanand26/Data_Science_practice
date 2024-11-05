import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://api.coingecko.com/api/v3/coins/markets"

parameter = { "vs_currency": "usd",
              "order": "market_cap_desc",
              "per_page": 100,
              "page": 1,
              "sparkline": False}

response = requests.get(url, params = parameter)
data = response.json()
print(data)

df = pd.DataFrame(data)
print(df)

df.dropna(inplace=True)
df['market_cap'] = df["market_cap"].astype(int)

df_describe = df.describe()
print(df_describe)

plt.figure(figsize=(10,8))
sns.histplot(df['market_cap'],bins =50,kde= True )
plt.show()
