# 8. pie chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("book_categories.csv")
plt.pie(df["Number of Books"],labels=df["Category"],autopct='%1.1f%%')
plt.title("Library Book Categories")
plt.show()