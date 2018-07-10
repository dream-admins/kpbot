class FilmItem:
    def __init__(self):
        self.__name = None
        self.__image_url = None
        self.__country_year = None
        self.__genre = None
        self.__time = None
        self.__preview_3d = None
        self.__film_dict = {}

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_image_url(self):
        return self.__image_url

    def set_image_url(self, image_url):
        self.__image_url = image_url

    def get_country_year(self):
        return self.__country_year

    def set_country_year(self, country_year):
        self.__country_year = country_year

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_time(self):
        return self.__genre

    def set_time(self, time):
        self.__time = time

    def get_preview_3d(self):
        return self.__preview_3d

    def set_preview_3d(self, preview_3d):
        self.__preview_3d = preview_3d

    def get_dict(self):
        self.__film_dict['%name'] = self.__name
        self.__film_dict['%image_url'] = self.__image_url
        self.__film_dict['%country&year'] = self.__country_year
        self.__film_dict['%genre'] = self.__genre
        self.__film_dict['%time'] = self.__time
        self.__film_dict['%3d'] = str(self.__preview_3d)
        return self.__film_dict

    def to_String(self):
        return ("\nName:{}\n Url:{}\n Country and Year:{}\n Genre:{}\n Time:{}\n Preview 3D:{}\n".format(
            self.__name,
            self.__image_url,
            self.__country_year,
            self.__genre,
            self.__time,
            self.__preview_3d))


