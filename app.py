# app.py
import os
from flask import Flask, Response, request, abort
from spider.politican import area
from coder import MyEncoder
import json
import sys
from model.line import lineModule
from controller import( user,politician,proposal)
from flask import render_template
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage
)

app = Flask(__name__)
app.register_blueprint(user.userProfile)
app.register_blueprint(politician.politicianProfile)
app.register_blueprint(proposal.proposal)
line_bot_api = LineBotApi(
    "JFkmqeDZk4E5qf6W2awhVwtKPKCYXCG7BXu8PgaSv3GAS4PxqYGtC/96OTk3L0sG6zZnZtRtJRA2htHC2v6gAw01UE7KE2RYeGdvZF9epTkIH8DjmeeuA32vz3pcTnG7n5XzxU8jDyYzUeFlmI2SXgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("02402a84858b56f54b5a34fc1928d4a4")


@app.route('/', methods=["POST"])
def line():
    return "ok"


@app.route('/', methods=["GET"])
def home():
    return 'good from backend'




@app.route('/area')
def findArea():
    data = area.findArea()
    print(type(data))
    # data= "".join( chr( val ) for val in data )
    # return Response(json.dumps(data, cls=MyEncoder), mimetype='application/json')
    return "enter area"


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

@app.route('/', methods=["GET"])
def find():
    return 'show'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    data = lineModule.handle_messenge(event)
    line_bot_api.reply_message(event.reply_token, data)


