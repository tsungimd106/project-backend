# -*- coding:utf-8 -*-
from model.db import DB
import xiangshi as xs

#category = ['財政金融', '教育', '內政', '司法及法制', '科技', '文化', '食品安全', '外交國防',
            #'長期照顧', '衛生社福', '農業', '交通', '海洋', '性別平等', '動物保育', '社會福利及衛生環境', '環境', '勞工權益']

#從資料庫裡抓取政見
def findPolicy(politicianId):
    sqlstr = "select id,content from policy where politician_id=\"%s\"" % politicianId
    return DB.execution(DB.select, sqlstr)
def findCategory(category_id):
    sqlstr = "select id,name from category where id=\"%s\"" % id
    return DB.execution(DB.select, sqlstr)

#待匯入完畢後跑迴圈
data = findPolicy(399)
category = findCategory()

#分類與政見逐條比對
for i in range(len(category)):
    temp = [category[i]]
    print('第', i+1, '個元素:', category[i])
    for j in data:
        dataList = []
        d = data
        dataList.append(j["content"])
        s=j["content"].decode(encoding='utf-8', errors='ignore')
        print(s) 
        result = xs.cossim(temp, [s])

        print(result)

        num = int(result)
        if num > 0:
            returnCategory()

# 將所屬類別存回資料庫
def returnCategory(policy_id, category_id):
        sqlstr = "insert into policy_category (policy_id, category_id) VALUES (%s, %s)" %  (
        policy_id, category_id)
        return DB.execution(DB.select, sqlstr)