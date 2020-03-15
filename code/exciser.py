import numpy as np
from time import  time
import sys
def pythonsum(n):
    a=list(range(n))
    b=list(range(n))
    c=[]
    for i in range(n):
        a[i]=i**2
        b[i]=i**3
        c.append(a[i]+b[i])
    return c

def numpysum(n):
    a=np.arange(n)**2
    b=np.arange(n)**3
    c=a+b
    return c

size=int(sys.argv[1])
start=time()
result=pythonsum(size)
pythondelta=(time()-start)*10000
print('python sum the last 2 elements is:',result[-2:])
# print('pythonsum used time {0:2f}'.format(delta*10000))
print('')
start=time()
result=numpysum(size)
numpydelta=(time()-start)*10000
print('numpy sum the last 2 elements is:',result[-2:])
print(pythondelta/numpydelta)
print('='*30)