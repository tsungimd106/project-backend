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



def forClear(url):
    res = requests.get(url)
    res.encoding = "utf-8"
    if not res.ok:
        exit()
        return "error"
    return BeautifulSoup(res.text, 'html.parser')


def po():

    soup = forClear(URL)
    if soup != "error":
        soup.encoding = 'utf-8'
    b = list(soup.text)
    data = json.loads(soup.text)
    sql=[]
    for i in data:
        if i["createDateStr"][0:3]=="110":

            c = gg(DETAIL+i["publishUrl"]+'/'+str(i["contentId"]))
            c = re.sub(r'"',"'" , c)
            c = re.sub(r"\n", '', c)
            title = re.sub(r"'", '"', i["title"])
            date = re.sub(r"\.","-",i["createDateStr"])
        sql.append({"sql":"insert into article (title,content,type,createTime) VALUES(\"%s\", \"%s\", %s,\"%s\")" % (
        title,c,2,"2021"+date[3:]),"name":i["contentId"]})
    return DB.execution(DB.create, sql)


def gg(url):

    options=Options()
    options.add_argument("--disable-notifications")

    chrome=webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get(url)
    soup=BeautifulSoup(chrome.page_source, 'html.parser')
    content=soup.find("div", {"class": "main-cont"})
    downloadlist=soup.find("div", {"class": "downloadlist"})

    chrome.close()
    return (content.prettify()) + (downloadlist.prettify())
    

po()
