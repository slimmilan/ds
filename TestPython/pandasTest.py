import pandas as pd
import numpy as np

df1 = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item', sep='\t')
print(df1.head())
print(type(df1.head()))

df2 = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
df2.head()
print(df2.head())

