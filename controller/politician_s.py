from flask import Blueprint, request, Response
from model import politicianModel
import json
from coder import MyEncoder


politicianProfile = Blueprint("politician", __name__, url_prefix="/politician")


@politicianProfile.route("/find", methods=["GET"])
def find():
    content = request.json
    # name=content['name']
    cond = ["id", "term", "sex", "partyid", "areaid", "positionid"]
    data = {}
    for i in cond:
        if (i in content.keys()):
            data[i] = content[i]
    data = politicianModel.find(data)    
    return Response(json.dumps(data["data"], cls=MyEncoder), mimetype='application/json')

@politicianProfile.route("/", methods=["PATCH"])
def changeProfile():
    content = request.json
    account = content["id"]
    cond = [ "term", "sex", "partyid", "areaid", "positionid"]
    data = {}
    for i in cond:
        if(i in content.keys()):
            data[i] = content[i]
    data = politicianModel.changePolitician(data, id)
    result = {"success": False, "message": "修改異常", "data": data}
    if(data["success"]):
        result["success"]=True
        result["message"]="修改成功"
    return Response(json.dumps(result, cls=MyEncoder), mimetype='application/json')
