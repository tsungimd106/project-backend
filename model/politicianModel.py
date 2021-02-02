from model.db import DB
import json


def find(data):
    strCond=""
    
    if (isinstance(data ,dict)):
        for i in data.keys():
            strCond+=" %s =\"%s\" and" %(i,data[i])
    
    sqlstr = "select * from politician  %s" %( "where "+ strCond[0:len(strCond)-3] if len(strCond)>0   else "")    
    return (DB.execution(DB.select, sqlstr))

def getPropsoal(politicianId):
    sqlstr="select * from proposer where "
def changePolitician(data, id):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" ," % (i, data[i])    
    sqlstr = "update user set %s where id=\"%s\"" % (
        strCond[0:len(strCond)-1], id)
    print(sqlstr)
    return DB.execution(DB.update, sqlstr)



