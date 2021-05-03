from flask import Blueprint, request, Response
from model import (userModel,manageModel)
import json
from coder import MyEncoder
from flask import app
from .util import (ret, checkParm)


manageAPI = Blueprint("manage", __name__, url_prefix="/manage")

@manageAPI.route("/politician", methods=["PATCH"])
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
    return ret(result)


@manageAPI.route("/proposal", methods=["PATCH"])
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

@manageAPI.route("/identity",methods=["GET"])
def identity():    
    return ret(manageModel.identity())

@manageAPI.route("/identity",methods=["POST"])
def setIdentity():
    content=request.json
    t=checkParm(["user_id","identity"])
    if(t==""):
        return ret(manageModel.setIdentity(content.user_id, content.identity))
    else :
        return ret(t)
@manageModel.route("/identity/user",methods=["GET"])
def identityUser():
    content=request.json
    t=checkParm(["identity"], content)
    if(t==""):
        return ret(manageModel.manager())
    else :
        return ret(t)
    