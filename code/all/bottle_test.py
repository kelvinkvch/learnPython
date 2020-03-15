import requests
respone=requests.get('http://localhost:7777/echo/kelvin')
if respone.status_code==200 and \
    respone.text=='Say hello to my little friend:kelvin!':
    print("It worked! That lamost never happens!")
else:
    print('Argh,got this:',respone.text)