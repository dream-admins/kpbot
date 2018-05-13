__author__ = 'dream-admins'

import certifi
import json
from urllib3 import PoolManager
import datetime
from weather_item import WeatherItem

class WeatherConnector:
    def __init__(self):
        self.__time_format = '%H:%M'

    def get_observation(self):
        observ_url = "https://api.weather.com/v1/geocode/48.693344/26.557896/observations/" \
                     "current.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&language=uk&units=m"
        jsObj = json.loads(self.__get_weather_resp(observ_url).data.decode('utf-8'))
        return self.__make_weather_one_item(jsObj)

    def get_forecats(self, dayIndex):
        forecast_url = "https://api.weather.com/v2/turbo/vt1dailyforecast?apiKey=d522aa97197fd864d36b418f39ebb323&" \
                       "format=json&geocode=48.68%2C26.59&language=uk-UA&units=m"
        jsObj = json.loads(self.__get_weather_resp(forecast_url).data.decode('utf-8'))
        return self.__make_weather_more_item(jsObj, dayIndex)
    
    def __make_weather_more_item(self, jsonObj, dayIndex):
        weather_list = []
        daily_forecast = jsonObj['vt1dailyforecast']
        for index in range(1, dayIndex):
            weather_item = WeatherItem()
            weather_item.set_day_name(daily_forecast['dayOfWeek'][index])
            weather_item.set_current_date(self.__get_formated_date(daily_forecast['validDate'][index], None))
            weather_item.set_sunrise(self.__get_formated_date(daily_forecast['sunrise'][index], self.__time_format))
            weather_item.set_sunset(self.__get_formated_date(daily_forecast['sunset'][index], self.__time_format))

            dayObj = daily_forecast['day']
            weather_item.set_icon_code(dayObj['icon'][index])
            weather_item.set_phrase(dayObj['phrase'][index])
            weather_item.set_wind_direction(dayObj['windDirCompass'][index])
            weather_item.set_wind_speed(dayObj['windSpeed'][index])
            weather_item.set_temperature(dayObj['temperature'][index])
            weather_item.set_feel_like(dayObj['temperature'][index])
            weather_list.append(weather_item)
        return weather_list



    def __make_weather_one_item(self, jsonObj):
        weather_list = []
        weather_item = WeatherItem()
        observation_obj = jsonObj['observation']

        weather_item.set_day_name(observation_obj["dow"])
        weather_item.set_current_date(self.__get_formated_date(observation_obj['obs_time_local'], None))

        weather_item.set_current_time(self.__get_formated_date(observation_obj['obs_time_local'], self.__time_format))
        weather_item.set_sunrise(self.__get_formated_date(observation_obj['sunrise'], self.__time_format))
        weather_item.set_sunset(self.__get_formated_date(observation_obj['sunset'], self.__time_format))
        weather_item.set_icon_code(observation_obj['icon_code'])
        weather_item.set_phrase(observation_obj['phrase_32char'])
        weather_item.set_wind_direction(observation_obj['wdir_cardinal'])

        metric_obj = observation_obj['metric']
        weather_item.set_temperature(metric_obj['temp'])
        weather_item.set_feel_like(metric_obj['feels_like'])
        weather_item.set_wind_speed(metric_obj['wspd'])
        weather_list.append(weather_item)

        return weather_list


    def __get_formated_date(self, obs_time, date_format):
        current_time = datetime.datetime.strptime(obs_time, '%Y-%m-%dT%H:%M:%S%z')
        if date_format is None:
            return current_time.strftime("%d/%m/%Y")
        else:
            return current_time.strftime(date_format)

    def __get_weather_resp(self, url):
        http = PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        resp = http.request("GET", url)
        return resp

