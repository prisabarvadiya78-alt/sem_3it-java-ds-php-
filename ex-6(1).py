from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = ['Fail', 'Fail', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass']

model = DecisionTreeClassifier()
model.fit(X, y)

test = [[2.5], [3.5], [4.5], [6]]
print(model.predict(test))