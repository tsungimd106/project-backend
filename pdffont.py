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
    sqlstr = "select id,pdfUrl from proposal"
    return DB.execution(DB.select, sqlstr)
content = findPdfurl()
print(len(content["data"]))

pdfdb = findPdfurl()
#讀取成文字後存回資料庫
def returnPdfcontent(content):
    sqlstr = "insert into proposal (content) VALUES (%s)" % (
        content)
    return DB.execution(DB.create, sqlstr)

for j in pdfdb["data"]:
    rq = requests.get(j["pdfUrl"])
    pdf = pdfplumber.load(BytesIO(rq.content))
    for i in range(len(pdf.pages)):
        #print(i)
        page = pdf.pages[1]
        text = page.extract_text()
        print(text)

    tags = jieba.analyse.extract_tags(text, topK=5, withWeight=True,allowPOS=('n','a','an','nr','ns','nt','nz'))
    stopwords = ['stopwords.txt']
    break_words=[]
    for j in text:
        break_words.append(j)
    for word in open ('stopwords.txt','r',encoding="utf-8",errors='ignore'):
        stopwords.append(word.strip())
    del_stopwords=[]
    for k in break_words:
        if k not in stopwords:
            del_stopwords.append(k)
    for sentence in text:
        seg_list = jieba.lcut(sentence)
    #seg_list = jieba.lcut(sentence)    
    #print(seg_list)
    for tag in tags:
        print('word:', tag[0], 'tf-idf:', tag[1])


        #returnPdfcontent(text)
    #讀取文字
   #text=p0.extract_text()
    #print (text)

