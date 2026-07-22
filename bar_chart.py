#2.create bar chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()