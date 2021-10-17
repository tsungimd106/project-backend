# -*- coding:utf-8
import csv
import jieba
import jieba.analyse
import re

# jieba.set_dictionary('dict.txt.big.txt')

jieba.load_userdict('user_dict.txt')

with open('C:\\Users\\Chihyu\\Downloads\\jieba-20210924T064633Z-001\\jieba\\train_test.csv', 'r', encoding='utf-8-sig') as file:
    #資料集路徑
    file_object2 = file.read().split('\n')

Rs2 = []  # 建立存儲分词的列表
print(len(file_object2))  # 1767筆政見

# 第一個引數：待提取關鍵詞的文字
# 第二個引數：返回關鍵詞的數量，重要性從高到低排序
# 第三個引數：是否同時返回每個關鍵詞的權重
# 第四個引數：詞性過濾，為空表示不過濾，若提供則僅返回符合詞性要求的關鍵詞


for i in range(len(file_object2)):
    result = []
    r4 = "\【.*?】+|\-《.*?》+|；\#.*?#+|[.!/_,$&%^*()<>+""'?@|:~{}#]+|[——！\，。=？、：“”‘’￥……()「」《》【】]"
    sentence = re.sub(r4, '', file_object2[i])
    print(sentence)
    seg_list = jieba.cut(sentence)
    for w in seg_list:  # 讀取每一行分詞
        result.append(w)
        # print(result)
    Rs2.append(result)  # 將該行分詞寫入列表形式的總分詞列表

# 寫入CSV
with open('C:\\Users\\chihyu\\Desktop\\result15.csv', 'a+', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)  # 定義寫入格式為csv
    writer.writerows(Rs2)  # 按行寫入
    file.close()
