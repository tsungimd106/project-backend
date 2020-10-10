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
    return(json.dumps(data, cls=MyEncoder))
