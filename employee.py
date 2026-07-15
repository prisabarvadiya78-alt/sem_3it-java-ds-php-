import sys
import pandas as pd
df=pd.read_csv("employee.csv")
print(df)

print("\ndataset shape:")
print(df.shape)

print("\n\n")
print("\n display first 5 rows (default)")
print(df.head())

print("\n\n")
print("\n display first 6 rows")
print(df.head(6))

print("\n")
print("\n display last 4 rows")
print(df.tail())

print("\n")
print("\n display last 3 rows")
print(df.tail(3))

