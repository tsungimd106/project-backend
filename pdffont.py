from model.db import DB
import pandas as pd
import pdfplumber
import requests
from io import BytesIO

# 從資料庫裡抓取pdf連結

def findPdfurl():
    sqlstr = "select id,pdfUrl from proposal"
    return DB.execution(DB.select, sqlstr)
content = findPdfurl()
print(len(content["data"]))

pdfdb = findPdfurl()


for j in pdfdb["data"]:
    rq = requests.get(j["pdfUrl"])
    pdf = pdfplumber.load(BytesIO(rq.content))
    for i in range(len(pdf.pages)):
        #print(i)
        page = pdf.pages[1]
        text = page.extract_text()
    #讀取文字
   #text=p0.extract_text()
    print(text)


def returnPdfcontent(content):
    sqlstr = "insert into proposal (content) VALUES (%s)" % (
        content)
    return DB.execution(DB.create, sqlstr)