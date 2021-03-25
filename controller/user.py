from flask import Response
from flask_restplus import Namespace, Resource, fields
from model import userModel
import json
from coder import MyEncoder
userApi = Namespace(name='user', description='使用者')

loginModal = userApi.model("login", {
    'account': fields.String,
    'password': fields.String,
})

userM = userApi.clone('user', loginModal, {

    "birthday": fields.Date,
    "sex": fields.String,
    "areaid": fields.String,
    "name": fields.String
}, )
signModel = userApi.clone("sign", userM, {
    "confirePassword": fields.String
})

# resultModel = api.model("result", {
#     "message": fields.String,
#     "success": fields.Boolean,
#     "data": fields.Nested
# })


@userApi.route("/test")
class Test(Resource):
    def get(self):
        return "test"


@userApi.route("/login")
class Login(Resource):
    @userApi.doc("使用者登入")
    @userApi.expect(loginModal)
    def post(self):
        content = userApi.payload
        account = content['account']
        password = content["password"]
        data = userModel.login(account, password)
        result = {"success": False, "data": data["data"], "message": ""}
        if len(data["data"]) == 1:
            result["message"] = "登入成功"
            result["success"] = True
        elif len(data["data"]) == 0:
            result["message"] = "登入失敗"
        else:
            result["message"] = "登入異常"
        return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')


@userApi.route("/sign")
class Sign(Resource):
    @userApi.doc("user sign")
    @userApi.expect(signModel)
    def post(self):
        content = userApi.payload
        cond = ["account", "password", "age", "sex", "areaid", "name"]
        result = {"success": False, "message": ""}

        if(checkParm(cond, content)):
            data = userModel.sign(content["account"], content["password"],
                                  content["age"], content["sex"], content["areaid"], content["name"])
        print(data)
        if(data["success"]):
            result["message"] = "註冊成功"
            result["success"] = True
        else:
            result["message"] = "註冊異常"
        return Response(json.dumps(result, cls=MyEncoder))


@userApi.route("/")
class User(Resource):
    @userApi.doc("user updatfile")
    def patch(self):
        content = userApi.payload
        data = {}
        cond = ["sex", "areaid", "nickname"]
        result = {"success": False, "message": ""}
        for i in cond:
            if i in content.keys():
                data[i] = content[i]

        result = userModel.changeProfile(data, account)

        if(data["success"]):
            result["message"] = "修改成功"
            result["success"] = True
        else:
            result["message"] = "修改異常"
        return Response(json.dumps(result, cls=MyEncoder))


def checkParm(cond, content):
    res = ""
    for i in cond:
        if(i not in content.keys()):
            res += "缺少必要參數 %s\n" % i
    return res
