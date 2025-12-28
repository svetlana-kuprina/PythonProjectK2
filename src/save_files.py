import json
import os
from abc import ABC, abstractmethod


class SaveFile(ABC):
    """класс для работы с файлами"""

    @abstractmethod
    def save_to_file(self, vacancies: list) -> None:
        """методы для добавления вакансий в файл"""
        pass

    @abstractmethod
    def load_from_file(self) -> None:
        """методы для получения данных из файла"""
        pass

    def load_write_from_file(self, new_vacancies_list: list) -> None:
        """методы для получения данных из файла проверки их на уникальность и записи в файл"""
        pass

    @abstractmethod
    def del_vacancies_file(self) -> None:
        """методы для удаления информации о вакансиях"""
        pass


class SaveFilesJSON(SaveFile):
    """класс для работы с файлами JSON"""

    def __init__(self, name_file="vacancies.json") -> None:
        self.name_file = name_file
        self.pathfile = os.path.join(os.path.dirname(__file__), "../data", self.name_file)

    def save_to_file(self, vacancies: list) -> None:
        """методы для добавления вакансий в файл JSON"""

        with open(self.pathfile, "w", encoding="UTF-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=2)

    def load_from_file(self) -> None:
        """методы для получения данных из файла"""

        try:
            with open(self.pathfile, "r", encoding="UTF-8") as file:
                vacancies = json.load(file)

            return vacancies

        except FileNotFoundError:
            print("Не верный путь к файлу")
        except json.decoder.JSONDecodeError:
            return []

    def load_write_from_file(self, new_vacancies_list: list) -> None:
        """методы для получения данных из файла проверки их на уникальность и записи в файл"""

        with open(self.pathfile, "r+", encoding="UTF-8") as file:
            try:
                file_vacancies = json.load(file)
            except json.decoder.JSONDecodeError:
                return []
            try:
                for vacancy in file_vacancies:
                    for new_vacancy in new_vacancies_list:
                        if vacancy["url"] == new_vacancy["url"]:
                            new_vacancies_list.remove(new_vacancy)
                        else:
                            continue

                file_vacancies.extend(new_vacancies_list)
                file.seek(0)
                json.dump(file_vacancies, file, ensure_ascii=False, indent=2)
                file.truncate()
            except Exception as e:
                print(e)

    def del_vacancies_file(self) -> None:
        with open("file.txt", "w"):
            pass
