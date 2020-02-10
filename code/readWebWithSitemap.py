import  re
from urllib.error import HTTPError,URLError,ContentTooShortError
import urllib.request

def getweb(url,user_agent='wswp',num_retries=2,charset='utf8'):
    print('Downloading:',url)
    req=urllib.request.Request(url)
    req.add_header('user-agent',user_agent)
    try:
        response=urllib.request.urlopen(req)
        cs=response.headers.get_content_charset()
        if not cs:
            cs=charset
        html=response.read().decode(cs)
    except (HTTPError,URLError,ContentTooShortError) as e:
        print('Download erro:',e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                getweb(url,num_retries-1)
    return html
def getsitemap(url):
    reg=re.compile(r'<loc>(.*?)</loc>')
    sitemap=getweb(url)
    links=reg.findall(sitemap)
    for lin in links:
        getweb(lin)

getsitemap('http://example.python-scraping.com/sitemap.xml')