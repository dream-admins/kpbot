import os
import json
from viberbot.api.messages import TextMessage, RichMediaMessage

from drugba_parser import DrugbaFilmParser


class FilmNavigator:
    def __init__(self, viber, message_commander):
        self.__viber = viber
        self.__current_path = os.path.dirname(__file__)
        self.__message_cmd = message_commander
        self.__max_film_length = 5

    def handleFilms(self, request):
        __message_text = request.message.text
        parser = DrugbaFilmParser()
        if __message_text.endswith('nav'):
            self.__send_rich_message(parser.get_film_elements(), request)

    def __send_rich_message(self, film_items, req):
        self.__viber.send_messages(req.sender.id, [RichMediaMessage(
            rich_media=self.__get_message_to_send(film_items), min_api_version=2.0,
            keyboard=self.__message_cmd.get_keyboard())])

        if not 0 == len(film_items):
            self.__send_rich_message(film_items, req)

    def __get_message_to_send(self, film_items):
        with open(os.path.dirname(__file__) + '/film_message_blocks.json', 'r') as message_file:
            message_blocks = ''.join(str(line) for line in message_file.readlines())
            rich_message = self.__film_template_message()
            for index in range(0, len(film_items)):
                item_dictionary = film_items.pop().get_dict()
                msg = message_blocks
                for key, val in item_dictionary.items():
                    msg = msg.replace(key, val)
                blocks_json = json.loads(msg)
                rich_message["Buttons"] = rich_message["Buttons"] + blocks_json["Blocks"]
                if index // self.__max_film_length:
                    break

        return rich_message

    def __film_template_message(self):
        weather_msg = {"Type": "rich_media",
                       "BgColor": "#5F9EA0",
                       "Buttons": []}
        return weather_msg
