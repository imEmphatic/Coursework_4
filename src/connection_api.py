import requests
from abc import ABC, abstractmethod


class AbstractApi(ABC):
    @abstractmethod
    def _get_response(self, per_page: int, text: str = ''):
        pass

    @abstractmethod
    def get_vacancies(self, per_page, text):
        pass


class HH(AbstractApi):
    """Класс для взаимодействия с API HeadHunter"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
    """Ссылка для получения БД"""

    def get_url(self):
        return self.__url
    """геттер для получения url и его возврата необходимый для теста"""

    def _get_response(self, per_page: int, text: str = ''):
        self.per_page = per_page
        self.text = text
        params = {'text': self.text, 'page': 0, 'per_page': self.per_page}
        response = requests.get(self.__url, params)
        return response
    """получение первичной информации о вакансиях с сайта"""

    def get_vacancies(self, per_page: int, text: str = ''):
        self.per_page = per_page
        self.text = text
        response = self._get_response(self.per_page, self.text)
        return response.json()['items']
    """перевод информации в json формат"""
