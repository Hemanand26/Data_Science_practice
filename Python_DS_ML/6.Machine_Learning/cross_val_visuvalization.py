import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
good_data = np.random.normal(loc=50,scale=5,size=100)
good_df = pd.DataFrame(good_data, columns=["Good_Data_Performance"])

bad_data = np.random.normal(loc=50,scale=5,size=100)
bad_data = np.append(bad_data, [150,160,170,180,190])

bad_df = pd.DataFrame(bad_data,columns=["Bad_Data_Performance"])

combined_df = pd.concat([good_df,bad_df],axis=1)
plt.figure(figsize=(10,8))
plt.subplot(1,2,1)
plt.boxplot(good_df['Good_Data_Performer'],vert = False)
plt.title("Good Data")

plt.subplot(1,2,2)
plt.boxplot(good_df['Bad_Data_Performer'],vert = False)
plt.title("Bad Data")

plt.tight_layout()
plt.show()