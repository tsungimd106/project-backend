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


@politicianAPI.route("/", methods=["PATCH"])
def changeProfile():
    content = request.json
    account = content["id"]
    cond = ["term", "sex", "partyid", "areaid", "positionid"]
    data = {}
    for i in cond:
        if(i in content.keys()):
            data[i] = content[i]
    data = politicianModel.changePolitician(data, id)
    result = {"success": False, "message": "修改異常", "data": data}
    if(data["success"]):
        result["success"] = True
        result["message"] = "修改成功"
    return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')
