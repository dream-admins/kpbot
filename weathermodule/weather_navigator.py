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

        i18n.load_path.append(self.__current_path)
        i18n.set('file_format', 'json')
        i18n.set('locale', 'uk')

    def handle_weather(self, request):
        __message_text = request.message.text
        connect = WeatherConnector()

        if __message_text.endswith('nav'):
            self.__viber.send_messages(request.sender.id, [TextMessage(text=self.__get_res('forecastTitle'), keyboard=self.__get_keyboard())])
        elif __message_text.endswith('now'):
            self.__viber.send_messages(request.sender.id, [TextMessage(text=connect.init_connection("observations").to_string(), keyboard=self.__get_keyboard())])
        elif __message_text.endswith("tomorrow"):
            weather_item = connect.init_connection("observations")
            SAMPLE_RICH_MEDIA = {
                  "Type": "rich_media",
                  "BgColor": "#FFFFFF",
                  "Buttons": [
                    {
                      "Columns": 6,
                      "Rows": 2,
                      "ActionType": "none",
                      "ActionBody": "none",
                      "TextVAlign": "top",
                      "TextHAlign": "center",
                      "Text": "<b>"+weather_item.get_day_name()+" - " + weather_item.get_current_date()
                              + "</b><br>Станом на: <b>"+weather_item.get_current_time()+"</b>"
                              + "<br><b>" + str(weather_item.get_temperature()) + " &#8451;</b>" ,
                      "TextOpacity": 100,
                      "TextSize": "regular"
                    },
                    {
                        "Columns": 3,
                        "Rows": 5,
                        "ActionType": "none",
                        "ActionBody": "none",
                        "TextVAlign": "middle",
                        "BgMedia": "https://raw.githubusercontent.com/dream-admins/kpbot/master/weather_icons/PNGs/"
                                 + str(weather_item.get_icon_code()) + ".png"
                    }

                  ]
                }

            SAMPLE_ALT_TEXT = "upgrade now!"

            message = RichMediaMessage(rich_media=SAMPLE_RICH_MEDIA, alt_text=SAMPLE_ALT_TEXT, min_api_version=2.0)
            self.__viber.send_messages(request.sender.id, [message])

    def __get_res(self, msg):
        return i18n.t('weather_navigator.' + msg)


    def __get_keyboard(self):
        with open(self.__current_path + '/weather_default_keyboard.json') as f:
            return json.load(f)


# "Columns": 6,
# "Rows": 1,
# "BgColor": "#454545",
# "BgMediaType": "gif",
# "BgMedia": "http://www.url.by/test.gif",
# "BgLoop": "true",
# "ActionType": "open-url",
# "Silent": "true",
# "ActionBody": "www.tut.by",
# "Image": "www.tut.by/img.jpg",
# "TextVAlign": "middle",
# "TextHAlign": "left",
# "Text": "<b>example</b> button",
# "TextOpacity": 10,
# "TextSize": "regular"
