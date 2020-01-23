import xml.etree.cElementTree as ET
import pandas as pd
import glob
import os
from time import time
t=time()
path=r'e:\工作/bom\h1000 - 副本/'
files=glob.glob(os.path.join(path,'*.xml'))
odf=[]
for file in files:
    tree=ET.parse(file)
    root=tree.getroot()
    drnumber=os.path.basename(file).replace('.xml','')
    nodes=root.findall(".//item/[@type='part']")
    if nodes!=None:
        for ch in nodes:
            id=ch.attrib['id']
            name=ch.attrib['nomeBreve']
            size=ch.attrib['sigla']
            ind=ch.attrib['posizione']
            number=ch.attrib['quantitaMinima']
            odf.append([drnumber,id,name,size,ind,number])
df=pd.DataFrame(odf,columns=['drnumber','id','name','size','ind','number'])
df.to_csv('h1000.csv',index=False)
print('my file used time:{0:.2f}'.format(time()-t))