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
            weather_item = connect.init_connection("observations")
            SAMPLE_RICH_MEDIA = {
                "Type": "rich_media",
                "BgColor": "#006699",
                "Buttons": [
                    {
                        "Columns": 6,
                        "Rows": 1,
                        "ActionType": "none",
                        "ActionBody": "none",
                        "TextVAlign": "top",
                        "TextHAlign": "center",
                        "BgColor": "#006699",
                        "Text": "<i><font color=\"#FFFFFF\"><b>"+weather_item.get_day_name()+" - " + weather_item.get_current_date() + "</b></font><i>",
                        "TextOpacity": 100,
                        "TextBgGradientColor": "#454545"
                    },
                    {
                        "Columns": 6,
                        "Rows": 1,
                        "ActionType": "none",
                        "ActionBody": "none",
                        "TextOpacity": 100,
                        "BgColor": "#006699",
                        "Text": "<i><font color=\"#FFFFFF\">Станом на: <b>"+weather_item.get_current_time()+"</b></font></i>"
                    },
                    {
                        "Columns": 1,
                        "Rows": 2,
                        "ActionType": "none",
                        "ActionBody": "none",
                        "TextOpacity": 0,
                        "BgColor": "#006699",
                        "Text": "tex"
                    },
                    {
                        "Columns": 2,
                        "Rows": 2,
                        "ActionType": "none",
                        "ActionBody": "none",
                        "BgColor": "#006699",
                        "Image": "https://raw.githubusercontent.com/dream-admins/kpbot/master/weather_icons/PNGs/"
                                 + str(weather_item.get_icon_code()) + ".png"
                    },
                    {
                        "Columns": 3,
                        "Rows": 2,
                        "ActionType": "none",
                        "ActionBody": "none",
                        "BgColor": "#006699",
                        "Text": "<font color=\"#FFFFFF\" size=\"32\"><b>" + str(weather_item.get_temperature()) + " &#8451;</b></font>",
                        "TextVAlign": "top",
                        "TextHAlign": "left",
                    },
                    {
                        "Columns": 6,
                        "Rows": 1,
                        "ActionType": "none",
                        "ActionBody": "none",
                        "BgColor": "#006699",
                        "Text": "<font color=\"#FFFFFF\" size=\"16\"><b>" + weather_item.get_phrase() + "</b></font>",
                        "TextVAlign": "top",
                        "TextHAlign": "center",
                     },
                    {
                        "Columns": 6,
                        "Rows": 2,
                        "ActionType": "none",
                        "ActionBody": "none",
                        "BgColor": "#006699",
                        "Text": "<i><font color=\"#FFFFFF\">За відчуттям: <b>" + str(weather_item.get_feel_like()) + " &#8451;</b><br>Вітер: <b>"+
                                            weather_item.get_wind_direction() + " " + str(weather_item.get_wind_speed()) +" км/год</b><br>"+
                                            "Cхід: <b>" + weather_item.get_sunrise() + "</b>&emsp;&emsp;Захід: <b>" + weather_item.get_sunset() + "</b></font></i>",
                        "TextVAlign": "bottom",
                        "TextHAlign": "left",
                        "TextBgGradientColor": "#454545"
                    }


                    ]
            }

            message = RichMediaMessage(rich_media=SAMPLE_RICH_MEDIA, min_api_version=2.0, keyboard=self.__get_keyboard())
            self.__viber.send_messages(request.sender.id, [message])
        elif __message_text.endswith("tomorrow"):
            pass

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
