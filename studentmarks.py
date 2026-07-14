import sys
import pandas as pd
df=pd.read_csv("studentmarks.csv")
print(df)

print("\ndataset shape:")
print(df.shape)

print("\n\n")
print("\n display first 5 rows (default)")
print(df.head())

print("\n\n")
print("\n display first 2 rows")
print(df.head(2))

print("\n")
print("\n display last 5 rows")
print(df.tail())

print("\n")
print("\n display last 3 rows")
print(df.tail(3))

