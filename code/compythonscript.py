from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
iris = load_iris()
xtrain, xtest, ytrain, ytest = train_test_split(
    iris['data'], iris['target'], random_state=0)
df = pd.DataFrame(xtrain, columns=iris['feature_names'])
# pd.plotting.scatter_matrix(df,c=ytrain,alpha=0.8,figsize=(15,10),marker='-',hist_kwds={'bins':20},s=50)
knn=KNeighborsClassifier(n_neighbors=11)
knn.fit(xtrain,ytrain)
x_new=np.array([[5,2.9,1,0.2]])
prediction=knn.predict(x_new)
ypred=knn.predict(xtest)
res=np.mean(ypred==ytest)
print(res)