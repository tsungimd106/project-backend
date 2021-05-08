# -*- coding:utf-8 -*-
from model.db import DB
import jieba
import re


def findPolitican():
    sqlstr = "select policy,id from politician"
    return DB.execution(DB.select, sqlstr)


def cut_sentences(content):

    # 结束符号，包含中文和英文的
    end_flag = ['?', '!', '.', '？', '！', '。', '…']

    content_len = len(content)
    sentences = []
    tmp_char = ''
    for idx, char in enumerate(content):
        # 拼接字符
        tmp_char += char

        # 判斷是否已经到了最後一位
        if (idx + 1) == content_len:
            sentences.append(tmp_char)
            break

        # 判斷是否為結束符號
        if char in end_flag:
            # 再判斷下一個字符是否為結束符號，若是不是結束符號，則切分句子
            next_idx = idx + 1
            if not content[next_idx] in end_flag:                
                if len(tmp_char) > 3:
                    sentences.append(tmp_char)
            tmp_char = ''

    return sentences


def returnPolicy(iid, stt):
    sqlstr = "insert into policy (politician_id,content) VALUES (%s,\"%s\")" % (
        iid, stt)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)


content = findPolitican()
print(len(content["data"]))

for j in content["data"]:

    sentences = cut_sentences(str(j["policy"], encoding='utf-8'))
    print(len(sentences))
    for jj in sentences:
        returnPolicy(j["id"],jj)

    #  print('\n\n'.join(sentences))
