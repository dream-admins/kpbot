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

    def to_string(self):
        return "{0},{1},{2},{3},{4},{5}".format(self.__day_name, self.__current_date, self.__temperature, self.__icon_code,
                                           self.get_sunrise(), self.get_sunset())




