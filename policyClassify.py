# -*- coding: utf-8 -*-
from re import A, M
from model.db import DB
import xiangshi as xs
import jieba.analyse
import jieba
import csv
import sys
sys.path.append('..')
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
 
    # Corpus with example sentences
    #政見文本
    '''corpus = [
        '推動原住民族基本權利入法，使原住民享有政治、經濟、教育、文化、狩獵、土地、醫療、傳播及社會福利之完整權益',
        '支持政府推動務實穩健、和睦友善之大陸政策，維護九二共識，使台灣安全，人民有錢，促進兩岸和平發展及民族團結。',
        '繼續推動原住民族自治法、反族群歧視法、礦業法、土地及海域法、野生動物保育法修正，使原住民享有命運自決之權利。',
        '解決全國原住民就學、就業、住宅問題，保障原住民工作權。並推動全國原鄉住宅，取得合法建照',
        '監督政府專案編列預算，加強原住民地區農路、堤防、護岸、橋樑及治山防洪之基礎建設工程，保障原住民族生命、財產及部落安全',
        '因應全球氣候變遷，大幅提高原住民地區禁伐補償及造林補助，推動原住民土地受限補償，保障原住民生存權',
        '政府應重視原住民文化創意產業，專案補助原住民電影、電視、歌舞、服飾及文創人才，以維護發揚原住民歷史、文化，有效保存物質和非物質文化遺產',
        '提昇原鄉學校老師薪資加給，保障原民生之加分制度、提昇族語師資待遇，改善原鄉地區學校教學環境與體育設施',
        '加強原住民地區文健站服務功能，提昇照服員薪資，加強照顧老人安養。對於貧困弱勢的原住民家庭，應予專案補助',
        '要求教育部應制訂尊重原住民為台灣歷史主人的教綱與課程，創立原住民大學、廣設原住民族教育資源中心',
        '六：國防自主，守護台灣，帶動國防產業發展。',
        '台灣優先 富樂嘉義 平民參政']'''
    for i in policy["data"]:
            corpus = list([i["content"].decode(encoding='utf-8', errors='ignore')])# 政見
           
    corpus_embeddings = embedder.encode(corpus)
 
    # Query sentences:
    queries = ["財政金融", "教育", "內政", "司法及法制", "科技", "觀光", "國防", "食品安全", "長期照顧", "衛生社福", "農業", "交通", "海洋", "性別平等", "動物保育", "原住民", "外交",
        "兩岸關係", "高齡化", "幼托育兒", "年改", "基礎建設", "拒毒品", "客家", "治安", "都市發展", "補助", "都市美化", "汽機車", "環保", "體育賽事", "勞工就業", "青年", "文創", "新住民"]
 
    for query in queries:
        query_embedding = embedder.encode(query)
        hits = semantic_search(query_embedding, corpus_embeddings, top_k=3)
        hits = hits[0]  # Get the hits for the first query
        for hit in hits:
            if hit['score']>0.35:
                print("Query:", query)
                print(corpus[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))
 
 
# 待匯入完畢後跑迴圈
policy = findPolicy()
category = findCategory()
 
categoryA = ["財政金融", "教育", "內政", "司法及法制", "科技", "觀光", "國防", "食品安全", "長期照顧", "衛生社福", "農業", "交通", "海洋", "性別平等", "動物保育", "原住民", "外交",
    "兩岸關係", "高齡化", "幼托育兒", "年改", "基礎建設", "拒毒品", "客家", "治安", "都市發展", "補助", "都市美化", "汽機車", "環保", "體育賽事", "勞工就業", "青年", "文創", "新住民"]
 
 
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
            similarity()
            #returnCategory(i["id"],j["id"])
       
