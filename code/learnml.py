from sklearn.model_selection import train_test_split
import mglearn
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
xtrain, xtest, ytrain, ytest = train_test_split(
    cancer.data, cancer.target, random_state=0)
forest=RandomForestClassifier(n_estimators=100,random_state=0)
forest.fit(xtrain,ytrain)
print(forest.score(xtrain,ytrain))
print(forest.score(xtest,ytest))