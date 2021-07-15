# app.py
import os
from flask import Flask, Response, request, abort
from coder import MyEncoder

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


 


@app.route('/get', methods=["GET","OPTIONS"])
def home():
    return 'good from backend'
    
#  ----------------------- 
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    
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


