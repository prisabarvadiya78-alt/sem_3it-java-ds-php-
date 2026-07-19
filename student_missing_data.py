import sys
print("\n  Read the CSV File")
import pandas as pd
df = pd.read_csv("student_missing_data.csv")
print(df)

print("\n  Display Dataset Information ")
print(df.info())

print("\n Count Missing Values")
print(df.isnull().sum())

print("\n  Display Rows Containing Missing Values")
print(df[df.isnull().any(axis=1)])


print("\n  Fill Missing Age with Average Age")
df['age'] = df['age'].fillna(df['age'].mean())
print(df)

print("\n  Fill Missing Marks with Average Marks")
df['marks'] = df['marks'].fillna(df['marks'].mean())
print(df)

print("\n  Check Duplicate Records")
print(df.duplicated())

print("\n   Count Duplicate Records")
print(df.duplicated().sum())

print("\n Display Duplicate Records ")
print(df[df.duplicated()])

print("\n  Remove Duplicate Records ")
df = df.drop_duplicates()
print(df)

print("\n Display Dataset After Cleaning")
print(df)


print("\n Save the Clean Dataset")
df.to_csv("student_cleaned_data.csv", index=False)
print("Dataset cleaned successfully.")


