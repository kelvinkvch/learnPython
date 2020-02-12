
import urllib.request
from bs4 import BeautifulSoup
import csv
f = csv.writer(open("bearing.txt", "a",encoding="gb2312"))
f.writerow(["ID", "轴承型号", "国内新型号", "国内旧型号", "国外品牌", "国外品牌型号"])
for page in range(4000,4500):
    url = ('http://c.zcwz.com/index1.asp?mode_x=0&turn_x='+str(page))
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page,'lxml')
    table = soup.find('table')

    # variable to check length of rows
    x = (len(table.findAll('tr')) - 1)
    # set to run through x
    for row in table.findAll('tr')[1:x]:
        col = row.findAll('td')
        id = col[0].getText()
        prtype = col[1].getText()
        newtype = col[2].getText()
        oldtype = col[3].getText()
        outbrand= col[4].getText()
        outype= col[5].getText()
        #vertical = col[6].getText()
        #broad = col[10].getText()
        #shuttle = col[11].getText()
        #threecone = col[12].getText()
        bearing = (id,prtype,newtype,oldtype,outbrand,outype)
        f.writerow(bearing)
