from flask import Blueprint, request, Response
from model import politicianModel
import json
from coder import MyEncoder
from .util import ret, checkParm


politicianAPI = Blueprint("politician", __name__, url_prefix="/politician")


@politicianAPI.route("/list", methods=["GET"])
def list():
    # content = request.json

    cond = ["id", "term", "sex", "partyid", "areaid", "positionid"]
    # data = {}
    # for i in cond:
    #     if (i in content.keys()):
    #         data[i] = content[i]
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





@politicianAPI.route("/score", methods=["GET"])
def getScore():
    return ret(politicianModel.schedule)


@politicianAPI.route("/score", methods=["POST"])
def score():
    content = request.json
    cond = ["user_id", "policy_id", "ps_id"]
    result = checkParm(cond, content)
    if(result == "")    {
        return ret({success: false, message: result})
    }
    else{
        return ret(politicianModel.score(content.user_id, content.policy_id, content.ps_id))
    }
