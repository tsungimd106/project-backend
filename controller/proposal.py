from flask import Blueprint, request, Response
from model import proposalModal
import json
from coder import MyEncoder
from .util import (ret, checkParm)


proposalAPI = Blueprint("proposal", __name__, url_prefix="/proposal")


@proposalAPI.route("/", methods=["GET"])
def find():
    cond = ["id", "term",  "ststusid", ]
    return ret(proposalModal.list({}))


@proposalAPI.route("/msg", methods=["POST"])
def msg():
    content = request.json
    cond = ["user_id", "content", "article_id", "parent_id"]
    t = checkParm(cond, content)
    if(t == ""):
        data = proposalModal.msg(
            account=content[cond[0]], mes=content[cond[1]], article_id=content[cond[2]], parent_id=content[cond[3]])
    else:
        data = {"success": False, "mes": t}
    print(data)
    return ret(data)


@proposalAPI.route("/msg/<p_id>", methods=["GET"])
def search(p_id):
    return ret(proposalModal.msgList(p_id))


@proposalAPI.route("/vote", methods=["POST"])
def vote():
    content = request.json
    cond = ["user_id", "sp_id", "proposal_id"]
    t = checkParm(cond, content)
    if(t == ""):
        data = proposalModal.vote(
            userid=content[cond[0]], sp_id=content[cond[1]], proposal_id=content[cond[2]])
    else:
        data = {"success": False, "mes": t}
    print(data)
    return ret(data)


@proposalAPI.route("/", methods=["PATCH"])
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
        result["success"] = True
        result["message"] = "修改成功"
        return ret(result)
