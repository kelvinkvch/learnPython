import requests
from lxml import etree
from bs4 import BeautifulSoup as bsp
url=r'https://news.ifeng.com/c/special/7tPlDSzDgVk'
hds={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
web=requests.get(url,headers=hds)
tree=etree.HTML(web.text)
rows=tree.xpath('//div[@class="tbody-3sEej9JG"]/div')
print(rows)