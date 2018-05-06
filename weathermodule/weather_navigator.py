import i18n
import json
import os
from viberbot.api.messages import TextMessage
from weather_connector import WeatherConnector

__author__ = 'dream-admins'

class WeatherNavigator:
    def __init__(self, viber):
        self.__viber = viber
        self.__current_path = os.path.dirname(__file__)

        i18n.load_path.append(self.__current_path)
        i18n.set('file_format', 'json')
        i18n.set('locale', 'uk')

    def handle_weather(self, request):
        __message_text = request.message.text
        if __message_text.endswith('nav'):
            self.__viber.send_messages(request.sender.id, [TextMessage(text=self.__get_res('forecastTitle'), keyboard=self.__get_keyboard())])
        elif __message_text.endswith('now'):
            connect = WeatherConnector()
            self.__viber.send_messages(request.sender.id, [TextMessage(text=connect.init_connection("observations").to_string(), keyboard=self.__get_keyboard())])

    def __get_res(self, msg):
        return i18n.t('weather_navigator.' + msg)


    def __get_keyboard(self):
        with open(self.__current_path + '/weather_default_keyboard.json') as f:
            return json.load(f)


