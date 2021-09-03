# 留言正負向分析
# -*- coding: utf-8 -*-
from model.db import DB
from snownlp import SnowNLP
from snownlp import sentiment

# 從資料庫裡抓取提案


'''def findMessage(id):
    sqlstr = "select id,content from message"
    return DB.execution(DB.select, sqlstr)


data = findMessage(14)
print(data)'''

l=["這不錯優","為甚麼提案可以審過","不對ㄟ","這提案好奇怪","這個提案根本不好","我好喜歡這篇提案","哈哈哈哈","HELLO WORLD","太強了"]

#保存情感极性值小于等于0.3的结果为负面情感结果
f1=open('neg.txt','w',encoding='utf-8')

#保存情感极性值大于0.3的结果为正面情感结果
f2=open('pos.txt','w',encoding='utf-8')

for j in l:
    s=SnowNLP(j)
    if s.sentiments <=0.4:
        f1.write(j+'\t'+str(s.sentiments)+'\n')
    else:
        f2.write(j + '\t' + str(s.sentiments) + '\n')
f1.close()
f2.close()