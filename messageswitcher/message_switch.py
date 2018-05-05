# coding=utf-8
import i18n
import os
import json

from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberMessageRequest

from message_commander import MessageCommander


class MessageSwitcher:

    def __init__(self, viber):
        self.__viber = viber
        self.__msg_commander = MessageCommander(viber)
        self.__current_path = os.path.dirname(__file__)

        i18n.load_path.append(self.__current_path)
        i18n.set('file_format', 'json')
        i18n.set('locale', 'uk')


    def disassembleReq(self, req):
        if isinstance (req, ViberConversationStartedRequest):
            self.__viber.send_messages(req.user.id,
                                       [TextMessage(text=i18n.t(self.__get_res('helloText'), userName=req.user.name), keyboard=self.__get_keyboard())])
        elif isinstance(req, ViberMessageRequest):
            self.__msg_commander.define_command(req)




    def __get_res(self, msg):
        return 'message_switch.' + msg

    def __get_keyboard(self):
        with open(self.__current_path + '/default_keyboard.json') as f:
            return json.load(f)
