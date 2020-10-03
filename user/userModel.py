from db import DB
import json


def login(account, password):
    sqlstr = "select * from member where id=\"%s\" and password = \"%s\"" % (
        account, password)
    return (DB.execution(DB.select, sqlstr))
def sign():
    sqlstr=""
    return ""