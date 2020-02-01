from bs4 import BeautifulSoup
import requests
import pandas as pd

web="http://www.quanthockey.com/khl/seasons/2017-18-khl-players-stats.html"
res=requests.get(web)
soup=BeautifulSoup(res.text,'lxml')
tables=soup.select('table')
df=[]
print(tables.prettify())