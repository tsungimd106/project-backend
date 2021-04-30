from model.db import DB
import json


def list(data):
    strCond = ""
    if (isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s =\"%s\" and" % (i, data[i])
    sqlstr = "select * from proposal  %s" % (
        "where " + strCond[0:len(strCond)-3] if len(strCond) > 0 else "")
    return (DB.execution(DB.select, sqlstr))


def change(data, id):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" ," % (i, data[i])
    sqlstr = "update proposal set %s where id=\"%s\"" % (
        strCond[0:len(strCond)-1], id)
    print(sqlstr)
    return DB.execution(DB.update, sqlstr)


def msg(account, mes, article_id, parent_id):
    sqlstr = "insert into message(user_id,content,proposal_id,parent_id) values(\"%s\",\"%s\",\"%s\",\"%s\")" % (
        account, mes, article_id, parent_id)
    return DB.execution(DB.create, sqlstr)


def vote(userid, sp_id, proposal_id):
    sqlstr = "insert into user_proposal(user_id,stand_id,proposal_id) values(\"%s\",\"%s\",\"%s\")" % (
        userid, sp_id, proposal_id)
    return DB.execution(DB.create, sqlstr)


def msgList(proposal_id):
    sqlstr = "select * from message where proposal_id=\"%s\"" % (proposal_id)
    return DB.execution(DB.select, sqlstr)
