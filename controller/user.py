from flask import Response
from flask_restplus import Namespace, Resource, fields
from model import userModel
import json
from coder import MyEncoder
api = Namespace('user', description='user controller')

userModel = api.model('user', {
    'account': fields.String,
    'password': fields.String,
    "birthday":fields.Date,
    "sex":fields.String,
    "areaid":fields.String,
    "name":fields.String
}, )

resultModel = api.model("result", {
    "message": fields.String,
    "success": fields.Boolean,
    "data": fields.Nested
})


@api.route("/login")
class User(Resource):
    @api.doc("user login")
    # @api.expect(userModel)
    def post(self):
        content = api.payload
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

       
# @api.route("/sign")
# class User(Resource):
#     @api.doc("user sign")
#     @api.expect()