#jieba 斷詞+詞頻
#coding:UTF-8<code>
import jieba
import re
from collections import Counter
import json
import csv
import codecs
import encodings

#jieba.set_dictionary('textanalysis\dict.txt')


# 輸入輸出文件訊息
origanword_file = 'C:\\Users\\Chihyu\\Desktop\\shcool\\project\\jieba\\test.txt'
stopword_file = 'C:\\Users\\Chihyu\\Desktop\\shcool\\project\\jieba\\stopwords.txt'
outputword_file = 'C:\\Users\\Chihyu\\Desktop\\shcool\\\project\\jieba\\sorted_words.csv'


# 按行讀取文件，返回文件的行字符串列表
def read_file(origanword_file):
    fp = codecs.open(origanword_file, 'rb',encoding="utf8",errors="ignore")
    content_lines = fp.readlines()
    fp.close()
    # 去除行末的換行符，否則會在停用詞匹配的過程中產生干擾
    for i in range(len(content_lines)):
        content_lines[i] = str(content_lines[i]).rstrip("\n")
        content_lines[i].encode('utf-8')
        print(content_lines[i])
    return content_lines


# 將content内容保存在對應的file_name文件
def save_file(outputword_file, content):
    fp = open(outputword_file,'wb',encodings='utf-8')
    fp.write(content)
    fp.write(codecs.BOM_UTF8)
    fp.close()


# 對短信中的用戶名前缀和内部的url鏈結進行過濾刪除
def regex_change(line):
    # 前缀的正则
    username_regex = re.compile(r"^\d+::")
    # URL，為了防止對中文的過滤，所以使用[a-zA-Z0-9]而不是\w
    url_regex = re.compile(r"""
        (https?://)?
        ([a-zA-Z0-9]+)
        (\.[a-zA-Z0-9]+)
        (\.[a-zA-Z0-9]+)*
        (/[a-zA-Z0-9]+)*
    """, re.VERBOSE | re.IGNORECASE)
    # 剔除日期
    data_regex = re.compile(u"""#utf-8编碼
        年 |
        月 |
        日 |
    """, re.VERBOSE)
    # 剔除所有数字
    decimal_regex = re.compile(r"[^a-zA-Z]\d+")
    # 剔除空格
    space_regex = re.compile(r"\s+")

    line = username_regex.sub(r"", line)
    line = url_regex.sub(r"", line)
    line = data_regex.sub(r"", line)
    line = decimal_regex.sub(r"", line)
    line = space_regex.sub(r"", line)

    return line


# 剔除停用词
def delete_stopwords(lines):
    stopwords = read_file(stopword_file)
    all_words = []

    for line in lines:
        all_words += [word for word in jieba.cut(line)
                      if word not in stopwords]


    dict_words = dict(Counter(all_words))

    return dict_words


# 主函數
if __name__ == "__main__":
    # 按行讀取文件
    lines = read_file(origanword_file)

    # 使用正則過滤
    for i in range(len(lines)):
        lines[i] = regex_change(lines[i])

    # 去除停用词，並返回詞袋字典
    bow_words = delete_stopwords(lines)

    # 對词袋字典进行排序
    sorted_bow = sorted(bow_words.items(), key=lambda d: d[1], reverse=True)

    # 将排序结果保存到json文件中
    with open(outputword_file, "w") as output_file:
        json.dump(sorted_bow, output_file, ensure_ascii=False)
    print("加載數據完成...")

    # 印出出現次數最高的100個數據，方便觀察
    for words in sorted_bow[:100]:
        print(str(words))
