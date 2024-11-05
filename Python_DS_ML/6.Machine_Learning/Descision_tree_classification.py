from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt

#Load iris dataset
iris = load_iris()
X = iris.data
print(X)
print(iris.feature_names)
Y = iris.target
print(Y)
print(iris.feature_names)
class_names = iris.target_names

#Create and train model

clf = DecisionTreeClassifier()
clf.fit(X,Y)
print(X)
print(Y)

#PLOT THE TREE
plt.figure(figsize=(10,8))
plot_tree(clf,filled= True, class_names= class_names, feature_names=iris.feature_names)
plt.title("Decision Tree Classification")
plt.show()

