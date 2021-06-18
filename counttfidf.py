#斷詞+算tf-idf
#encoding=utf-8
import jieba
import jieba.analyse
from jieba.analyse import extract_tags
# 提案doc url轉成文字存回資料庫欄位
# 抓資料庫提案欄位
f = open("C:\\Users\\110501\\Desktop\\proposal\\100311_00088.txt", "r",encoding="utf-8").read()
print(f)
# news = '本院民眾黨黨團，有鑑於我國近年來於太空科學研究、太空產業發展進步迅速，國際社會亦逐漸將外太空發展視為經濟、科技及軍事發展之嶄新競爭場域。為推動我國太空產業發展、培育及招募相關人才，亟須建立相關規範及完善法制，並明確太空產業發展業務之權責主導機關；爰此，擬具「太空發展法草案」。是否有當？敬請公決。'
tags = jieba.analyse.extract_tags(f, topK=5, withWeight=True)
stopwords = ['stopwords.txt']
break_words=[]
for j in f:
    break_words.append(j)
for word in open ('stopwords.txt','r',encoding="utf-8",errors='ignore'):
    stopwords.append(word.strip())
del_stopwords=[]
for k in break_words:
    if k not in stopwords:
        del_stopwords.append(k)
for sentence in f:
    seg_list = jieba.lcut(sentence)
#seg_list = jieba.lcut(sentence)
#print(seg_list)
for tag in tags:
    print('word:', tag[0], 'tf-idf:', tag[1])

#取前面前五個就好
