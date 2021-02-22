from model.db import DB
import json


def find(data):
    strCond = ""

    if (isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s =\"%s\" and" % (i, data[i])
    result = {"name": "", "d": []}
    sqlstr = "SELECT post.id,post.name  FROM db.politician as polit join position as post on  polit.position_id=post.id group by  polit.position_id "
    postition = DB.execution(DB.select, sqlstr)
    postition = postition["data"]

    for post in postition:
        resPost = {"name": post["name"], "d": []}
        sqlstr = "select term from politician where position_id='%s' group by term" % post[
            "id"]
        term = DB.execution(DB.select, sqlstr)
        term = term["data"]
        for t in term:
            resT = {"name": t["term"], "d": []}
            sqlstr = "SELECT polit.area_id,a.name FROM db.politician as polit join area as a on polit.area_id=a.id where  position_id='%s'  and term='%s' group by polit.area_id" % (
                post["id"], t["term"])
            areas = DB.execution(DB.select, sqlstr)
            areas = areas["data"]
            print(areas)
            for a in areas:
                resA = {"name": a["name"], "d": []}
                sqlstr = "SELECT * FROM db.politician as polit where  position_id='%s'  and term='%s' and area_id='%s' " % (
                    post["id"], t["term"], a["area_id"].decode())
                polit = DB.execution(DB.select, sqlstr)
                polit = polit["data"]
                for p in polit:
                    resA["d"].append(p)
                resT["d"].append(resA)
            resPost["d"].append(resT)
    return resPost
# sqlstr = "select * from politician  %s" %( "where "+ strCond[0:len(strCond)-3] if len(strCond)>0   else "")
    # return (DB.execution(DB.select, sqlstr))


def list(data):
    strCond = ""
    if (isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s =\"%s\" and" % (i, data[i])
    result = []
    sqlstr = "SELECT * from politician order by position_id,term,area_id"
    rows = DB.execution(DB.select, sqlstr)
    # return rows["data"]
    position = rows["data"][0]["position_id"]
    area = rows["data"][0]["area_id"]
    term = rows["data"][0]["term"]
    pList = []
    aList = []
    tList = []
    dList=[]
    for i in rows["data"]:
        if(area != i["area_id"]):                 
            aList.append({"name": area, "d": dList})
            dList=[]
            area = i["area_id"]
        if(term != i["term"]):            
            tList.append({"name":term,"d":aList})
            aList=[]        
            term = i["term"]
        if(position != i["position_id"]):
            pList.append({"name":position,"d":tList})
            position = i["position_id"]
        dList.append(i)
    
    return pList


def getPropsoal(politicianId):
    sqlstr = "select * from proposer where "


def changePolitician(data, id):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" ," % (i, data[i])
    sqlstr = "update user set %s where id=\"%s\"" % (
        strCond[0:len(strCond)-1], id)
    print(sqlstr)
    return DB.execution(DB.update, sqlstr)
