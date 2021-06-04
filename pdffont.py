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
    sqlstr = "select id,pdfUrl from proposal where term ='10'"
    return DB.execution(DB.select, sqlstr)
def getColName(table):
    if not isinstance(table[0],str):
        return getColName(table[0])
    else: 
        # print(table[0])
        return table[0]
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
        print(ind) 
        end=allText.index("提案人")
        print(end)
        text=allText[ind:end]
        print(text)
    print()
    #str1 = text
    #str2 = "草案總說明"
    #print (str1.index(str2)) 
    #開始斷詞
    tags = jieba.analyse.extract_tags(text, topK=3, withWeight=True,allowPOS=('n','a','an','nr','ns','nt','nz'))
    #取前三個詞
    #詞性篩選:名詞、形容詞、名形詞、人名、地名、機構團體、其他專有名詞
    stopwords = ['stopwords.txt']
    break_words=[]
    #去除停用詞
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

