import urllib.request
import pandas as pd
requst=urllib.request.Request('http://c.zcwz.com/index1.asp?mode_x=0&turn_x=1')
user_header='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
requst.add_header('User-agent',user_header)
html=urllib.request.urlopen(requst).read()
df=pd.read_html(html)
dt=pd.DataFrame(df)
dt.to_csv('df.csv')