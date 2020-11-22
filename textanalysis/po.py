# encoding=utf-8
import jieba
import jieba.analyse

jieba.load_userdict('C:\\Users\\Chihyu\\Desktop\\shcool\\project\\code\\project-backend-origin\\textanalysis\\userdict.txt')
#黃昭順政見
politics = ['全力捍衛中華民國主權，堅決反對一國兩制','年金改革嚴重違反信賴保護原則，將繼續在立法院爭取修法，還給退休軍公教警消海巡公平與正義。',
'剪除紊亂政府體制、自稱「東廠」、「西廠」之惡劣政務官。','恢復特偵組，徹查「慶富案」等重大弊案。','督促政府推動四維八德的品德教育，灌輸學生正確的人倫綱常']
tags = jieba.analyse.extract_tags(politics, topK=5, withWeight=True)

# 第一條政見
for sentence in politics:
    seg_list = jieba.lcut(sentence, cut_all=True)
seg_list = jieba.lcut(politics)
print(seg_list)
for tag in tags:
    print('word:', tag[0], 'tf-idf:', tag[1])

