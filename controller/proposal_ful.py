from flask import Blueprint, request, Response
from flask_restplus import Namespace, Resource, fields

from model import proposalModal
import json
from coder import MyEncoder
from .util import(checkParm, ret)
import sys
proposalApi = Namespace('proposal_ful', description='提案')


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
proposal_M = proposalApi.model("proposal_msg", {
    "user_id": fields.String,
    "content": fields.String,
    "article_id": fields.String,
    "parent_id": fields.Integer
})


@proposalApi.route("/")
class Proposal(Resource):
    @proposalApi.doc("提案")
    def get(self):

        # name=content['name']
        cond = ["id", "term", "sessionPeriod", "title", 
                 "ststusid"]
        data = {}
        try:
            content = proposalApi.payload
            if(isinstance(content, dict)):
                for i in cond:
                    if (i in content.keys()):
                        data[i] = content[i]
        except:
            print("Unexpected error:", sys.exc_info()[0])
        print("2")

        data = proposalModal.list({})
        print(data)
        return ret(data["data"])

    def patch(self):
        content = proposalApi.payload
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
            result["success"] = True
            result["message"] = "修改成功"
        return ret(result)


@proposalApi.route("/msg")
class Proposal_Msg(Resource):

    @proposalApi.doc("提案留言")
    @proposalApi.expect(proposal_M)
    def post(self):
        content = proposalApi.payload
        cond = ["user_id", "content", "article_id", "parent_id"]
        t = checkParm(cond, content)
        if(t == ""):
            data = proposalModal.msg(
                account=content[cond[0]], mes=content[cond[1]], article_id=content[cond[2]], parent_id=content[cond[3]])
        else:
            data = {"success": False, "mes": t}
        print(data)
        return ret(data)


@proposalApi.route("/msg/<id>")
class Proposal_Msg(Resource):
    @proposalApi.doc("提案留言查詢")
    def get(self, id):
        return ret(proposalModal.msgList(id))


@proposalApi.route("/vote")
class Proposal_Vote(Resource):
    @proposalApi.doc("提案投票")
    def post(self):
        content = proposalApi.payload
        cond = ["user_id", "sp_id", "proposal_id"]
        t = checkParm(cond, content)
        if(t == ""):
            data = proposalModal.vote(
                userid=content[cond[0]], sp_id=content[cond[1]], proposal_id=content[cond[2]])
        else:
            data = {"success": False, "mes": t}
        print(data)
        return ret(data)
