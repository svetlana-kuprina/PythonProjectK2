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


class FileManager:
    def save_to_file(self, vacancies, filename):
        with open(filename, 'w') as file:
            for vacancy in vacancies:
                file.write(f"{vacancy}\n")  # Предполагаем, что vacancy — это строка

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            return file.readlines()  # Возвращаем список строк