from lxml import etree
from lxml import  html
url=r'http://example.python-scraping.com/view/Botswana-30'
import requests
web=requests.get(url)
tree=etree.HTML(web.text)
print(etree.text())a