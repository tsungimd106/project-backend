import requests
from bs4 import BeautifulSoup
import json
from .spliderPolitican import web

__LYGOV_URL = "https://data.ly.gov.tw/odw/openDatasetJson.action?id=9&selectTerm=all&page=1"
__PO_URL = "https://data.ly.gov.tw/odw/openDatasetJson.action?id=20&selectTerm=all&page="


def forClear(url):
    res = requests.get(url)
    res.encoding = "utf-8"
    if not res.ok:
        exit()
        return "error"
    return BeautifulSoup(res.text, 'html.parser')


def lygov():
    soup = forClear(__LYGOV_URL)
    if soup != "error":
        soup.encoding = 'utf-8'
        data = json.loads(str(soup))
        count = 0
        for i in data["jsonList"]:
            web.createlygov(i)
            print("_"*7)
            # _____________________
            count += 1
            if(count > 25):
                break
    else:
        print("立法院open data error")
    exit()


def po():
    for i in range(1,22):
        soup = forClear(__PO_URL+i)
        if soup != "error":
            soup.encoding = 'utf-8'
            data = json.loads(str(soup))
            # print(str(soup))
            count = 0
            for i in data["jsonList"]:
                web.createpo(i)
                print("_"*7)
                # _____________________
                count += 1
                #if(count > 100):
                    #break
        else:
            print("立法院提案open data error")
        exit()
po()

# lygov()

