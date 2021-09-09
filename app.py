# app.py
import os
from flask import Flask, Response, request, abort,redirect
from coder import MyEncoder
import requests

import json
import sys
from model import line
from controller import( user,politician,proposal,manage)

#  ----------------------- 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage,TextSendMessage
)
from model import userModel
from controller.util import ret

from flask_cors import CORS
from flask_restplus import Resource, Api


app = Flask(__name__)

app.register_blueprint(user.userProfile)
app.register_blueprint(politician.politicianAPI)
app.register_blueprint(proposal.proposalAPI)
app.register_blueprint(manage.manageAPI)
line_bot_api = LineBotApi(
    "Oh4trCIb7cjh58YORcKoqqCHjKzg16U1HCCcVWrbBpplSt2LrUEzBNH+Yyjq5TWU9XG8b7LLZFxbAgYQW8nRufgVZeF4586KCRzFvxN82PLeWFEkKPbgGQwC7wV8BJ+3D5fCqFqE6f7/Js57OwQ1ZgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("41121bf7a06d828660ce43a388cded2f")
#  ----------------------- 

api =Api(app)

# api.add_namespace(politicianApi)
# api.add_namespace(userApi)
# api.add_namespace(proposalApi)
CORS(app)


 


@app.route('/lineLogin', methods=["GET","OPTIONS"])
def home():
    userLineID=""
    args=request.args.get("code")
    
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    r=requests.post("https://api.line.me/oauth2/v2.1/token",headers=header,data={
        "grant_type":"authorization_code","code":str(args),
        "redirect_uri":"https://test1022ntubimd.herokuapp.com/lineLogin",
        "client_id":"1656404446",
        "client_secret":"eb6bb1fe08f647ecf52b1e0978543a4d"
    })
    rText=r.text

    if("error" not in rText):
        # print(r.text)        
        j=json.loads(r.text)
        token=j["access_token"]        
        secondR=requests.get("https://api.line.me/v2/profile",headers={"Authorization": f"Bearer {token}"})
        secondText=secondR.text
        if("error" not in secondText):
            secondJ=json.loads(secondText)
            # print(secondJ["userId"])
            userLineID=secondJ["userId"]   
            print(userLineID)
            data=userModel.getUserByLine(userLineID)
            urlCond=f"?lineId={userLineID}"
            for i in data["data"]:
                urlCond+=f'&user_id={i["id"].decode()}&identity={i["identity"]}'
                
            return redirect(f"https://taipei.app/#/redirect{urlCond}")
            
        else:  
            print(secondText)  
            return ret({"success":False})
    else:
        print(rText)
        return ret({"success":False})

@app.route("/line")
def line():
    args=request.args.get("access_token")
    return "line"
    
#  ----------------------- 
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    return 'OK'
    app.logger.info("Request body: " + body)
   # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    data = line.lineModule.handle_messenge(event)    
    line_bot_api.reply_message(event.reply_token, data)


