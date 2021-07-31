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
            "sql": ("".join([
                "select p.*,s.status ,fi.name as f_name,c.name as c_name from favorite as f ",
                "join proposal as p on f.proposal_id=p.id ",
                "join status as s on p.status_id=s.id ",
                "left join proposer as er on p.id=er.proposal_id ",
                "left join politician as po on er.politician_id=po.id ",
                "left join figure as fi on po.figure_id=fi.id ",
                "left join proposal_category as pc on p.id=pc.propsoal_id ",
                "left join category as c on pc.category_id=c.id ",
                "where user_id= \"",
                user_id, "\" group by p.id,er.politician_id,c_name "
            ])),

            "name": "save"},
        {
            "sql": "select m.*,p.title ,c.name,f.name from message as m %s %s %s %s %s %s group by m.id ,c.name,f.name having user_id=\"%s\"" % (
                " left join proposal as p on m.proposal_id = p.id",
                " left join proposer as er on p.id=er.proposal_id",
                "left join politician as po on er.politician_id=po.id ",
                "left join figure as f on po.figure_id=f.id ",
                "left join proposal_category as pc on pc.propsoal_id=p.id",
                "left join category as c on pc.category_id=c.id",

                user_id), "name": "msg"
        },
        {
            "sql": "select p.*,s.name as type ,c.name as c_name from user_policy  as up  join policy as p on up.policy_id=p.id join schedule as s on up.ps_id=s.id join policy_category as pc on pc.policy_id=p.id join category as c on pc.category_id=c.id where user_id=\"%s\" group by up.id,p.id,c.id " % user_id,
            "name": "policy_vote"
        },
        {"sql": "select user_id,p.*,s.type from user_proposal as up  join stand as s on up.stand_id=s.id join proposal as p on up.proposal_id=p.id group by p.id having user_id =\"%s\"" % user_id, "name": "proposal_vote"}]
    data = DB.execution(DB.select, sqlstr)
    temp = {}
    f_name = set()
    c_name = set()
    save = []
    proposal_id = -1
    for i in data["data"][2]["data"]:
        if i["id"] != proposal_id:
            if proposal_id != -1:
                temp["f_name"] = f_name
                temp["c_name"] = c_name
                save.append(temp)
                temp = i
                f_name = set()
                c_name = set()
            else:
                temp = i
        f_name.add(i["f_name"])
        print(f_name)
        c_name.add(i["c_name"])
        proposal_id = i["id"]

    temp["f_name"] = f_name
    temp["c_name"] = c_name
    save.append(temp)
    data["data"][2]["data"] = save
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
        m.append({"content": i["content"], "time": i["time"]})
    item["content"] = m
    msg.append(item)
    data["data"][3]["data"] = msg
    item = {}
    c = set()
    policy_vote = []
    policy_id = -1
    for i in data["data"][4]["data"]:
      
        if i["id"] != policy_id:
            if policy_id != -1:
                item["c_name"] = c
                policy_vote.append(item)
                item = {}
                c = set()
            policy_id = i["id"]
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
