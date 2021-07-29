from model.db import DB
import json


def login(account, password):
    sqlstr = "select * from user where id=\"%s\" and password = md5(\"%s\")" % (
        account, password)
    return (DB.execution(DB.select, sqlstr))


def findPasswordByAccount(account):
    sqlstr = "select password from user where id=\"%s\"" % account
    return DB.execution(DB.select, sqlstr)


def changePassword(account, password):
    sqlstr = "update user set password = \"%s\" where id = \"%s\"" % (
        password, account)
    return DB.execution(DB.update, sqlstr)


def sign(account, password, age, sex, area, name):
    sqlstr = "insert into user(id, password,age,gender,area_id,name) VALUES (\"%s\", \"%s\" ,\"%s\" ,\"%s\",\"%s\",\"%s\")" % (
        account, password, age, sex, area, name)
    print(sqlstr)
    return DB.execution(DB.create, sqlstr)


def changeProfile(data, account):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" ," % (i, data[i])
    sqlstr = "update user set %s where id=\"%s\"" % (
        strCond[0:len(strCond)-1], account)
    print(sqlstr)
    return DB.execution(DB.update, sqlstr)


def findArea(area):
    sqlstr = "select * from area "
    return DB.execution(DB.select, sqlstr)


def findUserarea(area):
    sqlstr = "select area from user where id = \"%s\"" % (
        area)
    return DB.execution(DB.select, sqlstr)


def hasUser(userid):
    sqlstr = "select count(*) from user where id=\"%s\"" % (userid)
    return DB.execution(DB.select, sqlstr)


def user(user_id):
    sqlstr = [
        {"sql": "SELECT u.id,u.name,nick_name,degree,a.name as a_n ,gender,birthday FROM db.user as u join area as a on u.area_id=a.id where u.id=\"%s\"" %
         user_id, "name": "user"},
        {"sql": "select * from area", "name": "area"},
        {
            "sql": ("select * from favorite as f join proposal as p on f.proposal_id=p.id join status as s on p.status_id=s.id where user_id=\"%s\"" % user_id),
            "name": "save"},
        {
            "sql": "select m.*,p.title from message as m join proposal as p on m.proposal_id = p.id where user_id=\"%s\"" % (
                user_id), "name": "msg"
        }, {"sql": "select * from user_policy where user_id =\"%s\"" % user_id, "name": "policy_vote"},
        {"sql": "select user_id,p.*,s.type from user_proposal as up  join stand as s on up.stand_id=s.id join proposal as p on up.proposal_id=p.id group by p.id where user_id =\"%s\"" % user_id, "name": "proposal_vote"}]
    return DB.execution(DB.select, sqlstr)

def getUserIdByLine(line_id):
    sqlstr="select id from user where line=\"%s\""%line_id
    
    data=DB.execution(DB.select,sqlstr)
    return str(data["data"][0]["id"].decode())
