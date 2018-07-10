import requests
from film_item import FilmItem
from bs4 import BeautifulSoup

class DrugbaFilmParser:
    def __init__(self):
        self.__url = 'http://drugba-kino.com.ua'
        self.__headers = {'Host': 'drugba-kino.com.ua',
                          'Connection': 'keep-alive',
                          'Pragma': 'no-cache',
                          'Cache-Control': 'no-cache',
                          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                          'Upgrade-Insecure-Requests': '1',
                          'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
                          'Referer': 'https://www.google.com.ua/',
                          'Accept-Encoding': 'gzip, deflate, sdch',
                          'Accept-Language': 'ru,en-US;q=0.8,en;q=0.6,uk;q=0.4',
                          'X-Compress': 'null'
                          }
    def __get_html(self):
        response = requests.request(method='GET', url=self.__url, headers=self.__headers)
        return response.content

    def __get_elements(self, tag, html, className):
        soup = BeautifulSoup(html, 'lxml')
        elements = soup.find_all(tag, class_=className)
        return elements

    def get_film_elements(self):
        film_list = []
        html = self.__get_html()
        filmElements = self.__get_elements('div', html, 'product_preview_case')
        for filmElement in filmElements:

            image_url = filmElement.find('img', class_='product_preview_pictures').get('src').split('image=/').pop()
            image_url = self.__url + '/' + image_url
            film_block = filmElement.find('div', class_='product_preview_name_div')
            film_name = film_block.find('a').getText().strip()
            use_3d = False if film_block.find('div', class_='product_preview_3D') == None else True

            country_year = filmElement.find('div', class_='product_preview_country_year').getText().strip()

            genre_block = list(filmElement.find_all('div', class_='product_preview_genre'))
            time = ''.join("" if not char.isdigit() else char for char in genre_block.pop().getText())
            genre = genre_block.pop().getText().strip()

            item = FilmItem()
            item.set_name(film_name)
            item.set_image_url(image_url)
            item.set_country_year(country_year)
            item.set_time(time)
            item.set_preview_3d(use_3d)
            item.set_genre(genre)
            film_list.append(item)

        return film_list