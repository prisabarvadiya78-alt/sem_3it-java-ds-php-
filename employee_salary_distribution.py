# 5. histogram
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee_salary_distribution.csv")
plt.hist(df["salary"])
plt.title("salary distribution")
plt.xlabel("monthly salary")
plt.ylabel("number of employees")
plt.show()