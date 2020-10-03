from flask import Blueprint, request,Response
from user import userModel
import json
from coder import MyEncoder


userProfile = Blueprint("user", __name__, url_prefix="/user")

@userProfile.route("/login", methods=["POST"])
def login():
    content=request.json
    account = content['account']
    password = content["password"]
    data=userModel.login(account,password)
    # if(data)!=None: 
    #     message="登入成功"
    
    return Response(json.dumps(data,cls=MyEncoder), mimetype='application/json')

@userProfile.route("/sign", methods=["POST"])
def sign():
    account = request.values.get("account")
    password = request.values.get("password")
    age = request.values.get("age")
    sex = request.values.get("sex")
    return("enter sign")


