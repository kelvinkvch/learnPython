from urllib.request import urlopen
from urllib.error import HTTPError,URLError,ContentTooShortError
from bs4 import BeautifulSoup as bsp
def get_title(url):
    try:
        html=urlopen(url)
    except (HTTPError,URLError) as e:
        print("Url could not found,",e)
        return None
    try:
        soup=bsp(html.read(),features='lxml')
        title=soup.body
    except AttributeError as e:
        print('Tag could not found,',e)
        return None
    return title
url="http://pythonscraping.com/pages/page1.html"
title=get_title(url)
if title==None:
    print('Title could not found.')
else:
    print(title.text)