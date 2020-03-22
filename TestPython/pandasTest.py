import pandas as pd
import numpy as np
import pyarrow as pa

df1 = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item', sep='\t')
#print(df1.head())
#print(type(df1.head()))

df2 = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
df2.head()
#print(df2.head())

df3 = pd.read_orc('/home/soubhagyah/oldHome/soubhagya/Downloads/prateek/sadb/ss7_model/map/roamertype=2/eventdate=2019-03-21/bintime=1553140800/part-00126-ea88b0d4-0fec-415a-a1d0-31526ad58134.c000.snappy.orc')
print(df3.head())
