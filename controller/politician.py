from flask import Blueprint, request, Response
from flask_restplus import Namespace, Resource, fields

from model import politicianModel
import json
from coder import MyEncoder
politicianApi =Namespace(name='politician',description='政治人物')

# politicianM=politicianApi.model("politician",{
    
# })

@politicianApi.route('/')
class Test(Resource):
    @politicianApi.doc("政治人物列表")
    def get(self):            
        result=politicianModel.list(data={})
        return Response(json.dumps(result,cls=MyEncoder),mimetype="application/json")


@politicianApi.route("/<int:id>")
@politicianApi.param("id","政治人物編號")
class Politician(Resource):
    @politicianApi.doc("政治人物")
    def get(self,id):
        result=politicianModel.find({"id":id})
        return Response(json.dumps(result,cls=MyEncoder),mimetype="application/json")        

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
