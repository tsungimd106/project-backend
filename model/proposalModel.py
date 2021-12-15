from model.db import DB
from model.util import group
import json
import math
from snownlp import SnowNLP
from snownlp import sentiment


def pList(data):
    strCond = ""
    if (isinstance(data["cond"], dict)):
        for i in data["cond"].keys():
            if isinstance(data["cond"][i], type(list)):
                for j in data["cond"][i]:
                    if j == "title":
                        strCond += " '"+j+"` like\"%"+j+"%\" and"
                    else:
                        strCond += f" `{i}` =\"{j}\" and"
            else:
                if i == "title":
                    strCond += " "+i+" like \"%"+data["cond"][i]+"%\" and"
                else:
                    conds = "( "
                    for j in str(data["cond"][i]).split(","):
                        conds += j + " ,"
                    strCond += " "+i+" in "+conds[:len(conds)-1]+")"+" and"
    page = int(data["page"]) if data["page"] != None else 0
    sqlstr = [{"sql": "".join([
        "select p.*,s.status ,pc.category_id,f.name,IFNULL(goodc,0) as good ,ifnull(medc,0) as med ,ifnull(badc,0) as bad ,c.name as c_name ",
        "from proposal as p join `status`  as s on p.status_id=s.id ",
        f" join (select * from proposal group by id having term =10  { ' and ' + strCond[0:len(strCond)-3] if len(strCond) > 0 else ''} limit {page*20},20) as t  on p.id=t.id ",
        " left join proposal_category as pc on p.id=pc.propsoal_id ",
        
        " left join category as c on pc.category_id=c.id ",

        " left join proposer as er on p.id=er.proposal_id ",
        " left join politician as po on po.id=er.politician_id ",
        " left join figure as f on po.figure_id=f.id "
        " left join proposal_vote as pv on p.id=pv.id"
    ]), "name":"list"},
        {"sql": f"select count(*)/20 as n from proposal as p where term=10 {'and'+strCond[0:len(strCond)-3] if len(strCond) > 0 else ''}  ",
         "name": "page"}]
    rows = DB.execution(DB.select, sqlstr)
    result = group(rows["data"]["list"], ["name","c_name"], "id")
    

    return ({"data": {"list": result, "page": math.ceil(rows["data"]["page"][0]["n"]), }, "success": True})


def msg(account, mes, article_id, parent_id):
    try:
        s = SnowNLP(mes)
        sqlstr = f"insert into message(user_id,content,proposal_id,parent_id,postive) values(\"{account}\",\"{mes}\",\"{article_id}\",{0 if parent_id==None else parent_id},\"{s.sentiments}\");"

    except ValueError:
        sqlstr = f"insert into message(user_id,content,proposal_id,parent_id) values(\"{account}\",\"{mes}\",\"{article_id}\",{0 if parent_id==None else parent_id});"
        print("what")
        print(ValueError)

    return DB.execution(DB.create, sqlstr)


def vote(userid, sp_id, proposal_id):
    sqlstr = {"name": "proposal_vote", "arg": [
        f"{userid}", f"{proposal_id}", f"{sp_id}"]}
    return DB.execution(DB.store_p, sqlstr)


def msgList(proposal_id, user_id):
    sqlstr = [
        {"sql": f"select m.*,u.name from message as m  join user as u on m.user_id=u.id where proposal_id=\"{proposal_id}\"", "name": "msg"},
        {"sql":
         "".join([
             "select p.id,p.title,p.pdfUrl ,s.status,f.name from proposal as p ",
             " left join proposer as er on er.proposal_id=p.id ",
             " left join politician as polit on polit.id=er.politician_id ",
             " left join figure as f on polit.figure_id=f.id ",
             " left join status as s on p.status_id=s.id ",
             " left join proposal_category as pc on p.id=pc.propsoal_id "

             f"where   p.id=\"{proposal_id}\" "

         ]),
            "name": "detail"},
        {
            "sql": f"select * from favorite where user_id=\"{proposal_id}\" and proposal_id=\"{user_id}\"",
            "name": "heart"}, {"sql": "select * from rule", "name": "rule"},
        {
            "sql": f"SELECT * FROM db.proposal_vote where id=\"{proposal_id}\"",
            "name": "vote"
        }
    ]
    rows = DB.execution(DB.select, sqlstr)
    rows["data"]["detail"] = group(rows["data"]["detail"], ["name"], "id")
    return rows


def msgListByUser(user_id):
    sqlstr = f"select m.*,p.title from message as m join proposal as p on m.proposal_id = p.id where user_id=\"{user_id}\";"
    return DB.execution(DB.select, sqlstr)


def getSave(user_id):
    sqlstr = f"select * from favorite as f join proposal as p on f.proposal_id=p.id join status as s on p.status_id=s.id where user_id=\"{user_id}\""
    return DB.execution(DB.select, sqlstr)


def save(user_id, proposal_id):
    sqlstr = f"insert into favorite( user_id,proposal_id) values(\"{user_id}\",\"{proposal_id}\");"
    return DB.execution(DB.create, sqlstr)


def report(user_id, message_id, remark, rule):
    sql_Remark = []
    DB.execution(
        DB.create, f"insert into report (`user_id`,`message_id`,`remark`) values(\"{user_id}\",{message_id},\"{remark}\")")
    report_id = DB.execution(
        DB.select, f"select id from(select * from report  order by id) y where id in ( select max(id) from report where user_id=\"{user_id}\" )")
    report_id = report_id["data"][0]["id"]
    for i in rule:
        sql_Remark.append(
            {"sql": f"insert into `report_rule`(`report_id`,`rule_id`) values({report_id},{i});"})

    return DB.execution(DB.create, sql_Remark)


def rule():
    sqlstr = "select * from rule"
    return DB.execution(DB.select, sqlstr)


def getCond():
    sqlstr = [
        {"sql":  "select term as name from proposal group by term;", "name": "屆別"},
        {"sql": "select s.id,s.status as name from proposal as p join status as s on p.status_id=s.id group by status_id;", "name": "狀態"}
    ]
    return DB.execution(DB.select, sqlstr)


def great(user_id, m_id):
    sqlstr = f"insert into great(message_id,user_id) values(\"{user_id}\",\"{m_id}\")"
    return DB.execution(DB.create, sqlstr)


def removeGreat(user_id, m_id):
    sqlstr = f"delete great where user_id={user_id} and message_id {m_id}"
    return DB.execution(DB.delete, sqlstr)
