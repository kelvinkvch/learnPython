import numpy as np
import pandas as pd
index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956, 18975457, 19378102, 20851820, 25145561]
index=pd.MultiIndex.from_tuples(index)
pop=pd.Series(populations,index=index)
under18=[9265089,9284094,4687374,4318033,5906301,6879014]
popdf=pd.DataFrame({'total':pop,'under18':under18})
popdf['f18']=popdf['under18']/popdf['total']
print(popdf)
# print(f_u18.unstack())