import numpy as np
from sklearn.datasets import  load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris=load_iris()
xtrain,xtest,ytrain,ytest=train_test_split(iris.data,iris.target,random_state=0)
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(xtrain,ytrain)
# predict=knn.predict(xtest)
res=knn.score(xtest,ytest)
print(res)