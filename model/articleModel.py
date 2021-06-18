from model.db import DB
import json


def getArticle(type):
    sqlstr = "select * from article where =%s" % type
    return DB.execution(DB.select, sqlstr)


def change(data, id):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" ," % (i, data[i])
    sqlstr = "update article set %s where id=\"%s\"" % (
        strCond[0:len(strCond)-1], id)
    print(sqlstr)
    return DB.execution(DB.update, sqlstr)
