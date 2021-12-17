import requests
from model.db import DB
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
import os
import csv
import re

URL = "https://www.cec.gov.tw/central/cmsList/latestNews?order=asc&offset=0&limit=10&begin=&end=&title="
DETAIL = "https://www.cec.gov.tw/central/cms/"
TEST = "https://www.cec.gov.tw/central/cms/110news/35529"

# 抓取中選會連結導向政要RUN


def forClear(url):
    res = requests.get(url)
    res.encoding = "utf-8"
    if not res.ok:
        exit()
        return "error"
    return BeautifulSoup(res.text, 'html.parser')

# 先找到連結位置


def po():
    soup = forClear(DETAIL)
    if soup != "error":
        soup.encoding = 'utf-8'
    b = list(soup.text)
    data = json.loads(soup.text)
    sql = []
    for i in data:
        links = soup.find("td", {"class": "col-md-10"}).find("a"["href"])
        #for link in links.ol.children:
            #if link != '\n':
                #print(link.text + ':  ', link.a.get('href'))
        sql.append({"sql": "insert into article (title,content,type,createTime) VALUES(\"%s\", \"%s\", %s,\"%s\")" % (
            title, , 2, "2021"+date[3:]), "name": i["contentId"]})


'''def po():

    soup = forClear(URL)
    if soup != "error":
        soup.encoding = 'utf-8'
    b = list(soup.text)
    data = json.loads(soup.text)
    sql=[]
    for i in data:
        if i["createDateStr"][0:3]=="110": #篩選今年的公告

            c = gg(DETAIL+i["publishUrl"]+'/'+str(i["contentId"]))
            c = re.sub(r'"',"'" , c) #把雙引號取代成單引號
            c = re.sub(r"\n", '', c) #把換行取代成空白
            title = re.sub(r"'", '"', i["title"])
            date = re.sub(r"\.","-",i["createDateStr"]) #日期格式修改避免資料庫格式跑掉
        sql.append({"sql":"insert into article (title,content,type,createTime) VALUES(\"%s\", \"%s\", %s,\"%s\")" % (
        title,c,2,"2021"+date[3:]),"name":i["contentId"]})
    
    return DB.execution(DB.create, sql)'''


def gg(url):

    options = Options()
    options.add_argument("--disable-notifications")

    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get(url)
    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    connection = soup.find("")
    content = soup.find("div", {"class": "main-cont"})
    # 公告是純文字的
    downloadlist = soup.find("div", {"class": "downloadlist"})
    # 公告有附檔的

    chrome.close()
    return (content.prettify()) + (downloadlist.prettify())
    # 輸出排版後的兩者合併


po()
