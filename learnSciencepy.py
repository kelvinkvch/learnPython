import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
index=[('california',2000),('california',2010),
        ('new york',2000),('new york',2010),
        ('texas',2000),('texas',2010)]
populations=[33871648,37253956,
            18976457,19378102,
            20851820,25145561]
pop=pd.Series(populations,index=index)
print(pop)