from sklearn.neighbors import KNeighborsClassifier

# Input data (Study Hours)
x = [[1], [2], [4], [5]]

# Output data (Result)
y = ["Fail", "Fail", "Pass", "Pass"]

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)

# Predict for a new student
hours = [[3]]

prediction = model.predict(hours)

print(prediction)