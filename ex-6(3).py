from sklearn.neighbors import KNeighborsClassifier

X = [[18], [20], [22], [25], [30], [32], [35], [38]]
y = ['Normal', 'Normal', 'Normal', 'Normal',
     'Hot', 'Hot', 'Hot', 'Hot']

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

test = [[23], [28], [31], [36]]
print(model.predict(test))