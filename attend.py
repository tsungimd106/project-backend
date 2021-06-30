# -*- coding: UTF-8 -*-
import requests
import statistics
import numpy as np
from bs4 import BeautifulSoup
import re

for page in range(1, 407):
    response = requests.get(
        "https://ccw.org.tw/assess/34/legislator/"+str(page))
    soup = BeautifulSoup(response.text, "html.parser")
    # 抓人名
    sum = 0
    # print(soup.prettify())
    names = soup.find_all(
        "span", {"class": "text-extra-bold text-line-height-wide"})
    print(names)
    for attends in names:
        titles = soup.find_all(
            "div", {"class": "text-big-number -with-pa"}, limit=2)
        for title in titles:
            print("出席分數:", title.text)
            y = str(title)
            x = re.findall("[0-9]+", y)
            for i in x:
                i = int(i)
                sum = (sum+i)/i
        print(sum)
        # if len(titles)==2:
        #s = sum(int(title.text))
        # print(s)

    # 計算平均
    '''if len(titles) == 2:
        #print(titles[0].text,titles[1].text)
        listA =[titles[0].text,titles[1].text]
        means = statistics.mean(str(listA))
        print(means)'''
