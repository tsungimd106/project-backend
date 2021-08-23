from flask import Blueprint, request, Response
from model import politicianModel
import json
from coder import MyEncoder
from .util import ret, checkParm, normalize_query


politicianAPI = Blueprint("politician", __name__, url_prefix="/politician")


@politicianAPI.route("/list", methods=["GET"])
def list():
    print(request.args.get("name"))
    data = request.args
    query_params = normalize_query(data)
    print(query_params)
    return ret(politicianModel.getList({}))


@politicianAPI.route("/<p_id>", methods=["GET"])
def detail(p_id):
    return ret(politicianModel.getDetail({"id": p_id}))


@politicianAPI.route("/area", methods=["GET"])
def area():
    return ret(politicianModel.getArea())


@politicianAPI.route("/name", methods=["GET"])
def name():
    return ret(politicianModel.getName())


@politicianAPI.route("/term", methods=["GET"])
def term():
    return ret(politicianModel.getTerm())


@politicianAPI.route("/cond", methods=["GET"])
def cond():
    return ret(politicianModel.getCond())


@politicianAPI.route("/score", methods=["GET"])
def getScore():
    return ret(politicianModel.schedule())


@politicianAPI.route("/score", methods=["POST"])
def score():
    content = request.json
    cond = ["user_id", "policy_id", "ps_id", "remark"]
    result = checkParm(cond, content)
    if(isinstance(result,dict)):
        politicianModel.score(
            content["user_id"], content["policy_id"], content["ps_id"], content["remark"])
        return ret({"success": True, "message": "評分成功"})
    else:
        return ret({"success": False, "message": result})
