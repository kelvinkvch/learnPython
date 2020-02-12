import requests
from bs4 import BeautifulSoup
import pandas as pd
def getweb(url,user_agent='wswp',num_retries=2):
    print('Downloading:',url)
    headers={'user-agent':user_agent}
    try:
        resp=requests.get(url,headers)
        html=resp.text
        if resp.status_code>=400:
            print('Download error1:',resp.text)
            html=None
            if num_retries and 500<=resp.status_code<600:
                # num_retries-=1
                return getweb(url,num_retries-1)
    except requests.exceptions.RequestException as e:
        print('Download error2:',e.strerror)
        html=None
    return html

url='http://example.python-scraping.com/view/UnitedKingdom-239'
html=getweb(url)
soup=BeautifulSoup(html,'lxml')
tr=soup.find_all(attrs={'class':'w2p_fw'})
for t in tr:
    print(t.text)