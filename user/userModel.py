from db import DB
import json


def login(account, password):
    sqlstr = "select * from member where id=\"%s\" and password = \"%s\"" % (
        account, password)
    return (DB.execution(DB.select, sqlstr))
def sign():
    sqlstr=""
    return ""

def findPasswordByAccount(account):
    sqlstr="select password from member where id=\"%s\""%account
    return DB.execution(DB.select,sqlstr)

def changePassword(account,password):
    sqlstr="update member password=\"%s\" where account=\"%s\""%(password,account)
    return DB.execution(DB.update,sqlstr)     