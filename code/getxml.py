from lxml import etree as et
from bs4 import BeautifulSoup as bsp
import pandas as pd

file=r'd:\codepractice\learnPython\scfile\65NG00R1-04_1.xml'
tree=et.parse(file)
soup=bsp(et.tostring(tree),'lxml')
item=soup.select('item')
df=[]
for it in item:
   print(it.prettify())