import json
import sys

from coder import MyEncoder
from flask import Blueprint, Response, request
from flask_restplus import Namespace, Resource, fields, reqparse
from marshmallow import Schema, fields
from model import politicianModel
from .util import(ret, checkParm)

politicianApi = Namespace(name='politician_ful', description='政治人物')

# politicianM=politicianApi.model("politician",{

# })


# @politicianApi.route('/')
# class Test(Resource):
#     @politicianApi.doc("政治人物列表")
#     def get(self):
#         result = politicianModel.list(data={})
#         return Response(json.dumps(result, cls=MyEncoder), mimetype="application/json")

class query(Schema):
    name = fields.Str(required=False)
    term = fields.Str(required=False)
    other = fields.Str(required=False)


@politicianApi.route('/list')
class Test(Resource):
    @politicianApi.param(query)
    @politicianApi.doc("V政治人物列表")
    def get(self):
        print("enter")
        parser = reqparse.RequestParser()

        # try:

        # except:
        #     print("Unexpected error:", sys.exc_info()[0])
        # print("2")
        # parser.add_argument('name', action='append', required=False)
        parser.add_argument('other', action='append', required=False)
        parser.add_argument('term', action='append', required=False)
        print("end")
        args = {}
        try:
            args = parser.parse_args()
        except:
            print("Unexpected error:", sys.exc_info())
        print(2)
        d = {}

        for i in args:
            print(i)
            if args[i] != None:
                d[i] = args[i]
        print(d)
        # return Response(json.dumps(d, cls=MyEncoder), mimetype="application/json")
        return ret(politicianModel.getList(data=d))


@politicianApi.route("/<int:id>")
@politicianApi.param("id", "政治人物編號")
class Politician(Resource):
    @politicianApi.doc("政治人物")
    def get(self, id):        
        return ret(politicianModel.getDetail({"id": id}))
        


@politicianApi.route("/area")
class Area(Resource):
    def get(self):        
        return ret(politicianModel.getArea())


@politicianApi.route("/name")
class Area(Resource):
    def get(self):        
        return ret(politicianModel.getName())


@politicianApi.route("/term")
class Area(Resource):
    def get(self):        
        return ret(politicianModel.getTerm())
# @politicianProfile.route("/find", methods=["GET"])
# def find():
#     content = request.json
#     # name=content['name']
#     cond = ["id", "term", "sex", "partyid", "areaid", "positionid"]
#     data = {}
#     for i in cond:
#         if (i in content.keys()):
#             data[i] = content[i]
#     data = politicianModel.find(data)
#     return Response(json.dumps(data["data"], cls=MyEncoder), mimetype='application/json')

# @politicianProfile.route("/", methods=["PATCH"])
# def changeProfile():
#     content = request.json
#     account = content["id"]
#     cond = [ "term", "sex", "partyid", "areaid", "positionid"]
#     data = {}
#     for i in cond:
#         if(i in content.keys()):
#             data[i] = content[i]
#     data = politicianModel.changePolitician(data, id)
#     result = {"success": False, "message": "修改異常", "data": data}
#     if(data["success"]):
#         result["success"]=True
#         result["message"]="修改成功"
#     return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')
