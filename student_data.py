import sys
import pandas as pd
df=pd.read_csv("student_data.csv")
print(df)

print("\ndisplay first five records:")
print(df.head())

print("\ndisplay last five records:")
print(df.tail())

print("\ndisplay shape of dataset:")
print(df.shape)

print("\ndisplay column names:")
print(df.columns)

print("\ndisplay data types:")
print(df.dtypes)

print("\ndisplay dataset information:")
print(df.info())


print("\nstatical summary:")
print(df.describe())

print("\ndisplay name and marks:")
print(df[['name','marks']])

print("\nstudents having marks greater than 80:")
print(df[df['marks']>80])


print("\nstudents from rajkot:")
print(df[df['city']=="Rajkot"])

print("\nsort by marks(ascending):")
print(df.sort_values(by='marks'))

print("\nsort by marks(descending):")
print(df.sort_values(by='marks', ascending=False))

print("\nmaximum marks:")
print(df['marks'].max())

print("\nminimum marks:")
print(df['marks'].min())

print("\n average marks:")
print(df['marks'].mean())

print("\n count total students:")
print(df['name'].count())

print("\n add a new column:")
df['Result'] = "Pass"
print(df)

print("\n save updated csv file:")
df.to_csv("new_student_data.csv", index=False)
print("CSV file saved successfully.")
