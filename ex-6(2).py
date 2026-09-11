from sklearn.tree import DecisionTreeClassifier

X = [[45], [50], [60], [70], [75], [80], [85], [90]]
y = ['Not Eligible', 'Not Eligible', 'Not Eligible',
     'Eligible', 'Eligible', 'Eligible', 'Eligible', 'Eligible']

model = DecisionTreeClassifier()
model.fit(X, y)

test = [[55], [65], [72], [88]]
print(model.predict(test))