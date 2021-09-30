import json
from model import (politicianModel, userModel)
from app import MyEncoder
import json
from linebot.models import (
    URITemplateAction, TextSendMessage, ImageSendMessage, StickerSendMessage, QuickReply, QuickReplyButton, MessageAction, URIAction, ButtonsTemplate)


class lineModule:

    @staticmethod
    def handle_messenge(event):
        print(event)
        msg = event.message.text
        if(msg == "我要查詢政治人物"):
            return TextSendMessage(text="點選想查詢人物城市所在",
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(
                                           label='台北市', text='台北市')),
                                       QuickReplyButton(action=MessageAction(
                                           label='新北市', text='新北市')),
                                       QuickReplyButton(action=MessageAction(
                                           label='桃園市', text='桃園市')),
                                       QuickReplyButton(action=MessageAction(
                                        label='台中市', text='台中市')),
                                       QuickReplyButton(action=MessageAction(
                                           label='台南市', text='台南市')),
                                       QuickReplyButton(action=MessageAction(
                                           label='高雄市', text='高雄市'))
                                   ]))
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
        elif(msg == "我要查詢選區"):
            return TextSendMessage(text="點選所在城市",
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(
                                           label='台北市', text='台北市')),
                                       QuickReplyButton(action=MessageAction(
                                           label='新北市', text='新北市')),
                                       QuickReplyButton(action=MessageAction(
                                           label='桃園市', text='新北市')),
                                       QuickReplyButton(action=MessageAction(
                                        label='台中市', text='新北市')),
                                       QuickReplyButton(action=MessageAction(
                                           label='台南市', text='新北市')),
                                       QuickReplyButton(action=MessageAction(
                                           label='高雄市', text='新北市'))
                                   ]))
        elif(msg == "新北市"):
            return TextSendMessage(text="點選所在區域",
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(
                                           label='土城區', text='新北市第十選舉區')),
                                       QuickReplyButton(action=MessageAction(
                                           label='三峽區', text='新北市第十選舉區')),
                                       QuickReplyButton(action=MessageAction(
                                           label='金山區', text='新北市第十選舉區')),
                                       QuickReplyButton(action=MessageAction(
                                        label='萬里區', text='新北市第十選舉區')),
                                       QuickReplyButton(action=MessageAction(
                                           label='石門區', text='新北市第一選舉區')),
                                       QuickReplyButton(action=MessageAction(
                                           label='淡水區', text='新北市第一選舉區'))
                                   ]))
        
        elif(msg == "選舉專區"):
            return TextSendMessage(text="點選所想看的內容",
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(
                                           label='投票這六不', text='投票這六不')),
                                       QuickReplyButton(action=MessageAction(
                                           label='投票三口訣', text='投票三口訣')),
                                       QuickReplyButton(action=MessageAction(
                                           label='投票三寶', text='投票三寶')),
                                       QuickReplyButton(action=MessageAction(
                                        label='投票這五步', text='投票這五步')),
                                       QuickReplyButton(action=URIAction(
                                           label='點我看更多',
                                           uri='https://taipei.app/#/election'
                                       ))

                                   ]))
        elif(msg == "投票這六不"):
            return TextSendMessage(text="點選所想看的內容",
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(
                                           label='投票這六不', text='投票這六不')),
                                       QuickReplyButton(action=MessageAction(
                                           label='投票三口訣', text='投票三口訣')),
                                       QuickReplyButton(action=MessageAction(
                                           label='投票三寶', text='投票三寶')),
                                       QuickReplyButton(action=MessageAction(
                                        label='投票這五步', text='投票這五步')),
                                       QuickReplyButton(action=URIAction(
                                           label='點我看更多',
                                           uri='https://taipei.app/#/election'
                                       ))

                                   ]))
        elif(msg == "投票三寶"):
            return TextSendMessage(text="點選所想看的內容",
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(
                                           label='投票這六不', text='投票這六不')),
                                       QuickReplyButton(action=MessageAction(
                                           label='投票三口訣', text='投票三口訣')),
                                       QuickReplyButton(action=MessageAction(
                                           label='投票三寶', text='投票三寶')),
                                       QuickReplyButton(action=MessageAction(
                                        label='投票這五步', text='投票這五步')),
                                       QuickReplyButton(action=URIAction(
                                           label='點我看更多',
                                           uri='https://taipei.app/#/election'
                                       ))

                                   ]))
        elif(msg == "投票三口訣"):
            return TextSendMessage(text="點選所想看的內容",
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(
                                           label='投票這六不', text='投票這六不')),
                                       QuickReplyButton(action=MessageAction(
                                           label='投票三口訣', text='投票三口訣')),
                                       QuickReplyButton(action=MessageAction(
                                           label='投票三寶', text='投票三寶')),
                                       QuickReplyButton(action=MessageAction(
                                        label='投票這五步', text='投票這五步')),
                                       QuickReplyButton(action=URIAction(
                                           label='點我看更多',
                                           uri='https://taipei.app/#/election'
                                       ))

                                   ]))
        elif(msg == "投票這五步"):
            return TextSendMessage(text="點選所想看的內容",
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(
                                           label='投票這六不', text='投票這六不')),
                                       QuickReplyButton(action=MessageAction(
                                           label='投票三口訣', text='投票三口訣')),
                                       QuickReplyButton(action=MessageAction(
                                           label='投票三寶', text='投票三寶')),
                                       QuickReplyButton(action=MessageAction(
                                        label='投票這五步', text='投票這五步')),
                                       QuickReplyButton(action=URIAction(
                                           label='點我看更多',
                                           uri='https://taipei.app/#/election'
                                       ))


                                   ]))
        

        else:
            return TextSendMessage(text="")
