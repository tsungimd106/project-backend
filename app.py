# app.py
import os
from flask import Flask, Response, request, abort
from coder import MyEncoder
import json
import sys
# from model.line import lineModule
# from controller import( user_old,politician,proposal)

#  ----------------------- 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage
)
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_cors import CORS
from flask_restplus import Resource, Api
from controller.user import userApi
from controller.proposal import proposalApi
from controller.politician import politicianApi

app = Flask(__name__)
# app.register_blueprint(user_old.userProfile)
# app.register_blueprint(politician.politicianProfile)
# app.register_blueprint(proposal.proposal)
line_bot_api = LineBotApi(
    "JFkmqeDZk4E5qf6W2awhVwtKPKCYXCG7BXu8PgaSv3GAS4PxqYGtC/96OTk3L0sG6zZnZtRtJRA2htHC2v6gAw01UE7KE2RYeGdvZF9epTkIH8DjmeeuA32vz3pcTnG7n5XzxU8jDyYzUeFlmI2SXgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("02402a84858b56f54b5a34fc1928d4a4")
#  ----------------------- 

CORS(app)
api =Api(app)

api.add_namespace(politicianApi)
api.add_namespace(userApi)
# api.add_namespace(proposalApi)



@app.route('/', methods=["POST"])
def line():
    return "ok"


@app.route('/', methods=["GET"])
def home():
    return 'good from backend'
    
#  ----------------------- 
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)
    print(body)
   # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    data = lineModule.handle_messenge(event)
    line_bot_api.reply_message(event.reply_token, data)


