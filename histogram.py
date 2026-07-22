#5.histogram
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
plt.hist(df["Sales"], bins=5)
plt.title("Sales Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()