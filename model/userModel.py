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
    sqlstr = [{"sql": "SELECT id,name,nick_name,degree,area_id,gender,birthday FROM db.user where id=\"%s\"" %
               user_id, "name": "user"},
              {"sql": "select * from area", "name": "area"},
              {
                  "sql": ("select * from favorite as f join proposal as p on f.proposal_id=p.id join status as s on p.status_id=s.id where user_id=\"%s\"" % user_id),
                  "name": "save"}
              , {
                  "sql": "select m.*,p.title from message as m join proposal as p on m.proposal_id = p.id where user_id=\"%s\"" % (
                      user_id), "name": "msg"
    }]
    return DB.execution(DB.select, sqlstr)
