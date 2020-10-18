from flask import Blueprint, request, Response
from model import proposalModal
import json
from coder import MyEncoder


proposal = Blueprint("proposal", __name__, url_prefix="/proposal")


@proposal.route("/", methods=["GET"])
def find():
    content = request.json
    # name=content['name']
    cond = ["id", "term", "sessionPeriod", "billNo", "billName",
            "billOrg", "ststusid", "billProposer", "billCosignator"]
    data = {}
    if(isinstance(content,dict)):
        for i in cond:
            if (i in content.keys()):
                data[i] = content[i]
    data = proposalModal.find(data)
    return Response(json.dumps(data["data"], cls=MyEncoder), mimetype='application/json')


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
