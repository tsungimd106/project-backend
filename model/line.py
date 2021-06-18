import json
from model import politicianModel
from app import MyEncoder
import json
from linebot.models import (
    TextSendMessage, ImageSendMessage, StickerSendMessage)


class lineModule:

    @staticmethod
    def handle_messenge(event):
        msg = event.message.text
        if(msg == "我要area"):
            return TextSendMessage(
                text=str(json.dumps(politicianModel.find(), cls=MyEncoder)))
        else:
            return TextSendMessage(text=msg)
