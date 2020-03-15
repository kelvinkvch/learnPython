# IPython log file

get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('run', 'exciser.py 400')
from time import time
start=time()
delta=time()-start
get_ipython().run_line_magic('run', 'exciser.py 100')
get_ipython().run_line_magic('run', 'exciser.py 9999')
get_ipython().run_line_magic('run', 'exciser.py 9999')
get_ipython().run_line_magic('logstart', '')
get_ipython().run_line_magic('run', 'exciser.py 9999')
get_ipython().run_line_magic('run', 'exciser.py 99999')
get_ipython().run_line_magic('run', 'exciser.py 999999')
time run excier.py 9999
get_ipython().run_line_magic('run', '-d exciser.py 9999')
get_ipython().run_line_magic('run', '-p exciser.py 10000')
hist
hist()
get_ipython().run_line_magic('hist', '')
hist
arange(5)
a=arange(5)
a.dtype
a.ndim
a.shape
a
m=array([arnge(2),arange(2)])
m=array([arange(2),arange(2)])
m
m.shape
m.size()
m
m.size
quit()
