import requests
from model.db import DB
import json

def returnTitle(lateestnewsTitle, createDate):
    sqlstr = "insert into article (title, createTime) VALUES (%s, %s)" % (
        lateestnewsTitle, createDate)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)


f = open('lastestnews.json','r',encoding='utf-8')
data = json.load(f)

for i in data:
    returnTitle(i['title'], i['createDateStr'])