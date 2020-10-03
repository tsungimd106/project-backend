import requests
from bs4 import BeautifulSoup


__BASEURL="https://vote.ly.g0v.tw/candidate/%E8%87%BA%E5%8C%97%E5%B8%82%E7%AC%AC%E4%B8%80%E9%81%B8%E8%88%89%E5%8D%80/%E5%90%B3%E6%80%9D%E7%91%A4"
def forClear(url):
    # print(url)    
    res = requests.get(url)
    if not res.ok:    
        exit()    
        print("error")   
        return "error"
    return BeautifulSoup(res.text,'html.parser')

soup = forClear(__BASEURL+'Pages/List.aspx?nodeid=109')
print(soup)
if soup!="error":
    soup = soup.select('.Muibox-root jss1664 jss1658')
    count=0
    for item in soup:
        
         print(item)
         print("-"*3)
         print(item.get("href"))
         print("-"*7)
         smallSoup=forClear(__BASEURL+item.get("href"))
         smallSoup=smallSoup.select("article")
         print(smallSoup)
    
exit()
    



