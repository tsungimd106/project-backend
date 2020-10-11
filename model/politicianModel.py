from model.db import DB
import json


def findAll(data):
    strCond=""
    if (isinstance(data ,dict)):
        for i in data.keys():
            strCond+="%s =\"%s\" and" %(i,data[i])
    sqlstr = "select id,term,partyid from politician where %s" %(strCond[0:len(strCond)-3])
    return (DB.execution(DB.select, sqlstr))

def find(data):
    strCond=""
    if (isinstance(data ,dict)):
        for i in data.keys():
            strCond+="%s =\"%s\" and" %(i,data[i])
    sqlstr = "select * from politician  %s" %(strCond[0:len(strCond)-3])
    return (DB.execution(DB.select, sqlstr))


