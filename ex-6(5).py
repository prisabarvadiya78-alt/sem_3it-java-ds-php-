from sklearn.naive_bayes import GaussianNB

X = [[25], [30], [35], [40], [45], [55], [65], [75]]
y = ['Fail', 'Fail', 'Fail', 'Pass',
     'Pass', 'Pass', 'Pass', 'Pass']

model = GaussianNB()
model.fit(X, y)

test = [[28], [37], [48], [70]]
print(model.predict(test))