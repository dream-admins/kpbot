import os
import logging
import i18n
from flask import Flask, request, Response

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

from message_switch import MessageSwitcher


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def main():
    i18n.load_path.append(os.path.dirname(__file__))
    i18n.set('file_format', 'json')

    token = None
    with open(os.path.dirname(__file__) + '/token_file', 'r') as tokenFile:
        token = tokenFile.readline()


    app = Flask(__name__)
    viber = Api(BotConfiguration(
        name=i18n.t(__get_res('botName')),
        avatar=i18n.t(__get_res('image-url')),
        auth_token=token
    ))

    messageSwitcher = MessageSwitcher(viber)


    @app.route('/' + token, methods=['POST'])
    def incoming():
        logger.debug("received request. post data: {0}".format(request.get_data()))

        viber_request = viber.parse_request(request.get_data().decode('utf-8'))
        messageSwitcher.disassembleReq(viber_request)

    #     if isinstance(viber_request, ViberMessageRequest):
    #         message = viber_request.message
    #         # lets echo back
    #         userId = viber_request.sender.id
    #         sendMessage(viber, userId)
    # # viber.send_messages(viber_request.sender.id, [message])
    #     elif isinstance(viber_request, ViberSubscribedRequest):
    #         viber.send_messages(viber_request.get_user.id, [
    #             TextMessage(text="thanks for subscribing!")
    #         ])
    #     elif isinstance(viber_request, ViberFailedRequest):
    #         logger.warn("client failed receiving message. failure: {0}".format(viber_request))

        return Response(status=200)

    app.run()


def __get_res(message):
    return 'bot_runner.' + message

if __name__ == "__main__":
    main()
