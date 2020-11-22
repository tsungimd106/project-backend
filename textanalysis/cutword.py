import jieba


def gettext():
    #開啟檔案
    text=open('C:\\Users\\Chihyu\\Desktop\\shcool\\project\\jieba\\cutword.txt',"r",encoding='utf-8').read()
    text=text.lower()
    #將特殊符號全部換成空格
    for ch in '!"#$%^&*()+_-，.。/:;<>?@[]{}\|~':
        text=text.replace(ch,"")
    return text

hamlettxt=gettext()
#將字串按空格分割成列表
words=hamlettxt.split()
counts={}
#以字典形式統計每個單詞的出現次數
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
#將列表按從大到小排序
items.sort(key=lambda x:x[1],reverse=True)
for i in range(50):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))