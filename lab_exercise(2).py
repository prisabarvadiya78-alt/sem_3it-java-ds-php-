# student marks analysis 
import numpy as np
marks = np.array([78, 85, 90, 67, 72, 95, 88])
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

#supermarket sales 
import numpy as np
sales = np.array([1200, 1500, 1100, 1800, 1700, 2000, 1600])
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))

# whether Analysis 
import numpy as np
temperature = np.array([32, 33, 34, 36, 35, 31, 30])
print("Average Temperature:", np.mean(temperature))
print("Maximum Temperature:", np.max(temperature))

# Hospital patient monitoring 
import numpy as np
heart_rate = np.array([72, 75, 80, 78, 76])
print("Average Heart Rate:", np.mean(heart_rate))

# cricket statistics 
import numpy as np
runs = np.array([45, 60, 12, 98, 75, 33])
print("Average Runs:", np.mean(runs))
print("Highest Score:", np.max(runs))

# image processing 
import numpy as np
image = np.array([
 [120,130,125],
 [200,210,205],
 [50,60,55]
])
print(image)

# stock market 
import numpy as np
prices = np.array([250,255,248,260,270])
print("Average Price:", np.mean(prices))
print("Highest Price:", np.max(prices))

#Internet of Things (IoT)
import numpy as np
sensor = np.array([28.5,29.1,28.8,29.3,28.9])
print("Average:", np.mean(sensor))

# Banking
import numpy as np
transactions = np.array([500,-200,1000,-150,250])
print("Net Balance Change:", np.sum(transactions))

#Machine Learning
import numpy as np
houses = np.array([
 [1200,2],
 [1500,3],
 [1800,4]
])
print(houses)



# Marks of students
marks = np.array([78, 65, 89, 91, 73, 84, 67, 95, 80, 76])
total = np.sum(marks)
average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)

above_80 = np.sum(marks > 80)


print("Student Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Number of Students Score Above 80:", above_80)


