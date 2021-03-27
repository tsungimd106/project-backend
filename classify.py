# -*- coding:utf-8 -*-
from model.db import DB
import xiangshi as xs

#從資料庫裡抓取政見
def findPolicy():
    sqlstr = "select id,content from policy"
    return DB.execution(DB.select, sqlstr)

#從資料庫裡抓取類別
def findCategory():
    sqlstr = "select id,name from category"
    return DB.execution(DB.select, sqlstr)

#待匯入完畢後跑迴圈
data = findPolicy()
category = findCategory()

#分類與政見逐條比對
for j in category:
    m = [j["name"]] #類別
    print('第1個元素:', j)
    for i in data:
        n=[i["content"].decode(encoding='utf-8', errors='ignore')] #政見
        s=i["content"]
        print(n) 
        result = xs.cossim(m, n)
        print(result)

        num = int(result)
        if num > 0.4:
            returnCategory()

# 將所屬類別存回資料庫
def returnCategory(policy_id, category_id):
        sqlstr = "insert into policy_category (policy_id, category_id) VALUES (%s, %s)" %  (
        policy_id, category_id)
        return DB.execution(DB.select, sqlstr)