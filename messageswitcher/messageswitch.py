# coding=utf-8
import i18n
import os

from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberRequest



class MessageSwitcher:

    def __init__(self, viber):
        self.__viber = viber
        i18n.load_path.append(os.path.dirname(__file__))
        i18n.set('file_format', 'json')
        i18n.set('locale', 'uk')

    def disassembleReq(self, req):
        if isinstance (req, ViberConversationStartedRequest):
            self.__viber.send_messages(req.user.id,
                                       [TextMessage(text=i18n.t(self.__get_res('helloText'), userName=req.user.name), keyboard=self.__get_keyboard())])


    def __get_res(self, msg):
        return 'messageswitch.' + msg

    def __get_keyboard(self):
        return {
            "Type": "keyboard",
            "Buttons": [{
                "Columns": 3,
                "Rows": 2,
                "Text": "<font color=\"#494E67\">Погода</font>",
                "TextSize": "medium",
                "TextHAlign": "center",
                "TextVAlign": "bottom",
                "ActionType": "reply",
                "ActionBody": "weather",
                "Image": "https://lh3.googleusercontent.com/N5fvMCn_2mGgrfGOyOLxB_rxYJbut4AgdYygC4ZJphh3gepckm0orFJvLqVvueeR5vilWXc56mFJ23lty0_PQkrNDJblNuzwD-_fTHHunWC2bE85ZgdPcpTYMxnwibwjnI6XP9_341g1x7riAym4LoXQ9NoNqgbAS43_RY6j6sTSh8OhJUOdEXkQq59nimxFP_R1huttAAJ3VEsih0RDlg8tXW-PPCN5TI4YhZS6Xym4-mkfFcTIaQugaOnWjAqpWL532Zis-Xs4i1NR6qGhCbdNeZhFSWdiTYilw_CvZ6dBs-rwjpLOrYjXygFWxRlu5gUb6JwkXKGHt3slHTWBI8fWk1C7PfI5EKsiRqu8Erzil1u6C2DTNCRZRp4HT1DNlqSiGtzz6xaLO9Sjd3-TBZdlh-l85l3277ri8YLRCJyCstyMnn6XE1sJmDAyAWQGs6DD90QNnqrpcFwWxGfIdCoJzIQpcx7OF1pNGe0lmENcjQ-dFIXL6v7xXHm4TcYLSGRoSo0cEb_z8pw9YfD_QxYOI4RYbYFMxwJ1LnYprCV1KOD6MJB3o-r1tvDuPBFx=w1920-h553",
                "BgColor": "#f7bb3f"
            }, {
                "Columns": 3,
                "Rows": 2,
                "Text": "<font color=\"#494E67\">Non Smoking</font><br><br>",
                "TextSize": "medium",
                "TextHAlign": "center",
                "TextVAlign": "bottom",
                "ActionType": "reply",
                "ActionBody": "Non smoking",
                "BgColor": "#f6f7f9",
                "Image": "https://image.flaticon.com/icons/svg/227/227363.svg"
            }, {
                    "Columns": 3,
                    "Rows": 2,
                    "Text": "<font color=\"#494E67\">Non Smoking</font><br><br>",
                    "TextSize": "medium",
                    "TextHAlign": "center",
                    "TextVAlign": "bottom",
                    "ActionType": "reply",
                    "ActionBody": "Non smoking",
                    "BgColor": "#f6f7f9",
                    "Image": "https://image.flaticon.com/icons/svg/227/227363.svg"
                }
            ]

        }
