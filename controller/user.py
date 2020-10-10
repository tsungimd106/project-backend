from flask import Blueprint, request, Response
from model import userModel
import json
from coder import MyEncoder


userProfile = Blueprint("user", __name__, url_prefix="/user")


@userProfile.route("/login", methods=["POST"])
def login():
    content = request.json
    account = content['account']
    password = content["password"]
    data = userModel.login(account, password)
    result = {"sucess": False, "data": data}
    if len(data) == 1:
        result["message"] = "登入成功"
        result["sucess"] = True
    elif len(data) == 0:
        result["message"] = "登入失敗"
    else:
        result["message"] = "登入異常"

    return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')


@userProfile.route("/sign", methods=["POST"])
def sign():
    content = request.json
    account = content['account']
    password = content["password"]
    age = content["age"]
    sex = content["sex"]
    area = content["area"]
    data = userModel.sign(account, password, age, sex,area)
    return("enter sign")


@userProfile.route("/findUserarea", methods=["GET"])
def findUserarea():
    content = request.json
    area = content["area"]
    data = userModel.findUserarea(area)
    return("")


@userProfile.route("/password", methods=["PUT"])
def edit():
    content = request.json
    account = content["account"]
    oldPassword = content["oldpassword"]
    password = content["password"]
    passwordConfire = content["passwordConfire"]
    result = {"success": False, "message": ""}
    oldPasswordFromDB = userModel.findPasswordByAccount(account)
    if(oldPasswordFromDB):
        if(oldPasswordFromDB != oldPassword):
            result["message"] += "輸入舊密碼錯誤\n"
        if(password != passwordConfire):
            result["message"] += "密碼和確認密碼不同\n"
        if(result["message"]):
            data = userModel.changePassword(account, password)
            result["message"] = "更換密碼"
            result["data"] = data
    else:
        result["message"] = "帳號不存在"
    return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')
