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
            "sql": "select m.*,p.title from message as m join proposal as p on m.proposal_id = p.id group by m.id having user_id=\"%s\"" % (
                user_id), "name": "msg"
        },
        {
            "sql": "select p.*,s.name as type ,c.name as c_name from user_policy  as up  join policy as p on up.policy_id=p.id join schedule as s on up.ps_id=s.id join policy_category as pc on pc.policy_id=p.id join category as c on pc.category_id=c.id where user_id=\"%s\" group by up.id,p.id,c.id " % user_id,
            "name": "policy_vote"
        },
        {"sql": "select user_id,p.*,s.type from user_proposal as up  join stand as s on up.stand_id=s.id join proposal as p on up.proposal_id=p.id group by p.id having user_id =\"%s\"" % user_id, "name": "proposal_vote"}]
    data = DB.execution(DB.select, sqlstr)
    msg = []
    proposal_id = -1
    title = ""
    item = {}
    m = []
    for i in data["data"][3]["data"]:

        if i["proposal_id"] != proposal_id:
            if proposal_id != -1:
                item["content"] = m
                msg.append(item)
                item = {}
                m = []
            proposal_id = i["proposal_id"]
            item["title"] = i["title"]
            item["proposal"] = i["proposal_id"]
        m.append(i["content"])
    item["content"] = m
    msg.append(item)
    data["data"][3]["data"] = msg
    item = {}
    c = set()
    policy_vote = []
    policy_id = -1
    for i in data["data"][4]["data"]:
        print(i)
        if i["id"] != policy_id:
            if policy_id != -1:
                item["c_name"] = c
                policy_vote.append(item)
                item = {}
                c = set()
            policy_id=i["id"]
            item = i
        c.add(i["c_name"])
    item["c_name"] = c
    policy_vote.append(item)
    data["data"][4]["data"] = policy_vote

    # print(data)
    return data


def getUserIdByLine(line_id):
    sqlstr = "select id from user where line=\"%s\"" % line_id

    data = DB.execution(DB.select, sqlstr)
    return str(data["data"][0]["id"].decode())
