from model.db import DB
import json


def list(data):
    strCond = ""
    if (isinstance(data["cond"], dict)):
        for i in data["cond"].keys():
            if isinstance(data["cond"][i], type(list)):
                for j in data["cond"][i]:
                    strCond += " `%s` =\"%s\" and " % (i, j)
            else:
                strCond += " %s =\"%s\" and" % (i, data["cond"][i])
    page = int(data["page"]) if data["page"] != None else 0
    # if (isinstance(data, dict)):
    #     for i in data.keys():
    #         strCond += " %s =\"%s\" and" % (i, data[i]) if i!="page" else ""
    sqlstr = [{"sql": "select p.*,s.status ,pc.category_id,h.hashtag_name,f.name %s %s %s %s %s %s %s  " % (
        "from proposal as p join `status`  as s on p.status_id=s.id",
        "join (select * from proposal group by id having term =10  %s limit %d,20) as t  on p.id=t.id" % (
            "and " + strCond[0:len(strCond)-3] if len(strCond) > 0 else "", page*20),
        "left join proposal_category as pc on p.id=pc.propsoal_id",
        "left join hashtag as h on pc.category_id=h.id",
        "left join proposer as er on p.id=er.proposal_id",
        "left join politician as po on po.id=er.politician_id",
        "left join figure as f on po.figure_id=f.id"
    ), "name":"list"}, {"sql": "select count(*)/20 as n from proposal as p where term=10 %s  " % ("and"+strCond[0:len(strCond)-3] if len(strCond) > 0 else ""), "name":"page"}]
    rows = DB.execution(DB.select, sqlstr)
    
    result = []
    if len(rows["data"][0]["data"]) > 0:
        pdf = set()
        category = set()
        proposer = set()
        temp = rows["data"][0]["data"][0]
        now = rows["data"][0]["data"][0]["id"]
        for i in rows["data"][0]["data"]:
            if now != i["id"]:
                temp["pdfUrl"] = pdf
                temp["category"] = category
                temp["proposer"] = proposer
                result.append(temp)
                now = i["id"]
                pdf = set()
                category = set()
                proposer = set()
                temp = i
            pdf.add(i["pdfUrl"])
            proposer.add(i["name"])
            category.add(i["hashtag_name"])

        temp["pdfUrl"] = pdf
        temp["category"] = category
        temp["proposer"] = proposer
        result.append(temp)
    return ({"list":result,"page":rows["data"][1]["data"]})


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
        {"sql": " select p.id,p.title,p.pdfUrl ,s.status,f.name ,h.hashtag_name from proposal as p %s  %s %s  %s  %s where   p.id=\"%s\" " %
            ("left join proposer as er on er.proposal_id=p.id",
             "left join figure as f on er.politician_id=f.id",
             "left join status as s on p.status_id=s.id",
             "left join proposal_category as pc on p.id=pc.propsoal_id",
             "left join hashtag as h on pc.category_id=h.id",
                proposal_id),
         "name": "detail"},
        {"sql": "select * from favorite where user_id=\"%s\" and proposal_id=\"%s\"" %
         (proposal_id, user_id), "name": "heart"}, {"sql": "select * from rule", "name": "rule"}
    ]
    rows = DB.execution(DB.select, sqlstr)
    result = {}
    category = set()
    proposer = set()
    # print(rows)
    for i in rows["data"][1]["data"]:
        category.add(i["hashtag_name"])
        proposer.add(i["name"])
    rows["data"][1]["data"][0]["name"] = proposer
    rows["data"][1]["data"][0]["category"] = category
    rows["data"][1]["data"] = rows["data"][1]["data"][0]
    return rows


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

    return DB.execution(DB.update, sqlstr)


def getCond():
    sqlstr = [
        {"sql":  "select term as name from proposal group by term;", "name": "屆別"},
        {"sql": "select s.status as name from proposal as p join status as s on p.status_id=s.id group by status_id;", "name": "狀態"}
    ]
    return DB.execution(DB.select, sqlstr)
