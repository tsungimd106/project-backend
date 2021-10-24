# -*- coding: utf-8 -*-
from re import A, M
from model.db import DB
import xiangshi as xs
import jieba.analyse
import jieba
import csv

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

categoryA = ["財政金融", "教育", "內政", "司法及法制", "科技", "觀光", "國防", "食品安全", "長期照顧", "衛生社福", "農業", "交通", "海洋", "性別平等", "動物保育", "原住民", "外交",
    "兩岸關係", "高齡化", "幼托育兒", "年改", "基礎建設", "拒毒品", "客家", "治安", "都市發展", "補助", "都市美化", "汽機車", "環保", "體育賽事", "勞工就業", "青年", "文創", "新住民"]

with open('C:\\Users\\Chihyu\\Desktop\\shcool\\project\\category.csv', newline='', encoding="utf-8", errors="ignore") as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    lines = list(rows)

# 分類與政見逐條比對
print(category)
for j in category["data"]:
    m = [j["name"]]
    #print('第1個元素:', j)
    # print(len(policy["data"])) #1679
    for i in policy["data"]:
        n = [i["content"].decode(encoding='utf-8', errors='ignore')]  # 政見
        s = i["content"]
        result = xs.cossim(m, n)

        if result > 0.4:
            #print("類別:", m)
            #print("政見:", n)
            print(n)

            # returnCategory(i["id"],j["id"])
        else:
            print("ELSE==================")
            for row in lines:
                print(row)
                if lines[0] == policy["data"]:
                    returnCategory(i["id"], categoryA(rows[1])+1)

                else:
                    exit
