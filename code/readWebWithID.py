import re
import urllib.request
from urllib.error import HTTPError,URLError,ContentTooShortError
proxy='http://myproxy.net:1234'
proxy_support=urllib.request.ProxyHandler({'http':proxy})
opener=urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
def getweb(url,user_agent='wswp',num_reties=2,charset='utf-8',proxy=None):
    print('downloading:',url)
    request=urllib.request.Request(url)
    request.add_header('user-agent',user_agent)
    try:
        if proxy:
            proxy_support=urllib.request.ProxyHandler({'http':proxy})
            opener=urllib.request.build_opener(proxy_support)
        resp=urllib.request.urlopen(request)
        cs=resp.headers.get_content_charset()
        if not cs:
            cs=charset
        html=resp.read().decode(cs)
    except (HTTPError,URLError,ContentTooShortError) as e:
        print('download error:',e.reason)
        html=None
        if num_reties>0:
            if hasattr(e,'code') and 500<e.code<600:
                return getweb(url,num_reties-1)
    return html
res=getweb('http://example.python-scraping.com/site.xml')
print(res)