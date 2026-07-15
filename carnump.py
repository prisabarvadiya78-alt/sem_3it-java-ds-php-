import sys
import pandas as pd
df=pd.read_csv("carnump.csv")
print(df)

print("\ndataset shape:")
print(df.shape)

print("\n\n")
print("\n display first 4 rows (default)")
print(df.head())

print("\n\n")
print("\n display first 5 rows")
print(df.head(5))

print("\n")
print("\n display last 1 rows")
print(df.tail())

print("\n")
print("\n display last 3 rows")
print(df.tail(3))

