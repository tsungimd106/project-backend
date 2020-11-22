#斷詞+算tf-idf
#encoding=utf-8
import jieba
import jieba.analyse

#蔡適應政見(交通)
news = '持續推進交通優化：持續爭取快捷公車新路線；督促城際轉運站工程進度；爭取國道一號拓寬。'
tags = jieba.analyse.extract_tags(news, topK=30, withWeight=True)


for sentence in news:
    seg_list = jieba.lcut(sentence, cut_all=True)
seg_list = jieba.lcut(news)
print(seg_list)
for tag in tags:
    print('word:', tag[0], 'tf-idf:', tag[1])

