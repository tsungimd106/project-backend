#-*- coding: utf-8 -*-
from model.db import DB
from snownlp import SnowNLP
from snownlp import sentiment
import json

# 從資料庫裡抓取提案

def findMessage():
    sqlstr = "select id,content from message"
    return DB.execution(DB.select, sqlstr)

def returnMessage(postive,iid):
    sqlstr = "update message set postive = %s where id=\"%s\"" % (
        postive,iid)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)

def stringToList(string):
    listRes = list(string.split(" "))
    return listRes

datas = findMessage()


#小於等於0.4的结果為負面情感結果
#f1=open('neg.txt','w',encoding='utf-8')

#大於0.4的結果為正面情感結果
#f2=open('pos.txt','w',encoding='utf-8')


for i in datas["data"]:
    a = str(i["content"], encoding='utf-8')
    stringToList(a)

    s=SnowNLP(a)
    if s.sentiments <=0.4:
        #f1.write(a+'\t'+str(s.sentiments)+'\n')
        returnMessage(s.sentiments,i["id"])
    else:
        #f2.write(a + '\t' + str(s.sentiments) + '\n')
        returnMessage(s.sentiments,i["id"])
                
#f1.close()
#f2.close()

