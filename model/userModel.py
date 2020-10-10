from model.db import DB
import json


def login(account, password):
    sqlstr = "select * from member where id=\"%s\" and password = \"%s\"" % (
        account, password)
    return (DB.execution(DB.select, sqlstr))


def findPasswordByAccount(account):
    sqlstr = "select password from member where id=\"%s\"" % account
    return DB.execution(DB.select, sqlstr)


def changePassword(account, password):
    sqlstr = "update member password=\"%s\" where id=\"%s\"" % (
        password, account)
    return DB.execution(DB.update, sqlstr)


def sign(account, password, age, sex,area):
    sqlstr = "insert into member(id, password,age,sex,area) VALUES (%s, %s ,%s ,%s,%s)" % (
        account, password, age, sex,area)
    return DB.execution(DB.create, sqlstr)


def findArea(area):
    sqlstr = "select * from area "
    return DB.execution(DB.select, sqlstr)


def findUserarea(area):
    sqlstr = "select area from member where id = \"%s\"" % (
        area)
    return DB.execution(DB.select, sqlstr)
