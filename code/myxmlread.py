import pandas as pd
import glob
import os
import xml.etree.cElementTree as ET
from time import time

t=time()

def getxml(path):
    files = glob.glob(os.path.join(path, '*.xml'))
    df = []
    # dffinal=pd.DataFrame(columns=['drawing','id','name','size','index','number'])
    for file in files:
        root = ET.parse(file)
        nodes = root.findall(".//item[@type='part']")
        # if nodes !=None:
        #     node = root.findall(".//item")
            # continue
        for element in nodes:               
            drawing=os.path.basename(file)
            id= element.attrib['id']
            name = element.attrib['nomeBreve']
            size= element.attrib['sigla']
            index = element.attrib['posizione']
            number = element.attrib['quantitaMinima']
            df.append([drawing,id,name,size,index,number])
    listall = pd.DataFrame(df,columns=['drawing','id','name','size','index','nubmer'])
    # listall=pd.concat(listall,ignore_index=True)
    listall.to_csv('h1000.csv',index=False)
path = r"E:\工作\BOM\h1000"
getxml(path)
print("{0:.2f}".format(time()-t))