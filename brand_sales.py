#3.pie chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("brand_sales.csv")
plt.pie(df["Units sold"],
 labels=df["Brand"],
 autopct='%1.1f%%')
plt.title("Smartphone Brand Sales")
plt.show()