from flask import Blueprint, request, Response
from model import userModel, proposalModel
import json
from coder import MyEncoder
from flask import app
from .util import checkParm, ret

userProfile = Blueprint("user", __name__, url_prefix="/user")


@userProfile.route("/login", methods=["POST"])
def login():
    content = request.json
    account = content['account']
    password = content["password"]
    data = userModel.login(account, password)
    result = {"sucess": False, "data": data}
    if len(data["data"]) == 1:
        result["message"] = "登入成功"
        result["sucess"] = True
    elif len(data["data"]) == 0:
        result["message"] = "登入失敗"
    else:
        result["message"] = "登入異常"

    return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')


@userProfile.route("/sign", methods=["POST"])
def sign():
    content = request.json
    cond = ["account", "password", "age", "sex", "areaid", "name", "degree"]
    result = {"success": False, "message": ""}
    for i in cond:
        if(i not in content.keys()):
            result["message"] += "缺少必要參數 %s\n" % i
    if(result["message"] == ""):
        data = userModel.sign(content["account"], content["password"],
                              content["age"], content["sex"], content["areaid"], content["name"])
        if(data["success"]):
            result["message"] = "註冊成功"
            result["success"] = True
        else:
            result["message"] = "註冊異常"
    return Response(json.dumps(result, cls=MyEncoder))


@userProfile.route("/findUserarea", methods=["GET"])
def findUserarea():
    content = request.json
    area = content["area"]
    data = userModel.findUserarea(area)
    return Response(json.dumps(data, cls=MyEncoder), mimetype="application/json")


@userProfile.route("/<u_id>", methods=["GET"])
def getUser(u_id):
    return ret(userModel.user(u_id))


@userProfile.route("/", methods=["POST"])
def user():
    content = request.json
    return ret(userModel.user(content["user_id"]))


@userProfile.route("/psw", methods=["POST"])
def edit():
    content = request.json
    print(content)
    cond = ["account", "oldPassword", "password", "passwordConfire"]
    result = {"success": False, "message": ""}
    t = checkParm(cond, content)

    if(isinstance(t, dict)):
        oldPasswordFromDB = userModel.findPasswordByAccount(
            content["account"], t["oldPassword"])
        print(oldPasswordFromDB)
        if(oldPasswordFromDB["success"]):
            oldPasswordFromDB = oldPasswordFromDB["data"]
            if(len(oldPasswordFromDB) > 0):
                if(content["password"] != content["passwordConfire"]):
                    result["message"] += "密碼和確認密碼不同\n"
                if(result["message"] == ""):
                    data = userModel.changePassword(
                        content["account"], content["password"])
                    result["message"] = "更換密碼成功"
                    result["success"] = True
                    result["data"] = data
            elif(len(oldPasswordFromDB) == 0):
                result["message"] = "輸入舊密碼錯誤"
            else:
                result["message"] = "帳號異常"
    return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')


@userProfile.route("/", methods=["PATCH"])
def changeProfile():
    content = request.json
    account = content["account"]
    cond = [ "area_id","name"]
    data = {}
    for i in cond:
        if(i in content.keys()):
            data[i] = content[i]
    data = userModel.changeProfile(data, account)
    result = {"success": False, "message": "修改異常", "data": data}
    if(data["success"]):
        result["success"] = True
        result["message"] = "修改成功"
    return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')


@userProfile.route("/msg/<u_id>", methods=["GET"])
def getMsg(u_id):
    return ret(proposalModel.msgListByUser(u_id))


@userProfile.route("vote/<u_id>", methods=["GET"])
def getVote(u_id):
    return ret("")
