# -*- coding: utf-8 -*-
from re import M
from model.db import DB
import xiangshi as xs
import jieba.analyse
import jieba

# 政見分類
# 從資料庫裡抓取政見


def findPolicy():
    sqlstr = "select id,content from policy"
    return DB.execution(DB.select, sqlstr)

# 從資料庫裡抓取類別


def findCategory():
    sqlstr = "select id,name from category"
    return DB.execution(DB.select, sqlstr)


# 將所屬類別存回資料庫
def returnCategory(policy_id, category_id):
    sqlstr = "insert into policy_category (policy_id, category_id) VALUES (%s, %s)" % (
        policy_id, category_id)
    return DB.execution(DB.create, sqlstr)


# 待匯入完畢後跑迴圈
policy = findPolicy()
category = findCategory()

'''sentence = category["data"]
keywords = jieba.analyse.extract_tags(
    sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
print(keywords)'''

# 分類與政見逐條比對
print(category)
for j in category["data"]:
    m = [j["name"]]
    #print('第1個元素:', j)
    for i in policy["data"]:
        n = [i["content"].decode(encoding='utf-8', errors='ignore')]  # 政見
        s = i["content"]

        result = xs.cossim(m, n)

        if result > 0.5:
            #print("類別:", m)
            #print("政見:", n)
            #print(result>0.1)
            #print("結果", result)
            print(n)

            # returnCategory(i["id"],j["id"])
    
