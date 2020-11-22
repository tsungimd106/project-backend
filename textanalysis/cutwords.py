#encoding=utf-8
import jieba
import re
from collections import Counter

jieba.set_dictionary('textanalysis\dict.txt')

stopword_file = 'C:\\Users\\Chihyu\\Desktop\\shcool\\project\\jieba\\stopwords.txt'

sentence = "1.四年內完成設計發包三大輕軌動線竹科環狀輕軌竹東到竹科輕軌竹北到竹科輕軌。2.四年內完成，四大機車風廊建置，竹林大橋，頭前溪橋，中正大橋，竹東大橋，讓機車族安全回家。3.四年內，建置150個ubike站，讓外地人騎車到市場吃特色美食，深入地方風景。4.任內，送出1000名青年，到美國唸國際碩士，80%學貸，讓年輕人加強競爭力，以資訊管理為例，到國外唸雲計算，量子電腦，物聯網，增加國際視野，也學好英文。5. 統籌200項，地方特色產品，銜接亞馬遜網站，國際記者會，電商上架銷售，把10年的農特產，一次賣光。6.任內，協調政府，完成100件，中小企業貸款與補助，引進郭台銘企業創投，協助青年創業，創立品牌。7.結合工研院中科院清交大矽谷德國日本歐美印度等500位專家企業，籌組竹科產發改造小組，延伸下一代竹科產業。8.爆肝繳稅不公平，爭取竹科工程師，助理技術員，租稅正義公平。9.食品太危險，人容易生病早死，任內每年4次定期委託食品研究所抽驗。10.推動郭台銘政策，0到6歲國家養，退休後國家養，父母跟長輩不要太擔心。11.任內修正動保法，虐貓虐狗的，處以重重刑，貓狗真心陪伴，也是我們的家人。孩子徬徨，大人擔憂，老人臉上沒有笑容，這不是我們要的社會，我們親民黨做事100分選舉0分，這次讓我們找回會做事的親民黨，讓我們為您服務，找回新竹居民的幸福感。"
print("Input：", sentence)
words = jieba.cut(sentence, cut_all=False)
print("Output 精確模式 Full Mode：")
for word in words:
    print(word)


# 按行讀取文件，返回文件的行字符串列表
def read_file(sentence):
    fp = open(sentence, "rb")
    content_lines = fp.sentence()
    fp.close()
    # 去除行末的換行符，否則會在停用詞匹配的過程中產生干擾
    for i in range(len(content_lines)):
        
        content_lines[i] = str(content_lines[i]).rstrip("\n")
        print(content_lines[i])
    return content_lines



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
    data_regex = re.compile(u"""        #utf-8编码
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
    lines = sentence

    # 對词袋字典进行排序
    sorted_bow = sorted(sentence, key=lambda d: d[0], reverse=True)

    # 去除停用词，並返回詞袋字典
    #bow_words = delete_stopwords(lines)

    # 将排序结果保存到json文件中
    print("加載數據完成...")

    # 印出出現次數最高的100個數據，方便觀察
    for sentence in sorted_bow[:30]:
        print(str(sentence))