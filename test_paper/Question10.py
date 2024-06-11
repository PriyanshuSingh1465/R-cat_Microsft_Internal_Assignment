import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder


data = {
    'A': ['x', 'y', np.nan, 'z', 'x'],
    'B': [1, 2, 3, np.nan, 5],
    'C': [10, 20, np.nan, 40, 50]
}
df = pd.DataFrame(data)


df[['B', 'C']] = SimpleImputer().fit_transform(df[['B', 'C']])

df = pd.get_dummies(df, columns=['A'], drop_first=True)

print("Dataset after handling missing values and categorical data:")
print(df)

# output :
# Dataset after handling missing values and categorical data:
#       B     C    A_y    A_z
# 0  1.00  10.0  False  False
# 1  2.00  20.0   True  False
# 2  3.00  30.0  False  False
# 3  2.75  40.0  False   True
# 4  5.00  50.0  False  False
