from sklearn import tree

X = [[0, 0], [2, 2]]
Y = [0.5, 2.5]

clf = tree.DecisionTreeRegressor()
clf.fit(X, Y)

print clf

print clf.predict([[2., 2.]])