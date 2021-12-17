from flask import Blueprint, request, Response
from model.filter import DFAFilter
import model.proposalModel
from model.filter import DFAFilter
from model import proposalModel
import json
from coder import MyEncoder
from .util import (ret, checkParm, normalize_query, normalize_query_param)


proposalAPI = Blueprint("proposal", __name__, url_prefix="/proposal")


@proposalAPI.route("", methods=["GET"])
def find():
    cond = ["id", "term",  "status_id", "title"]
    content = request.args
    after = normalize_query(content)
    condData = {}
    for i in after.keys():
        if i in cond:
            condData[i] = after[i]
    data = {}
    data["cond"] = condData
    data["page"] = after["page"] if "page" in after.keys() else 0
    # for i in cond:

    return ret(proposalModel.pList(data))


@proposalAPI.route("/msg", methods=["POST"])
def msg():
    print("here")
    content = request.json
    cond = ["user_id", "content", "article_id", "parent_id"]
    t = checkParm(cond, content)
    if(isinstance(t, dict)):
        gfw = DFAFilter()
        gfw.parse()
        text = content["content"]
        result = gfw.filter(text)
        if len(str(content["content"]).replace("*", "")) == len(str(result).replace("*", "")):
            data = proposalModel.msg(
                account=content[cond[0]], mes=content[cond[1]], article_id=content[cond[2]], parent_id=content[cond[3]])
        else:
            data = {"success": False, "mes": "請確認是否有不雅字詞出現"}
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


@proposalAPI.route("/great", methods=["POST"])
def great():
    checkParm(["user_id", "m_id"])
    sqlstr = ""


@proposalAPI.route("/great", methods=["DELETE"])
def removeGreat(m_id):
    sqlstr = f"select * from great where id={m_id}"


@proposalAPI.route("/great", methods=["GET"])
def getGreat():
    checkParm(["m_id"])
    return ""


@proposalAPI.route("/save/del", methods=["POST"])
def removeSave():
    content = request.json
    cond = ["user_id", "proposal_id"]
    t = checkParm(cond, content)
    if(isinstance(t, dict)):
        return ret(proposalModel.removeSave(t["user_id"], t["proposal_id"]))
    else:
        return ret({"success": False, "message": t})
