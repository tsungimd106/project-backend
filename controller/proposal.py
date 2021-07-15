from flask import Blueprint, request, Response
from model import proposalModel
import json
from coder import MyEncoder
from .util import (ret, checkParm, normalize_query, normalize_query_param)


proposalAPI = Blueprint("proposal", __name__, url_prefix="/proposal")


@proposalAPI.route("", methods=["GET"])
def find():
    cond = ["id", "term",  "ststusid", ]
    content = request.args
    print(content)
    after = normalize_query(content)
    print(after)
    # print(normalize_query_param(content))

    return ret(proposalModel.list(after))


@proposalAPI.route("/msg", methods=["POST"])
def msg():
    content = request.json
    cond = ["user_id", "content", "article_id", "parent_id"]
    t = checkParm(cond, content)
    if(isinstance(t, dict)):
        data = proposalModel.msg(
            account=content[cond[0]], mes=content[cond[1]], article_id=content[cond[2]], parent_id=content[cond[3]])
    else:
        data = {"success": False, "mes": t}

    return ret(data)


@proposalAPI.route("/<p_id>", methods=["GET"])
def search(p_id):
    user_id = request.args.get("user_id")
    return ret(proposalModel.msgList(p_id, user_id))


@proposalAPI.route("/vote", methods=["POST"])
def vote():
    content = request.json
    cond = ["user_id", "sp_id", "proposal_id"]
    t = checkParm(cond, content)
    if(isinstance(t, str)):
        data = {"success": False, "mes": t}

    else:
        data = proposalModel.vote(
            userid=content[cond[0]], sp_id=content[cond[1]], proposal_id=content[cond[2]])

    return ret(data)


@proposalAPI.route("/save", methods=["GET"])
def getSave():
    content = request.args.get("user_id")

    cond = ["user_id"]
    # result = checkParm(cond, content)
    if(content == ""):
        return ret({"success": False, "message": "請登入"})
    else:
        return ret(proposalModel.getSave(content))


@proposalAPI.route("/save", methods=["POST"])
def save():
    content = request.json
    cond = ["user_id", "proposal_id"]
    result = checkParm(cond, content)
    if(isinstance(result, dict)):
        return ret(proposalModel.save(content["user_id"], content["proposal_id"]))
    else:
        return ret({"success": False, "message": result})


@proposalAPI.route("/report", methods=["POST"])
def report():
    content = request.json
    cond = ["user_id", "message_id", "remark", "rule"]
    t = checkParm(cond, content)
    if(isinstance(t, dict)):
        return ret(proposalModel.report(content["user_id"], content["message_id"], content["remark"], content["rule"]))
    else:
        return ret({"success": False, "message": t})


@proposalAPI.route("/rule", methods=["GET"])
def rule():
    return ret(proposalModel.rule())


@proposalAPI.route("/cond", methods=["GET"])
def cond():
    return ret(proposalModel.getCond())
