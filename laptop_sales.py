#2.line chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("laptop_sales.csv")
plt.plot(df["Month"], df["laptop_sales"], marker='o')
plt.title("Monthly laptop_sales")
plt.xlabel("Month")
plt.ylabel("laptop_sales")
plt.show()