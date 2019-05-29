# coding=utf-8
import pandas as pd

df = pd.read_csv('data/online_shoppers_intention.csv', header=0)
print(df.columns)
print(df.head(5))