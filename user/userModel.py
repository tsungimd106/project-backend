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


def sign(account, password, age, sex):
    sqlstr = "INSERT INTO member(id, password,age,sex) VALUES (%s, %s ,%s ,%s)"% (account, password, age, sex)
    return DB.execution(DB.create, sqlstr)
