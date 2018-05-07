__author__ = 'dream-admins'

import certifi
import json
from urllib3 import PoolManager
import datetime
from weather_item import WeatherItem

class WeatherConnector:
    def __init__(self):
        pass

    def init_connection(self, type):
        weather_item = WeatherItem()
        jsObj = json.loads(self.__get_weather_resp(type).data.decode('utf-8'))
        observation_obj = jsObj['observation']

        weather_item.set_day_name(observation_obj["dow"])
        weather_item.set_current_date(self.__get_formated_date(observation_obj['obs_time_local'], None))

        time_format = '%H:%M'
        weather_item.set_current_time(self.__get_formated_date(observation_obj['obs_time_local'], time_format))
        weather_item.set_sunrise(self.__get_formated_date(observation_obj['sunrise'], time_format))
        weather_item.set_sunset(self.__get_formated_date(observation_obj['sunset'], time_format))
        weather_item.set_icon_code(observation_obj['icon_code'])

        metric_obj = observation_obj['metric']
        weather_item.set_temperature(metric_obj['temp'])

        weather_item.to_string()
        return  weather_item

    def __get_formated_date(self, obs_time, date_format):
        current_time = datetime.datetime.strptime(obs_time, '%Y-%m-%dT%H:%M:%S%z')
        if date_format is None:
            return current_time.strftime("%d/%m/%Y")
        else:
            return current_time.strftime(date_format)

    def __get_weather_resp(self, type):
        http = PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        resp = http.request("GET", "https://api.weather.com/v1/geocode/48.693344/26.557896/" + type + "/current.json?"
                                          "apiKey=6532d6454b8aa370768e63d6ba5a832e&language=uk&units=m")
        return resp

