from model.db import DB
import json


def list(data):
    strCond = ""
    if (isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s =\"%s\" and" % (i, data[i])
    result = []
    sqlstr = 'SELECT p.id,p.term,f.name,a.name as a_n	,p.experience,p.degree,p.tel FROM db.politician as p join electorate as e on p.electorate_id=e.id join figure as f on p.figure_id=f.id join area as a on e.area_id=a.id order by e.area_id'
    rows = DB.execution(DB.select, sqlstr)
    # return rows["data"]
    position = rows["data"][0]["postition"]
    area = rows["data"][0]["area"]
    term = rows["data"][0]["term"]
    pList = []
    # aList = []
    tList = []
    dList = []
    for i in rows["data"]:
        # if(area != i["area_id"]):
        #     aList.append({"name": area, "d": dList})
        #     dList=[]
        #     area = i["area_id"]
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
            c = ("%s in (" % i)
            for j in data[i]:
                c += " '%s' ," % j
            strCond += " %s )" % c[0:len(c)-1]

    print(data)
    result = []
    print(strCond)
    sqlstr = "SELECT p.id,p.term,f.name,p.photo,a.name as a_n,p.experience,p.degree,p.tel %s %s order by e.area_id,p.term,f.name" % (
        "FROM db.politician as p join electorate as e on p.electorate_id=e.id join figure as f on p.figure_id=f.id join area as a on e.area_id=a.id",
        "where %s " % strCond if len(strCond) > 0 else ""
    )
    print(sqlstr)
    rows = DB.execution(DB.select, sqlstr)

    return rows


def getDetail(data):
    strCond = ""
    if (isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s =\"%s\" and" % (i, data[i])
    result = []
    sqlstr = (
        "SELECT p.id,p.term,f.name,p.photo,a.name as a_n,p.experience,p.degree,p.tel,pa.name as p_name,e.name as e_n,e.remark %s  where p.id=\"%s\" order by e.area_id,p.term,f.name" % (
            "FROM db.politician as p join electorate as e on p.electorate_id=e.id join figure as f on p.figure_id=f.id join area as a on e.area_id=a.id join party as pa on p.party_id=pa.id",
            data["id"])
    )
    print(sqlstr)
    rows = DB.execution(DB.select, sqlstr)

    return rows


# def getPropsoal(politicianId):
#     sqlstr = "select * from proposer where "


def changePolitician(data, id):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" ," % (i, data[i])
    sqlstr = "update user set %s where id=\"%s\"" % (
        strCond[0:len(strCond)-1], id)
    print(sqlstr)
    return DB.execution(DB.update, sqlstr)


def getArea():
    sqlstr = "SELECT name FROM db.area order by id;"
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


def score(user_id, policy_id, ps_id):
    sqlstr = ("insert into user_policy(user_id,policy_id,ps_id) values(%s,%s,%s)" %
              user_id, policy_id, ps_id)
    return DB.execution(DB.create, sqlstr)
