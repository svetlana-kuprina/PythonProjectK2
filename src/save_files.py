from abc import ABC, abstractmethod


class SaveFile(ABC):

    @abstractmethod
    def add_vacancies_file(self):
        """методы для добавления вакансий в файл"""
        pass

    @abstractmethod
    def reading_vacancies_file(self):
        """методы для получения данных из файла по указанным критериям"""
        pass

    @abstractmethod
    def del_vacancies_file(self):
        """методы для удаления информации о вакансиях"""
        pass


class SaveFilesJSON(SaveFile):
    def __init__(self, name_file):
        self.name_file = 'vacancies.json'
