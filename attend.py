# -*- coding: UTF-8 -*-
import requests
from model.db import DB
import statistics
import numpy as np
from bs4 import BeautifulSoup
import re

def findFigure():
    sqlstr = "select id,name from politician"
    return DB.execution(DB.select, sqlstr)

def returnAttend(name):
    sqlstr = "insert into attendance(id,attend) VALUES (%s,%s)" % (
        name,avg)
    return DB.execution(DB.create, sqlstr)
    

for page in range(1, 407):
    response = requests.get(
        "https://ccw.org.tw/assess/34/legislator/"+str(page))
    soup = BeautifulSoup(response.text, "html.parser")
    avg = 0
    sum = 0
    com = ["院會", "委員會"]

    # 抓人名
    names = soup.find_all(
        "span", {"class": "text-extra-bold text-line-height-wide"}, limit=1)
    for name in names:
        print("名字:", name.text)
    for attends in names:
        titles = soup.find_all(
            "div", {"class": "text-big-number -with-pa"}, limit=2)
    
        #for title in titles:
        for i, title in enumerate(titles):
            print(com[i]+title.text)
            y = str(title)
            x = re.findall("[0-9]+", y)
            for i in x:
                i = int(i)
                sum = sum+i
                avg = sum/2

    #print("總分:", sum)
    print("平均分數",avg)

