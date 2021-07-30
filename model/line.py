import json
from model import (politicianModel, userModel)
from app import MyEncoder
import json
from linebot.models import (
     URITemplateAction,TextSendMessage, ImageSendMessage, StickerSendMessage, QuickReply, QuickReplyButton, MessageAction, URIAction,ButtonsTemplate)


class lineModule:

    @staticmethod
    def handle_messenge(event):
        print(event)
        msg = event.message.text
        if(msg == "我要查詢政治人物"):
            return TextSendMessage(text="輸入政治人物名稱")
        elif(msg == "蔣萬安"):
            return TextSendMessage(text=msg,
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=URIAction(
                                           label='點我進網站',
                                           uri='https://taipei.app/#/figure/492' 
                                       ))
                                   ]))
        elif(msg == "個人檔案"):
            webUserid = userModel.getUserIdByLine(event.source.user_id)
            return TextSendMessage(text=msg,
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=URIAction(
                                           label='個人檔案',
                                           uri='https://taipei.app/redirect/%s/user' % webUserid
                                       ))
                                   ]))
        else:
            return TextSendMessage(text=msg)


