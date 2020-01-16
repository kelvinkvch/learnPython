import pandas as pd
import numpy as np
import seaborn as sns
titanic=sns.load_dataset('titanic')
pvt=titanic.pivot_table('survived', index='class',columns='sex')*100
print(pvt)