from sklearn.svm import SVC

# Input data (Study Hours)
x = [[1], [2], [4], [5]]

# Output data (Result)
y = ["Fail", "Fail", "Pass", "Pass"]

# Create SVM model with a simple linear boundary
model = SVC(kernel="linear")
model.fit(x, y)

# Predict for a new student
hours = [[3]]

prediction = model.predict(hours)

print(prediction)