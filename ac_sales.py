# 1.bar chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Ac_sale.csv")
plt.bar(df["Month"], df["Ac_sales"])
plt.title("Monthly ac Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()