# 9. bar chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("student_mark_comparison.csv")
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks Comparison")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()