from sklearn.svm import SVC

X = [[15000], [20000], [25000], [30000],
     [35000], [40000], [50000], [60000]]

y = ['Not Buy', 'Not Buy', 'Not Buy', 'Buy',
     'Buy', 'Buy', 'Buy', 'Buy']

model = SVC(kernel='linear')
model.fit(X, y)

test = [[22000], [28000], [32000], [45000]]
print(model.predict(test))