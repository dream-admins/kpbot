import i18n
import json
import os

from viberbot.api.messages import TextMessage
from film_navigator import FilmNavigator
from weather_navigator import WeatherNavigator

__author__ = 'dream-admins'


class MessageCommander:

    def __init__(self, viber):
        self.__viber = viber
        self.__weather_nav = WeatherNavigator(viber)
        self.__film_nav = FilmNavigator(viber, self)
        self.__current_path = os.path.dirname(__file__)

        i18n.load_path.append(self.__current_path)
        i18n.set('file_format', 'json')
        i18n.set('locale', 'uk')

    def define_command(self, request):
        __message_text = request.message.text
        if __message_text.startswith('weather'):
            self.__weather_nav.handle_weather(request)
        elif __message_text.startswith('film'):
            self.__film_nav.handleFilms(request)
        elif __message_text == 'go_back':
            self.__viber.send_messages(request.sender.id,
                                       [TextMessage(text=i18n.t(self.__get_res('goBackTitle'),), keyboard=self.get_keyboard())])

    def __get_res(self, msg):
        return 'message_switch.' + msg

    def get_keyboard(self):
        if self.__current_path is None:
            self.__current_path = os.path.dirname(__file__)

        with open(self.__current_path + '/default_keyboard.json') as f:
            return json.load(f)