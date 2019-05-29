# coding=utf-8
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('data/online_shoppers_intention.csv', header=0)
print(df.columns)
print(df.head(5))
attributes = np.array(df.columns)
raw_data = df.to_numpy()
# print(raw_data)
enc = LabelEncoder()
for i in [10, 15, 16, 17]:
    a = raw_data[:, i].reshape(-1, 1)
    # print(a.shape)
    raw_data[:, i] = enc.fit_transform(raw_data[:, i])
raw_data[:, -1] = ['r' if i == 1 else 'p' for i in raw_data[:, -1]]
df = pd.DataFrame(raw_data[:, [6, 7, 8, -1]], columns=attributes[[6, 7, 8, -1]])
sns.pairplot(df, hue="Revenue")
plt.show()
