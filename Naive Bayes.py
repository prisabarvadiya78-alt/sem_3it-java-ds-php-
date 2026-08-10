from sklearn.naive_bayes import GaussianNB

# Input data (Study Hours)
X = [[1], [2], [4], [5]]

# Output data (Result)
y = ["Fail", "Fail", "Pass", "Pass"]

# Create Naive Bayes model
model = GaussianNB()

# Train the model
model.fit(X, y)

# Give new input
hours = [[3]]

# Predict result
prediction = model.predict(hours)

# Print result
print(prediction)