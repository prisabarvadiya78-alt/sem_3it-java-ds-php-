# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

# Input data (Study Hours)
X = [[1], [2], [4], [5]]

# Output data (Result)
y = ["Fail", "Fail", "Pass", "Pass"]

# Create Decision Tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# Give new input
hours = [[7]]

# Predict result
prediction = model.predict(hours)
print(prediction)