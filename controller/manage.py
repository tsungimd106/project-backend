from flask import Blueprint, request, Response
from controller.proposal import cond
from model import (userModel, manageModel, politicianModel,
                   proposalModel, articleModel)
import json
from coder import MyEncoder
from flask import app
from .util import (ret, checkParm)
from werkzeug.utils import secure_filename

manageAPI = Blueprint("manage", __name__, url_prefix="/manage")


# @manageAPI.route("/politician", methods=["PATCH"])
# def changeProfile():
#     content = request.json
#     account = content["id"]
#     cond = ["term", "sex", "partyid", "areaid", "positionid"]
#     data = {}
#     for i in cond:
#         if(i in content.keys()):
#             data[i] = content[i]
#     data = politicianModel.changePolitician(data, id)
#     result = {"success": False, "message": "修改異常", "data": data}
#     if(data["success"]):
#         result["success"] = True
#         result["message"] = "修改成功"
#     return ret(result)


# @manageAPI.route("/proposal", methods=["PATCH"])
# def changeProposal():
#     content = request.json
#     id = content["id"]
#     cond = ["term", "sessionPeriod", "billNo", "billName",
#             "billOrg", "ststusid", "billProposer", "billCosignator"]
#     data = {}
#     for i in cond:
#         if(i in content.keys()):
#             data[i] = content[i]
#     data = proposalModel.change(data, id)
#     result = {"success": False, "message": "修改異常", "data": data}
#     if(data["success"]):
#         result["success"] = True
#         result["message"] = "修改成功"
#         return ret(result)


@manageAPI.route("/identity", methods=["GET"])
def identity():
    return ret(manageModel.identity())

# 未完成
# 轉身分

@manageAPI.route("/identity", methods=["POST"])
def setIdentity():
    content = request.json
    cond = ["user_id", "identity"]
    t = checkParm(cond,content)
    if(isinstance(t, dict)):
        return ret(manageModel.setIdentity(t["user_id"], t["identity"]))
    else:
        return ret({"success": False, "message": t})


@manageAPI.route("/user", methods=["GET"])
def identityUser():
    return ret(manageModel.getUser())


@manageAPI.route("/report", methods=["GET"])
def getReport():
    return ret(manageModel.report())

# 檢舉審核
@manageAPI.route("/report", methods=["POST"])
def report():
    content = request.json
    cond = [ "check","report_id","manager_id","time"]
    t = checkParm(cond, content)
    if(isinstance(t, dict)):
        data = manageModel.reportCheck(
           check=content[cond[0]], report_id=content[cond[1]], manager_id=content[cond[2]],time=content[cond[3]])
        return ret(data)
    else:
        return ret({"success": False, "message": t})


# @manageAPI.route("article",methods=["POST"])
# def article():
#     content=request.json
#     cond=["article_id","content","version"]
#     t=checkParm(cond,content)
#     if t!="":
#         f=request.files[" "]
#         filename = secure_filename(file.filename)
#         f.save(os.path.join("tmp",filename))
#     else:
