from flask import Response
import json
from coder import MyEncoder


def checkParm(cond, content):
    res = ""
    for i in cond:
        if(i not in content.keys()):
            res += "缺少必要參數 %s\n" % i
    return res


def ret(result):
    return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')
