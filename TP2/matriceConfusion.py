from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
Y = iris.target
import sklearn.cross_validation

X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y, random_state=0)
from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(Y_test, Y_pred)
print(cm)
