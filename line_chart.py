#1.create line chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()



