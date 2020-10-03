import requests
from bs4 import BeautifulSoup


__BASEURL="https://www.ly.gov.tw/"
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
    soup = soup.select('.inner a')
    count=0
    for item in soup:
        count=count+1
        # print(item)
        # print("-"*3)
        # print(item.get("href"))
        # print("-"*7)
        # smallSoup=forClear(__BASEURL+item.get("href"))
        # smallSoup=smallSoup.select("article")
        # print(smallSoup)
    print(count)
exit()
    



