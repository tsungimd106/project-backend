import requests
from bs4 import BeautifulSoup

__BASEURL="https://lis.ly.gov.tw/lylegiscomc/committeekmout"
def forClear(url):
    # print(url)    
    res = requests.get(url)
    
    res.encoding = "utf-8"
    if not res.ok:    
        exit()    
        print("error")   
        return "error"
    return BeautifulSoup(res.text,'html.parser')

soup = forClear(__BASEURL)

if soup!="error":
    
    
    soup = soup.select('.sumtd2001')    
    print(soup)
exit()
