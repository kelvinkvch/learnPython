import matplotlib.pyplot as plt
import numpy as np
import mglearn
from sklearn.neighbors import KNeighborsRegressor
x,y=mglearn.datasets.make_wave(n_samples=40)
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,random_state=0)
fig ,axes=plt.subplots(1,3,figsize=(15,4))
line=np.linspace(-3,3,1000).reshape(-1,1)
for nb,ax in zip([1,3,9],axes):
    reg=KNeighborsRegressor(n_neighbors=nb)
    reg.fit(xtrain,ytrain)
    ax.plot(line,reg.predict(line))
    ax.plot(xtrain,ytrain,'^',c=mglearn.cm2(0),markersize=8)
    ax.plot(xtest,ytest,'v',c=mglearn.cm2(1),markersize=8)
    ax.set_title(
        '{}neighbor(s)\n train score:{:.2f} test score :{:.2f}'.format(
            nb,reg.score(xtrain,ytrain),reg.score(xtest,ytest)
        ))
    ax.set_xlabel('feature')
    ax.set_ylabel('target')
axes[0].legend(['model predictions','training data/target','test data/target'],loc='best')
plt.show()