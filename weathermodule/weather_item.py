__author__ = 'dream-admins'


class WeatherItem:
    def __init__(self):
        self.__day_name = None
        self.__current_date = None
        self.__current_time = None
        self.__sunrise = None
        self.__sunset = None
        self.__temperature = None
        self.__icon_code = None
        self.__phrase = None
        self.__feel_like = None
        self.__wind_direction = None
        self.__wind_speed = None
        self.__weather_dict = {}

    def get_day_name(self):
        return self.__day_name

    def set_day_name(self, day_name):
        self.__day_name = day_name

    def get_current_date(self):
        return self.__current_date

    def set_current_date(self, current_date):
        self.__current_date = current_date

    def get_current_time(self):
        return self.__current_time

    def set_current_time(self, current_time):
        self.__current_time = current_time

    def get_sunrise(self):
        return self.__sunrise

    def set_sunrise(self, sunrise):
        self.__sunrise = sunrise

    def get_sunset(self):
        return self.__sunset

    def set_sunset(self, sunset):
        self.__sunset = sunset

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def get_icon_code(self):
        return self.__icon_code

    def set_icon_code(self, icon_code):
        self.__icon_code = icon_code

    def get_phrase(self):
        return self.__phrase

    def set_phrase(self, phrase):
        self.__phrase = phrase

    def get_feel_like(self):
        return self.__feel_like

    def set_feel_like(self, fill_like):
        self.__feel_like = fill_like

    def get_wind_direction(self):
        return self.__wind_direction

    def set_wind_direction(self, wind_direction):
        self.__wind_direction = wind_direction

    def get_wind_speed(self):
        return self.__wind_speed

    def set_wind_speed(self, wind_speed):
        self.__wind_speed = wind_speed

    def get_dict(self):
        self.__weather_dict['%day_date_name'] = self.__day_name+ " - " + self.__current_date
        self.__weather_dict['%current_time'] = '' if self.__current_time is None else "Станом на: <b>"+self.__current_time+"</b>"
        self.__weather_dict['%feel_like'] = str(self.__feel_like)
        self.__weather_dict['%icon_code'] = str(self.__icon_code).zfill(2)
        self.__weather_dict['%temp'] = str(self.__temperature)
        self.__weather_dict['%phrase'] = self.__phrase
        self.__weather_dict['%wind_direction'] = self.__wind_direction
        self.__weather_dict['%wind_speed'] = str(self.__wind_speed)
        self.__weather_dict['%sunrise'] = self.__sunrise
        self.__weather_dict['%sunset'] = self.__sunset
        return self.__weather_dict


    def to_string(self):
        return "{0},{1},{2},{3},{4},{5}".format(self.__day_name, self.__current_date, self.__temperature, self.__icon_code,
                                           self.get_sunrise(), self.get_sunset())




