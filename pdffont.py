# -*-coding:utf8-*-
from operator import index, indexOf
from typing import Text
from model.db import DB
import pandas as pd
import pdfplumber
import requests
from io import BytesIO
import jieba
import jieba.analyse
from jieba.analyse import extract_tags

# 從資料庫裡抓取pdf連結

def findPdfurl():
    sqlstr = "select id,pdfUrl,term,session_Period,session_Time from proposal where term ='10'"
    return DB.execution(DB.select, sqlstr)
def getColName(table):
    if not isinstance(table[0],str):
        return getColName(table[0])
    else: 
        # print(table[0])
        return table[0]


#找輸出的hashtag編號
def findHash(hashtag):
    sqlstr = "select id from hashtag"
    return DB.execution(DB.select, sqlstr)

#傳回proposal_category
def returnProtag(proposal_id,hashtag):
    # 1. 傳入hashtag 的文字，在資料庫寫sp or function新增(之後系統放新資料也可以用)
    sqlstr1="call your_func_or_sp_name(\"%s\",\"%s\")"%(proposal_id,hashtag)

content = findPdfurl()
pdfdb = findPdfurl()
print(len(content["data"]))

#讀取成文字後存回資料庫
def returnPdfcontent(content):
    sqlstr = "insert into proposal (content) VALUES (%s)" % (
        content)
    return DB.execution(DB.create, sqlstr)

def returnHashtag(hashtags):
    for tag in hashtags:
        print("insert into hashtag (hashtag_name) VALUES ('%s')" % (
        tag[0]))

def returnText(proposal):
    for texts in proposal:
        print( "update proposal set content =\"%s\"" % (
        text))
        
       
    


for j in pdfdb["data"]:
    rq = requests.get(j["pdfUrl"])
    pdf = pdfplumber.load(BytesIO(rq.content))
    allText=""
    for i in pdf.pages:
        allText+=str(i.extract_text())
    # print(allText)
    text=""
    table=""
    for i in pdf.pages:
        content=i.extract_table()
        if content!=None:
            table=str(getColName(content))
            break

    
    # page = pdf.pages[1]
    # text = page.extract_text()
    # print(allText)
    try:
        ind=allText.index("說明")
        # print(ind) 
        end=allText.index(table)
        # print(end) 
        text=allText[ind:end]
        print(text)
        
    except:
        print("eror")
        ind=allText.index("案由")
        #print(ind) 
        end=allText.index("提案人")
        #print(end)
        text=allText[ind:end]
        print(text)
    print()
    #returnText(text)
    #str1 = text
    #str2 = "草案總說明"
    #print (str1.index(str2)) 
    #自訂詞語庫
    jieba.load_userdict('C:\\Users\\110501\\Desktop\\backend\\project-backend-from Chihyu\\dict.txt')
    #停用詞定義
    jieba.analyse.set_stop_words("C:\\Users\\110501\\Desktop\\backend\\project-backend-from Chihyu\\stopwords.txt")
    #開始斷詞
    tags = jieba.analyse.extract_tags(text, topK=3, withWeight=True,allowPOS=())
    print(tags)
    #取前三個詞

    #for tag in tags:
        #print('word:', tag[0], 'tf-idf:', tag[1])
    #hashtag=tag[0]
    #returnHashtag(tags)
  
    

    #returnPdfcontent(text)

