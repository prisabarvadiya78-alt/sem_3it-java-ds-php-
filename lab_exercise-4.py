#1.create line chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#2.create bar chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#3.pie chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
plt.pie(df["Sales"],
 labels=df["Month"],
 autopct='%1.1f%%')
plt.title("Monthly Sales Distribution")
plt.show()

#4.scatter plot
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
plt.scatter(df["Month"], df["Sales"])
plt.title("Monthly Sales Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#5.histogram
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
plt.hist(df["Sales"], bins=5)
plt.title("Sales Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()