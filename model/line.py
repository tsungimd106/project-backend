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
        elif (msg == "台北市"):
           
           
           
            return TextSendMessage(text="點選想查詢人物城市所在",
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=URIAction(
                                       label='蔣萬安',uri='https://taipei.app/#/figure/')),   
                                        QuickReplyButton(action=URIAction(
                                       label='何志偉',uri='https://taipei.app/#/figure/8')),
                                        QuickReplyButton(action=URIAction(
                                       label='吳思瑤',uri='https://taipei.app/#/figure/492')),
                                        QuickReplyButton(action=URIAction(
                                       label='林奕華',uri='https://taipei.app/#/figure/492')),
                                        QuickReplyButton(action=URIAction(
                                       label='林昶佐',uri='https://taipei.app/#/figure/492'))
                                   
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
                                           label='食品安全', text='食品安全')),
                                       QuickReplyButton(action=MessageAction(
                                           label='長期照顧', text='長期照顧')),
                                       QuickReplyButton(action=MessageAction(
                                           label='衛生社福', text='衛生社福')),
                                       QuickReplyButton(action=MessageAction(
                                           label='農業', text='農業')),
                                       QuickReplyButton(action=MessageAction(
                                           label='交通', text='交通')),
                                       QuickReplyButton(action=MessageAction(
                                           label='海洋', text='海洋')),
                                       QuickReplyButton(action=MessageAction(
                                           label='動物保育', text='動物保育')),
                                       QuickReplyButton(action=MessageAction(
                                           label='原住民', text='原住民')),
                                       QuickReplyButton(action=MessageAction(
                                           label='外交', text='外交')),
                                       QuickReplyButton(action=MessageAction(
                                           label='兩岸關係', text='兩岸關係')),
                                       QuickReplyButton(action=MessageAction(
                                           label='高齡化', text='高齡化')),
                                       QuickReplyButton(action=MessageAction(
                                           label='幼托育兒', text='幼托育兒')),
                                       QuickReplyButton(action=MessageAction(
                                           label='年改', text='年改')),
                                       QuickReplyButton(action=MessageAction(
                                           label='基礎建設', text='基礎建設')),
                                       QuickReplyButton(action=MessageAction(
                                           label='拒毒品', text='拒毒品')),
                                       QuickReplyButton(action=MessageAction(
                                           label='客家', text='客家')),
                                       QuickReplyButton(action=MessageAction(
                                           label='治安', text='治安')),
                                       QuickReplyButton(action=MessageAction(
                                           label='都市發展', text='都市發展')),
                                       QuickReplyButton(action=MessageAction(
                                           label='補助', text='補助')),
                                       QuickReplyButton(action=MessageAction(
                                           label='都市美化', text='都市美化')),
                                       QuickReplyButton(action=MessageAction(
                                           label='汽機車', text='汽機車')),
                                       QuickReplyButton(action=MessageAction(
                                           label='環保', text='環保')),
                                       QuickReplyButton(action=MessageAction(
                                           label='體育賽事', text='體育賽事')),
                                       QuickReplyButton(action=MessageAction(
                                           label='勞工就業', text='勞工就業')),
                                       QuickReplyButton(action=MessageAction(
                                           label='青年', text='青年')),
                                       QuickReplyButton(action=MessageAction(
                                           label='文創', text='文創')),
                                       QuickReplyButton(action=MessageAction(
                                           label='新住民', text='新住民'))

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
