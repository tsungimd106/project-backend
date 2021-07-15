import json
from model import (politicianModel,userModel)
from app import MyEncoder
import json
from linebot.models import (
    TextSendMessage, ImageSendMessage, StickerSendMessage, QuickReply, QuickReplyButton, MessageAction, URIAction)


class lineModule:

    @staticmethod
    def handle_messenge(event):
        print(event)       
        msg = event.message.text
        if(msg == "我要area"):
            return TextSendMessage(text=msg)
        elif(msg == "個人檔案"):         
            webUserid=userModel.getUserIdByLine(event.source.user_id )
            return TextSendMessage(text='請選擇以下服務',
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=URIAction(
                                           label='個人檔案',
                                           uri='https://taipei.app/#/redirect/%s/user' %webUserid
                                       ))
                                   ]))
        else:
            return TextSendMessage(text=msg)
