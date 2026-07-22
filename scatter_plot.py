#4.scatter plot
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
plt.scatter(df["Month"], df["Sales"])
plt.title("Monthly Sales Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()