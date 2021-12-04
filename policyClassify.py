# -*- coding: utf-8 -*-
from re import A, M
from model.db import DB
import xiangshi as xs
import jieba.analyse
import jieba
import csv
import sys
sys.path.append('..')
import text2vec
from text2vec import SBert
from sentence_transformers.util import cos_sim, semantic_search
 
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
 
#若第一階段餘弦相似度沒有篩選成功，實施第二階段餘弦相似度計算
def similarity():
    embedder = SBert()
    
    #政見文本
    for i in policy["data"]:
            corpus = list([i["content"].decode(encoding='utf-8', errors='ignore')])# 政見
           
    corpus_embeddings = embedder.encode(corpus)
 
    # Query sentences:
    queries = ["財政金融", "教育", "內政", "司法及法制", "科技", "觀光", "國防", "食品安全", "長期照顧", "衛生社福", "農業", "交通", "海洋", "性別平等", "動物保育", "原住民", "外交",
        "兩岸關係", "高齡化", "幼托育兒", "年改", "基礎建設", "拒毒品", "客家", "治安", "都市發展", "補助", "都市美化", "汽機車", "環保", "體育賽事", "勞工就業", "青年", "文創", "新住民"]
 
    for query in queries:
        query_embedding = embedder.encode(query)
        hits = semantic_search(query_embedding, corpus_embeddings)
        hits = hits[0]  # Get the hits for the first query
        for hit in hits:
            if hit['score']>0.4:
                print("Query:", query)
                print(corpus[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))
                returnCategory(i["id"],query)
 
 
# 待匯入完畢後跑迴圈
policy = findPolicy()
category = findCategory()
 
 
# 分類與政見逐條比對
for j in category["data"]:
    m = [j["name"]]
    #print('第1個元素:', j)
    # print(len(policy["data"])) #1679
    for i in policy["data"]:
        n = [i["content"].decode(encoding='utf-8', errors='ignore')]  # 政見
        result = xs.cossim(m, n)
 
        if result > 0.4:
            print("類別:", m)
            print("政見:", n)
            print("=========")
            returnCategory(i["id"],j["id"])
        else:
            embedder = SBert()
            corpus_embeddings = embedder.encode(n)
            query_embedding = embedder.encode(m)
            hits = semantic_search(query_embedding, corpus_embeddings)
            hits = hits[0]
            for hit in hits:
                if hit['score']>0.3:
                    print("Query:", m)
                    print(n[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))
                    returnCategory(i["id"],j["id"])
       
