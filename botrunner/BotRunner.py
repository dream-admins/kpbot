from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import KeyboardMessage, RichMediaMessage
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

import i18n
import os

import time
import logging
import sched
import threading
import json

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

i18n.load_path.append(os.path.dirname(__file__))
i18n.set('file_format', 'json')
i18n.set('locale', 'uk')

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='KmBot',
    avatar='http://viber.com/avatar.jpg',
    auth_token='47bcc3f5e867d0b6-fdfcaa277e7a2a95-e98ca8adc6516d78'
))


@app.route('/47bcc3f5e867d0b6-fdfcaa277e7a2a95-e98ca8adc6516d78', methods=['POST'])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))

    viber_request = viber.parse_request(request.get_data().decode('utf-8'))
    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        # lets echo back
        userId = viber_request.sender.id
        sendMessage(userId)
#        viber.send_messages(viber_request.sender.id, [message])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)

def sendMessage(senderId):
    startup_keyboard = {
        "Type": "keyboard",
        "Buttons": [{
                    "Columns": 6,
                    "Rows": 1,
                    "BgColor": "#2db9b9",
                    "BgMediaType": "gif",
                    "BgMedia": "http://www.url.by/test.gif",
                    "BgLoop": True,
                    "ActionType": "open-url",
                    "ActionBody": "www.tut.by",
                    "Image": "www.tut.by/img.jpg",
                    "Text": "Key text",
                    "TextVAlign": "middle",
                    "TextHAlign": "center",
                    "TextOpacity": 60,
                    "TextSize": "regular"
                    }]

    }
    viber.send_messages(senderId, [TextMessage(text="thanks for subscribing!", keyboard=startup_keyboard)])
    logger.debug("message send");


if __name__ == "__main__":
    app.run()