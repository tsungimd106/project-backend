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
    sqlstr = "insert into message(user_id,content,proposal_id,parent_id) values(\"%s\",\"%s\",\"%s\",\"%s\");" % (
        account, mes, article_id, parent_id)
    return DB.execution(DB.create, sqlstr)


def vote(userid, sp_id, proposal_id):
    sqlstr = "insert into user_proposal(user_id,stand_id,proposal_id) values(\"%s\",\"%s\",\"%s\")" % (
        userid, sp_id, proposal_id)
    return DB.execution(DB.create, sqlstr)


def old_msgList(proposal_id):
    sqlstr = "select * from message where proposal_id=\"%s\"" % (proposal_id)
    return DB.execution(DB.select, sqlstr)


def msgList(proposal_id, user_id):
    sqlstr = [
        {"sql": "select * from message where proposal_id=\"%s\"" %
            (proposal_id), "name": "msg"},
        {"sql": "select * from proposal where id=\"%s\"" %
            (proposal_id), "name": "detail"},
        {"sql": "select * from favorite where user_id=\"%s\" and proposal_id=\"%s\"" %
         (proposal_id, user_id), "name": "heart"},
    ]
    return DB.execution(DB.select, sqlstr)


def msgListByUser(user_id):
    sqlstr = "select m.*,p.title from message as m join proposal as p on m.proposal_id = p.id where user_id=\"%s\";" % (
        user_id)
    return DB.execution(DB.select, sqlstr)


def getSave(user_id):
    sqlstr = ("select * from favorite as f join proposal as p on f.proposal_id=p.id join status as s on p.status_id=s.id where user_id=\"%s\"" % user_id)
    return DB.execution(DB.select, sqlstr)


def save(user_id, proposal_id):
    sqlstr = ("insert into favorite( user_id,proposal_id) values(\"%s\",\"%s\");" %
              (user_id, proposal_id))
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)


def report(user_id, message_id, remark, rule):
    sql_Remark = ""
    for i in rule:
        sql_Remark += "insert into `report_rule`(`report_id`,`rule_id`) values(@v_report_id,%s);" % i
    sqlstr = (
        "    set @v_report_id = 0;call db.report(\"%s\", %s, \"%s\", @v_report_id);"+sql_Remark) % (user_id, message_id, remark)

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
        {"sql":  "select term as name from proposal group by term;", "name": "屆別"},
        {"sql": "select s.status as name from proposal as p join status as s on p.status_id=s.id group by status_id;", "name": "狀態"}
    ]
    return DB.execution(DB.select, sqlstr)
