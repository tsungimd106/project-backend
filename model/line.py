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

        elif(msg == "提案專區"):
            return TextSendMessage(text="點選所想看的類別",
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(
                                           label='財政金融', text='財政金融')),
                                       QuickReplyButton(action=MessageAction(
                                           label='教育', text='教育')),
                                       QuickReplyButton(action=MessageAction(
                                           label='內政', text='內政')),
                                       QuickReplyButton(action=MessageAction(
                                        label='司法及法制', text='司法及法制')),
                                       QuickReplyButton(action=MessageAction(
                                           label='科技', text='科技')),
                                       QuickReplyButton(action=MessageAction(
                                           label='觀光', text='觀光')),
                                       QuickReplyButton(action=MessageAction(
                                           label='國防', text='國防')),
                                       QuickReplyButton(action=MessageAction(
                                           label='性別平等', text='性別平等')),
                                       QuickReplyButton(action=MessageAction(
                                           label='食品安全', text='投票這五步')),
                                       QuickReplyButton(action=MessageAction(
                                           label='長期照顧', text='投票這五步')),
                                       QuickReplyButton(action=MessageAction(
                                           label='司法及法制', text='投票這五步'

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
