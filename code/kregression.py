import numpy as np
import matplotlib.pyplot as plt
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

x,y=mglearn.datasets.make_wave(n_samples=40)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,random_state=0)
line=np.linspace(-3,3,1000).reshape(-1,1)
fig,axes=plt.subplots(1,3, figsize=(15,5))
for nbs,ax in zip([1,3,9],axes):
    reg=KNeighborsRegressor(n_neighbors=nbs)
    reg.fit(xtrain,ytrain)
    ax.plot(line,reg.predict(line))
    ax.plot(xtrain,ytrain,'^',c=mglearn.cm2(0),markersize=8)
    ax.plot(xtest,ytest,'v',c=mglearn.cm2(1),markersize=8)
    ax.set_title(
        '{0} models\n train score {0:.2f} test score {1:2f}'.format(nbs,reg.score(xtrain,ytrain),reg.score(xtest,ytest))
    )
    ax.set_xlabel('feature')
    ax.set_ylabel('target')
axes[0].legend(['model','train','test'],loc='best')
plt.show()