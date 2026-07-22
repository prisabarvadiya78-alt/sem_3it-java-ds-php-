#3.pie chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
plt.pie(df["Sales"],
 labels=df["Month"],
 autopct='%1.1f%%')
plt.title("Monthly Sales Distribution")
plt.show()