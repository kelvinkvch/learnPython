import numpy as np
import pandas as pd
f1 = r"D:\codepractice\python\PythonDataScienceHandbook\notebooks\data\state-population.csv"
f2 = r"D:\codepractice\python\PythonDataScienceHandbook\notebooks\data\state-areas.csv"
f3 = r"D:\codepractice\python\PythonDataScienceHandbook\notebooks\data\state-abbrevs.csv"
pop = pd.read_csv(f1)
areas = pd.read_csv(f2)
abbrevs = pd.read_csv(f3)
merged=pd.merge(pop,abbrevs,how='outer',left_on='state/region', right_on='abbreviation').drop('abbreviation', 1)
merged.loc[merged['state/region']=='USA','state']='Unit states'
merged.loc[merged['state/region']=='PR','state']='Puerto Rico'
final=pd.merge(merged, areas,on='state',how='left')
final=final.dropna()
data2010=final.query("year==2010&ages=='total'")
data2010=data2010.set_index('state')
density=data2010['area (sq. mi)']/data2010['population']

density.sort_values(ascending=False,inplace=True)
print(density.head())