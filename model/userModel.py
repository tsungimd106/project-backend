from model.db import DB
import json
from model.util import group


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
    return DB.execution(DB.create, sqlstr)


def changeProfile(data, account):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" ," % (i, data[i])
    sqlstr = "update user set %s where id=\"%s\"" % (
        strCond[0:len(strCond)-1], account)
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
        {"sql": "".join(["SELECT u.id,u.name,nick_name,degree,a.name as a_n ,gender,birthday FROM db.user as u join area as a on u.area_id=a.id where u.id=\"", user_id, "\""]), "name": "user"},
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
            "sql": "".join([
                "select m.*,p.title ,c.name as c_name ,f.name as f_name from message as m",
                " left join proposal as p on m.proposal_id = p.id",
                " left join proposer as er on p.id=er.proposal_id",
                " left join politician as po on er.politician_id=po.id ",
                " left join figure as f on po.figure_id=f.id ", "left join proposal_category as pc on pc.propsoal_id=p.id",
                " left join category as c on pc.category_id=c.id",
                " group by m.id ,c.name,f.name having user_id=\"", user_id, "\" order by p.id,m.id"

            ]), "name": "msg"
        },
        {
            "sql": "".join(["select p.*,s.name as type ,c.name as c_name from user_policy  as up  join policy as p on up.policy_id=p.id join schedule as s on up.ps_id=s.id join policy_category as pc on pc.policy_id=p.id join category as c on pc.category_id=c.id where user_id=\"", user_id, "%s\" group by up.id,p.id,c.id "]),
            "name": "policy_vote"
        },
        {"sql": "".join(["select user_id,p.*,s.type from user_proposal as up  join stand as s on up.stand_id=s.id join proposal as p on up.proposal_id=p.id group by p.id having user_id =\"", user_id, "%s\""]), "name": "proposal_vote"}]
    data = DB.execution(DB.select, sqlstr)

    data["data"][2]["data"] = group(data["data"][2]["data"], [
                                    "f_name", "c_name"], "id")
    data["data"][4]["data"] = group(data["data"][4]["data"], ["c_name"], "id")
    # data["data"][3]["data"]=group(data["data"][3]["data"],["f_name","c_name"],"proposal_id")
    msg = []
    proposal_id = data["data"][3]["data"][0]["proposal_id"]
    m_id=data["data"][3]["data"][0]["id"]
    title = ""
    item = {}
    m = []
    abc=0
    c_name=set()
    f_name=set()
    for i in data["data"][3]["data"]:
        if i["proposal_id"] != proposal_id:
            if proposal_id != -1:
                item["content"] = m
                item["c_name"]=c_name
                item["f_name"]=f_name
                item["proposal_id"]=i["proposal_id"]
                item["title"]=i["title"]
                c_name=set()
                f_name=set()
                msg.append(item)
                item = {}
                m = []
            proposal_id = i["proposal_id"]
        if(m_id!=i["id"]):
            m_id=i["id"]
            abc+=1
            m.append({"content": i["content"], "time": i["time"],"postive":i["postive"],"id":i["id"]})
        c_name.add(i["c_name"])
        f_name.add(i["f_name"])
    item["content"] = m
    item["c_name"]=c_name
    item["f_name"]=f_name
    item["proposal_id"]=i["proposal_id"]
    item["title"]=i["title"]
    msg.append(item)
    data["data"][3]["data"] = msg
    print(abc)
    # data["data"][3]["data"]=group(data["data"][3]["data"],["f_name","c_name"],"proposal_id")
    return data


def getUserIdByLine(line_id):
    sqlstr = "select id from user where line=\"%s\"" % line_id

    data = DB.execution(DB.select, sqlstr)
    return str(data["data"][0]["id"].decode())
