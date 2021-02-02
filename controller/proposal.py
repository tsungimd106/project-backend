from flask import Blueprint, request, Response
from flask_restplus import Namespace, Resource, fields

from model import proposalModal
import json
from coder import MyEncoder
proposalApi = Namespace('proposal', description='提案')

proposal = Blueprint("proposal", __name__, url_prefix="/proposal")
# proposalM=proposalApi.moel("proposal",{
#     "id":fields.String,
#     "term":fields.String,
#     "sessionPeriod":fields.String,
#     "billNo":fields.String,
#     "billName":fields.String,
#     "billOrg":fields.String,
#     "ststusid":fields.String,
#     "billCosignator":fields.String

# })

# @proposalApi.route("/")
# class Proposal(Resource):
#     @proposalApi.doc("提案")
#     def get(self):
#         content = proposalApi.payload
#         # name=content['name']
#         cond = ["id", "term", "sessionPeriod", "billNo", "billName",
#                 "billOrg", "ststusid", "billProposer", "billCosignator"]
#         data = {}
#         if(isinstance(content,dict)):
#             for i in cond:
#                 if (i in content.keys()):
#                     data[i] = content[i]
#         data = proposalModal.find(data)
#         return Response(json.dumps(data["data"], cls=MyEncoder), mimetype='application/json')


@proposal.route("/", methods=["PATCH"])
def changeProfile():
    content = request.json
    id = content["id"]
    cond = ["term", "sessionPeriod", "billNo", "billName",
            "billOrg", "ststusid", "billProposer", "billCosignator"]
    data = {}
    for i in cond:
        if(i in content.keys()):
            data[i] = content[i]
    data = proposalModal.change(data, id)
    result = {"success": False, "message": "修改異常", "data": data}
    if(data["success"]):
        result["success"]=True
        result["message"] = "修改成功"
    return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')
