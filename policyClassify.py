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
 
 
# 待匯入完畢後跑迴圈
policy = findPolicy()
category = findCategory()
 
 
# 分類與政見逐條比對
for j in category["data"]:
    m = [j["name"]]
    
    for i in policy["data"]:
        n = [i["content"].decode(encoding='utf-8', errors='ignore')]  # 政見
        result = xs.cossim(m, n)
 
        if result > 0.4:
            returnCategory(i["id"],j["id"])
        else:
            embedder = SBert()
            corpus_embeddings = embedder.encode(n)
            query_embedding = embedder.encode(m)
            hits = semantic_search(query_embedding, corpus_embeddings)
            hits = hits[0]
            for hit in hits:
                if hit['score']>0.4:
                    returnCategory(i["id"],j["id"])
       
 

