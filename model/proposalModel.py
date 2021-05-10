from model.db import DB
import json


def list(data):
    strCond = ""
    if (isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s =\"%s\" and" % (i, data[i])
    sqlstr = "select p.*,s.status from proposal as p join `status`  as s on p.status_id=s.id %s limit 50" % (
        "where " + strCond[0:len(strCond)-3] if len(strCond) > 0 else "")
    print(sqlstr)
    return (DB.execution(DB.select, sqlstr))


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


def msgListByUser(user_id):
    sqlstr = "select * from message where user_id=\"%s\"" % (user_id)
    return DB.execution(DB.select, sqlstr)


def getSave(user_id):
    sqlstr = ("select * from favorite as f join proposal as p on f.proposal_id=p.id join status as s on p.status_id=s.id where user_id=\"%s\"" % user_id)
    return DB.execution(DB.select, sqlstr)


def save(user_id, proposal_id):
    sqlstr = ("insert into favorite( user_id,proposal_id) values(%s,%s)" %
              user_id, proposal_id)
    return DB.execution(DB.create, sqlstr)


def report(user_id, rule_id, message_id, remark):
    sqlstr = ("insert into report(user_id,rule_id,message_id,remark) values(%s,%s,%s,%s)" % (
        user_id, rule_id, message_id, remark))
    return DB.execution(DB.create, sqlstr)


def rule():
    sqlstr = "select * from rule"
    return DB.execution(DB.select, sqlstr)


def change(data, id):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" ," % (i, data[i])
    sqlstr = "update proposal set %s where id=\"%s\"" % (
        strCond[0:len(strCond)-1], id)
    print(sqlstr)
    return DB.execution(DB.update, sqlstr)


def getCond():
    sqlstr = [
      {"sql":  "select term as name from proposal group by term;","name":"屆別"},
        {"sql":"select s.status as name from proposal as p join status as s on p.status_id=s.id group by status_id;","name":"狀態"}
    ]
    return DB.execution(DB.select, sqlstr)
