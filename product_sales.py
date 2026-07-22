# 6. bar chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("product_sales.csv")
plt.barh(df["Product"], df["Units Sold"])
plt.title("Product sales comparison")
plt.xlabel("Units Sold")
plt.ylabel("Product")
plt.show()