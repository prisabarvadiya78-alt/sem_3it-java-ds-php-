from sklearn.neural_network import MLPClassifier

# Training data
X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

# Create and train the model
model = MLPClassifier(
    hidden_layer_sizes=(2,),
    max_iter=5000,
    random_state=42
)

model.fit(X, y)

# Take input from the user
hours = float(input("Enter study hours: "))

# Predict
prediction = model.predict([[hours]])[0]

# Display result
if prediction == 1:
    print("Result: Pass")
else:
    print("Result: Fail")