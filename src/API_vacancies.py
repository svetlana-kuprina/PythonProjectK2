from abc import ABC, abstractmethod

import requests



class VacanciesAPI(ABC):
    """Абстрактный класс для работы с API сервиса вакансий."""

    @abstractmethod
    def _api_connections(self):
        """Метод проверки API происходит проверка статус-кода ответа."""
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        """Метод получения данных API сервиса вакансий."""
        pass


class HH(VacanciesAPI):
    """Класс для работы с API сервиса вакансий с платформой hh.ru."""

    def __init__(self) -> None:
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 5, 'search_field': 'name', 'area': '3', 'period': 14}
        self.__base_url = "https://api.hh.ru"
        self.__vacancies = []


    def _api_connections(self, params: dict = None) -> int | None:
        """Метод проверки API. Происходит проверка статус-кода ответа hh.ru."""
        try:

            response = requests.get(self.__base_url, params=params)
            # response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            response.raise_for_status()
            return response.status_code
        except Exception as e:
            print(e)


    def load_vacancies(self, keyword:str) -> list:
        """Метод получения данных API сервиса вакансий с платформой hh.ru."""
        params = {'per_page': 1}
        print(self._api_connections(params))
        self.__params['text'] = keyword
        while self.__params.get('page') != 2:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
        return self.__vacancies