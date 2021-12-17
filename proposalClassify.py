# -*- coding: utf-8 -*-
from text2vec import SBert
from sentence_transformers.util import semantic_search
from sentence_transformers import SentenceTransformer
from configparser import ParsingError
from re import A, M
from model.db import DB
import xiangshi as xs
import jieba.analyse
import jieba
import csv
import sys
sys.path.append('..')
 
 
# 提案分類
# 從資料庫裡抓取提案標題
def findProposal():
    sqlstr = "select id,title from proposal"
    return DB.execution(DB.select, sqlstr)
 
 
# 從資料庫裡抓取類別
def findCategory():
    sqlstr = "select id,name from category"
    return DB.execution(DB.select, sqlstr)
 
 
# 將所屬類別存回資料庫
def returnproCategory(propsoal_id, category_id):
    sqlstr = "insert into proposal_category (propsoal_id, category_id) VALUES (%s, %s)" % (
        propsoal_id, category_id)
    return DB.execution(DB.create, sqlstr)
 
# 待匯入完畢後跑迴圈
proposal = findProposal()
category = findCategory()
 
for j in category["data"]:
    m = [j["name"]]
    for i in proposal["data"]:  
        stopwords= i["title"].decode().strip('，請審議案。') #標題去掉請審議案
        n = [stopwords]
        result = xs.cossim(j, n)
        if result > 0.4:
            returnproCategory((int(i["id"]),j["id"]))
        else:
            embedder = SBert()
            corpus_embeddings = embedder.encode(n)
            query_embedding = embedder.encode(j)
            hits = semantic_search(query_embedding, corpus_embeddings)
            hits = hits[0]
            for hit in hits:
                if hit['score']>0.4:
                    returnproCategory(int(i["id"]),j["id"])

