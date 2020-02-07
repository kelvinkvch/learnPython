import re
import urllib.request
from urllib.error import HTTPError,URLError,ContentTooShortError

def getweb(url,user_agent='wswp',num_retries=2,charset='utf-8'):
    print('Downloading:',url)
    req=urllib.request.Request(url)
    req.add_header('User-agent',user_agent)
    try:
        resp=urllib.request.urlopen(req)
        cs=resp.headers.get_content_charset()
        if not cs:
            cs=charset
        html=resp.read().decode(cs)
    except (HTTPError,URLError,ContentTooShortError) as e:
        print('Download error:',e.reason)
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                getweb(url,num_retries-1)
    return html
def getsitemap(url):
    sitemap=getweb(url)
    links=re.findall(r'<loc>(.*?)</loc>',sitemap)
    for link in links:
        html=getweb(link)

getsitemap('http://example.python-scraping.com/sitemap.xml')
