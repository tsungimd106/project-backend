from flask import Blueprint, request, Response
from model import politicianModel
import json
from coder import MyEncoder
from .util import ret, checkParm, normalize_query


politicianAPI = Blueprint("politician", __name__, url_prefix="/politician")


@politicianAPI.route("/list", methods=["GET"])
def list():
    print(request.args.get("name"))
    # content = request.json
    # print(content)
    # cond = ["id", "term", "sex", "partyid", "areaid", "positionid"]
    # data = {}
    # for i in cond:
    #     if (i in content.keys()):
    #         data[i] = content[i]
    # print(data)
    query_params = normalize_query(request.args)
    print(query_params)
    return ret(politicianModel.getList({}))


@politicianAPI.route("/<p_id>", methods=["GET"])
def detail(p_id):
    temp=politicianModel.getDetail({"id":p_id})
    print(temp)
    policy=[]
    policyContent=""
    policyCateogry=[]
    now=0
    for i in temp["data"][1]["data"]:
        if now!=i["id"]:
            policy.append({"content":policyContent,"cateogry":policyCateogry,"id":now})
            now=i["id"]            
            policyContent=i["content"]
            policyCateogry=[]
            policyCateogry.append(i["name"])
        else:
            policyCateogry.append(i["name"])
        
    temp["data"][1]["data"]=policy   
    return ret(temp)


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
    cond = ["user_id", "policy_id", "ps_id","remark"]
    result = checkParm(cond, content)
    if(result == ""):
        politicianModel.score(content["user_id"], content["policy_id"], content["ps_id"],content["remark"])
        return ret({"success":True,"message":"評分成功"})
    else:
        return ret({"success": False, "message": result})
