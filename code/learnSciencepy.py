import numpy as np
x=np.array([1.0,0.5])
w1=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
b1=np.array([0.1,0.2,0.3])
a1=np.dot(x,w1)+b1

w2=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
b2=np.array([0.1,0.2])
a2=np.dot(a1,w2)+b2
print(a2)