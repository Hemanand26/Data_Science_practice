import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

data = {
    'Height': [183.25, 182.71,182.92],
    'Weight': [57,74,None],
    'Age': [None, 45, 32]
}

df = pd.DataFrame(data)
print(df)

SI = SimpleImputer()
df= SI.fit_transform(df)
print(df)