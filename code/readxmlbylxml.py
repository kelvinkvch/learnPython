import pandas as pd
from lxml import etree
from time import time
import csv
import glob
import os
t = time()
path = r"E:\工作\BOM\h1000"
csvfile=open('rrr.csv','w',newline='')
csvwriter=csv.writer(csvfile)
csvwriter.writerow(['id','name','index','size','number','drawingno'])
alldf = []
files = glob.glob(os.path.join(path, '*.xml'))
print(time()-t)

    # file = r"E:\工作\BOM\h1000\33NG39-34_1.xml"
def getxml(file):
    tree = etree.parse(file)
    fl=os.path.basename(file).replace('.xml','')
    nodes=tree.xpath('//item[@type="part"]')
    # if nodes is None:
    #     continue
    if nodes is not None:
        for nd in nodes:
            id=nd.attrib['id']
            nb=nd.attrib['nomeBreve']
            ind=nd.attrib['posizione']
            sz=nd.attrib['sigla']
            nb=nd.attrib['quantitaMinima']    
            csvwriter.writerow([id,nb,ind,sz,nb,fl])
for file in files:
    getxml(file)
csvfile.close()
