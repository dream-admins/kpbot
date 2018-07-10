import i18n
import json
import os
from viberbot.api.messages import TextMessage, RichMediaMessage
from weather_connector import WeatherConnector

__author__ = 'dream-admins'

class WeatherNavigator:
    def __init__(self, viber):
        self.__viber = viber
        self.__current_path = os.path.dirname(__file__)
        self.__tomorrow_day_index = 2
        self.__5_days_index = 6

        i18n.load_path.append(self.__current_path)
        i18n.set('file_format', 'json')
        i18n.set('locale', 'uk')

    def handle_weather(self, request):
        __message_text = request.message.text
        connector = WeatherConnector()

        if __message_text.endswith('nav'):
            self.__viber.send_messages(request.sender.id, [TextMessage(text=self.__get_res('forecastTitle'),
                                                                       keyboard=self.__get_keyboard())])
        elif __message_text.endswith('now'):
            self.__send_rich_message(connector.get_observation(), request)

        elif __message_text.endswith("tomorrow"):
            self.__send_rich_message(connector.get_forecats(self.__tomorrow_day_index), request)
        elif __message_text.endswith("weekend"):
            self.__send_rich_message(connector.get_weekend_weather(), request)
        elif __message_text.endswith("5_days"):
            self.__send_rich_message(connector.get_forecats(self.__5_days_index), request)

    def __get_res(self, msg):
        return i18n.t('weather_navigator.' + msg)

    def __get_message_to_send(self, weather_items):
        with open(os.path.dirname(__file__) +'/weather_message_blocks.json', 'r') as message_file:
            message_blocks = ''.join(str(line) for line in message_file.readlines())
            rich_message = self.__weather_message()
            for weather_item in weather_items:
                item_dictionary = weather_item.get_dict()
                msg = message_blocks
                for key,val in item_dictionary.items():
                    msg = msg.replace(key,val)
                blocks_json = json.loads(msg)
                rich_message["Buttons"] = rich_message["Buttons"] + blocks_json["Blocks"]

            return rich_message

    def __weather_message(self):
        weather_msg = {"Type": "rich_media",
                       "BgColor": "#006699",
                       "Buttons": []}
        return weather_msg

    def __send_rich_message(self, weather_items, req):
        self.__viber.send_messages(req.sender.id, [ RichMediaMessage(
            rich_media=self.__get_message_to_send(weather_items), min_api_version=2.0,
            keyboard=self.__get_keyboard())])


    def __get_keyboard(self):
        with open(self.__current_path + '/weather_default_keyboard.json') as f:
            return json.load(f)