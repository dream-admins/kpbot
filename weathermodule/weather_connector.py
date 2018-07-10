__author__ = 'dream-admins'

import certifi
import json
from urllib3 import PoolManager
import datetime
from weather_item import WeatherItem

class WeatherConnector:
    def __init__(self):
        self.__time_format = '%H:%M'
        self.__observ_url = "https://api.weather.com/v1/geocode/48.693344/26.557896/observations/" \
                            "current.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&language=uk&units=m"
        self.__forecast_url = "https://api.weather.com/v2/turbo/vt1dailyforecast?apiKey=d522aa97197fd864d36b418f39ebb323&" \
                              "format=json&geocode=48.68%2C26.59&language=uk-UA&units=m"
        self.__start_day_index = 1

    def get_observation(self):

        jsObj = json.loads(self.__get_weather_resp(self.__observ_url).data.decode('utf-8'))
        return self.__make_observation_weather_item(jsObj)

    def get_weekend_weather(self):
        jsObj = json.loads(self.__get_weather_resp(self.__forecast_url).data.decode('utf-8'))
        allDays = jsObj['vt1dailyforecast']['validDate']

        start_range = 1
        end_range = 7

        saturday_index = 5
        sunday_index = 0

        start_index = self.__get_day_index(start_range, end_range, allDays, saturday_index)
        end_index = self.__get_day_index(start_range, end_range, allDays, sunday_index)

        return self.__make_weather_more_item(jsObj, start_index, end_index)



    def get_forecats(self, end_day_Index):

        jsObj = json.loads(self.__get_weather_resp(self.__forecast_url).data.decode('utf-8'))
        return self.__make_weather_more_item(jsObj, self.__start_day_index, end_day_Index)
    
    def __make_weather_more_item(self, jsonObj, start_day_index, endDayIndex):
        weather_list = []
        daily_forecast = jsonObj['vt1dailyforecast']

        for index in range(start_day_index, endDayIndex):
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


    def __make_observation_weather_item(self, jsonObj):
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

    def __get_day_index(self, start_range, end_range, allDays, condition_index):
        for index in range(start_range, end_range):
            date_time = self.__get_formated_date(allDays[index], None)
            week_day = datetime.datetime.strptime(date_time, '%d/%m/%Y').weekday()

            if week_day == condition_index:
                return index

        return None
