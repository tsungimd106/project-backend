from model.db import DB
import json
from model.util import group


def list(data):
    strCond = ""
    if (isinstance(data, dict)):
        for i in data.keys():
            strCond += f" {i} =\"{data[i]}\" and"
    result = []
    sqlstr = 'SELECT p.id,p.term,f.name,a.name as a_n	,p.experience,p.degree,p.tel FROM db.politician as p join electorate as e on p.electorate_id=e.id join figure as f on p.figure_id=f.id join area as a on e.area_id=a.id order by e.area_id'
    rows = DB.execution(DB.select, sqlstr)
    # return rows["data"]
    position = rows["data"][0]["postition"]
    area = rows["data"][0]["area"]
    term = rows["data"][0]["term"]
    pList = []
    tList = []
    dList = []
    for i in rows["data"]:
        if(term != i["term"]):
            tList.append({"name": term, "d": dList})
            aList = []
            term = i["term"]
        if(position != i["postition"]):
            pList.append({"name": position, "d": tList})
            position = i["postition"]
        dList.append(i)

    return pList


def getList(data):
    strCond = ""
    if (isinstance(data, dict)):
        for i in data.keys():
            c = (f"{i} in (")
            for j in data[i]:
                c += f" '{j}' ,"
            strCond += f" { c[0:len(c)-1]} )"
    sqlstr = "".join([
        " SELECT p.id,p.term,f.name,p.photo,a.name as a_n,p.experience,p.degree,p.tel ,cs.score ",
        " FROM db.politician as p join electorate as e on p.electorate_id=e.id join figure as f on p.figure_id=f.id join area as a on e.area_id=a.id ",
        " join count_score as cs on p.id=cs.id "
        f"  {' where '+strCond if len(strCond) > 0 else ''} ",
        " order by e.area_id,p.term,f.name"
    ])

    rows = DB.execution(DB.select, sqlstr)

    return rows


def getDetail(data):
    strCond = ""
    if (isinstance(data, dict)):
        for i in data.keys():
            strCond += f" {i} =\"{data[i]}\" and"
    result = []
    sqlstr = [
        {
            "sql":

            "SELECT p.id,p.term,f.name,p.photo,a.name as a_n,p.experience,p.degree,p.tel,pa.name as p_name,e.name as e_n,e.remark"
            + " FROM db.politician as p join electorate as e on p.electorate_id=e.id join figure as f on p.figure_id=f.id join area as a on e.area_id=a.id join party as pa on p.party_id=pa.id"
            + f" where p.id=\" {data['id']} \" order by e.area_id,p.term,f.name",              "name": "detail"
        },
        {
            "sql": f"select p.id,p.content,c.name ,c.id as c_id from policy as p join policy_category as pc on pc.policy_id=p.id join category as c on pc.category_id=c.id where politician_id={data['id']} order by p.id",
            "name": "policy"
        },  {
            "sql": "".join(["SELECT * FROM table_policy where  p_id =\"", data["id"], "\"", " order by quota desc ,total desc"]), "name":"table_policy"
        },
        {
            "sql": "".join(["SELECT * FROM table_policyDetail where  id =\"", data["id"], "\""]), "name":"table_policyDetail"
        },  {
            "sql": "".join(["SELECT * FROM count_score where  id =\"", data["id"], "\""]), "name":"count_score"
        }, {
            "sql": "".join(["select *,count(*) as quota from proposer where politician_id=", data["id"], " group by politician_id "]), "name":"proposal_quota"
        }, {
            "sql": "".join(["select * from proposer as er join proposal as p on er.proposal_id=p.id where er.politician_id=\"", data["id"], "\""]), "name":"proposal"
        },
        {
            "sql": f"SELECT session,attend FROM db.attendance  where politician_id={data['id']} group by `session` ;", "name": "attend"
        },
        {
            "sql": f"SELECT session,sum(attend)/count(*) as avg FROM db.attendance group by `session` ;",            "name": "trend_attend_group"
        },
        {
            "sql": f"select s.status,ifnull(d.c,0) as c  from status as s left join (select status_id,count(*) as c from proposer as er  left join proposal as po on er.proposal_id=po.id where er.politician_id={data['id']} group by status_id ) d on d.status_id=s.id ",
            "name": "pro"
        },
        {
            "sql": f"select s.status,ifnull(d.c,0)/113 as c from status as s left join (select status_id,count(*) as c from proposer as er  left join proposal as po on er.proposal_id=po.id  group by status_id ) d on d.status_id=s.id ",
            "name": "trend_pro"
        },
        {
            "sql": "".join([
                "SELECT   fakeD.t ,ifnull(realD.score,0) as score from  ",
                " (select concat(year(up.time),'-',month(up.time)) as t from user_policy as up group by month(up.time)) fakeD "
                "left join (SELECT   (SUM(`s`.`value`) / COUNT(`s`.`name`)) AS `score`,   `po`.`politician_id` AS `politician_id`,  concat(year(up.time),'-',month(up.time)) as t  "
                "FROM  ((`policy` `po`  JOIN `user_policy` `up` ON ((`up`.`policy_id` = `po`.`id`))) ",
                f"JOIN `schedule` `s` ON ((`up`.`ps_id` = `s`.`id`)))  where politician_id={data['id']} GROUP BY month(up.time) ) realD on fakeD.t=realD.t "

            ]),
            "name": "trend_policy"
        }, {
            "name": "trend_policy_group",
            "sql": "".join([
                "SELECT   fakeD.t ,ifnull(realD.score,0) as score from  ",
                " (select concat(year(up.time),'-',month(up.time)) as t from user_policy as up group by month(up.time)) fakeD "
                "left join (SELECT   (SUM(`s`.`value`) / COUNT(`s`.`name`)) AS `score`,   `po`.`politician_id` AS `politician_id`,  concat(year(up.time),'-',month(up.time)) as t  "
                "FROM  ((`policy` `po`  JOIN `user_policy` `up` ON ((`up`.`policy_id` = `po`.`id`))) ",
                f"JOIN `schedule` `s` ON ((`up`.`ps_id` = `s`.`id`)))    GROUP BY month(up.time) ) realD on fakeD.t=realD.t "

            ]),
        }
    ]

    rows = DB.execution(DB.select, sqlstr)
    rows["data"]["policy"] = group(rows["data"]["policy"], ["name"], "id")
    return rows


# 用不到
def changePolitician(data, id):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" ," % (i, data[i])
    sqlstr = "update user set %s where id=\"%s\"" % (
        strCond[0:len(strCond)-1], id)
    return DB.execution(DB.update, sqlstr)


def getArea():
    sqlstr = "SELECT id as value ,name as text FROM db.area order by id;"
    strCond = ""
    return DB.execution(DB.select, sqlstr)


def getName():
    sqlstr = "SELECT name FROM db.figure group by name;"
    strCond = ""
    return DB.execution(DB.select, sqlstr)


def getTerm():
    sqlstr = "SELECT term FROM db.politician group by term;"
    strCond = ""
    return DB.execution(DB.select, sqlstr)


def getCond():
    sqlstr = [{"sql": "SELECT name FROM db.area order by id;", "name": "地區"},
              {"sql": "SELECT name FROM db.figure group by name;", "name": "姓名"},
              {"sql": "SELECT term as name FROM db.politician group by term;", "name": "屆別"}]
    return DB.execution(DB.select, sqlstr)


def schedule():
    sqlstr = "select * from db.schedule"
    return DB.execution(DB.select, sqlstr)


def score(user_id, policy_id, ps_id, remark):   
    sqlstr = {"name": "policy_vote", "arg": [
        f"{user_id}", f"{policy_id}", f"{ps_id}",f"{remark}"]}
    return DB.execution(DB.store_p, sqlstr)
