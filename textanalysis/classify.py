# coding:utf-8

import xiangshi as xs
f = open("C:\\Users\\chihyu\\Desktop\\shcool\\project\\code\\textanalysis\\titles.txt",
         "r", encoding="utf-8")
f = f.readlines()
Input1 = ['長照貼心 走入社區：廣佈各級長照據點，擴增服務項目，落實銀髮族照護。']

for j in range(len(f)):
    print('第', j+1, '個元素:', f[j], type(f[j]))
    temp=[f[j]]
    result = xs.cossim(temp, Input1)
    print(result)   


# 餘弦相似度0.190692517849
# 完全相似 1.0
