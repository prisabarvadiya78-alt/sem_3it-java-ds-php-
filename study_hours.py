#4.scatter plot
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("study_hours.csv")
plt.scatter(df["Study Hours"], df["Marks"])
plt.title("Study_hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()