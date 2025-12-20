from abc import ABC, abstractmethod

import requests



class VacanciesAPI(ABC):
    """Абстрактный класс для работы с API сервиса вакансий."""

    @abstractmethod
    def __api_connections(self):
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
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def __api_connections(self) -> int | None:
        """Метод проверки API. Происходит проверка статус-кода ответа hh.ru."""
        try:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            response.raise_for_status()
            return response.status_code
        except Exception as e:
            print(e)


    def load_vacancies(self, keyword:str) -> list:
        """Метод получения данных API сервиса вакансий с платформой hh.ru."""
        self.__params['text'] = keyword
        print(self.__api_connections())
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            self.__params['page'] += 1
            self.__params['per_page'] = 100
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
        return self.__vacancies