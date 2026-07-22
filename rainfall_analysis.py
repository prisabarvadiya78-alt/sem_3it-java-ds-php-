# 7. line chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("rainfall_analysis.csv")
plt.plot(df["Month"], df["Rainfall(mm)"], marker='o')
plt.title("Monthly Rainfall Analysis")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()