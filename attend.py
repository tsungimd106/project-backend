# -*- coding: UTF-8 -*-
import requests
from model.db import DB
import statistics
import numpy as np
from bs4 import BeautifulSoup
import re
import time
time.sleep(0.6)

def findPolid():
    sqlstr = "select name,figure_id,p.id from politician as p inner Join figure as f on f.id =p.figure_id"
    return DB.execution(DB.select, sqlstr)


def findPolitician():
    sqlstr = "select id,figure_id from politician"
    return DB.execution(DB.select, sqlstr)


def returnAttend(polid, session1, avg):
    sqlstr = "insert into attendance(politician_id,session,attend) VALUES ('%s',%s,%s)" % (
        polid, session1, avg)
    return DB.execution(DB.create, sqlstr)


polid = findPolid()

for i in polid["data"]:
        n = i["name"]
        m = i["id"]
for page in range(1, 407):
    response = requests.get(
        "https://ccw.org.tw/assess/38/legislator/"+str(page))
    soup = BeautifulSoup(response.text, "html.parser")
    avg = 0
    sum = 0
    com = ["院會", "委員會"]

    # 抓人名
    names = soup.find_all(
        "span", {"class": "text-extra-bold text-line-height-wide"}, limit=1)
    
    for name in names:
        n1 = name.text
        if n1 == n:
            print("名字:",m)
        for attends in names:
            titles = soup.find_all(
                "div", {"class": "text-big-number -with-pa"}, limit=2)

        for i, title in enumerate(titles):
            y = str(title)
            x = re.findall("[0-9]+", y)
            for i in x:
                i = int(i)
                sum = sum+i
                avg = sum/2
        #print(n1,"3",avg)
        #returnAttend(m, "2", avg)
