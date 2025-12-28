from src.utils import class_to_dict


class Vacancy:
    __slots__ = ('name', 'url', 'experience', 'schedule', 'salary_from', 'salary_to', 'description')

    def __init__(self, name, url, experience, schedule, salary, description):
        self.name = name
        self.url = url
        self.experience = experience if experience else None
        self.schedule = schedule
        self.salary_from = self.__salary_from_method(salary)
        self.salary_to = self.__salary_to_method(salary)
        self.description = description
        self.description = description

    def __salary_from_method(self, salary: dict | None) -> int:
        """Валидация заработной платы поля from"""

        if salary is None:
            salary = {'from': 0}
        elif salary['from'] is None:
            salary['from'] = 0

        return salary['from']

    def __salary_to_method(self, salary: dict | None) -> int:
        """Валидация заработной платы поля to"""

        if salary is None:
            salary = {'to': 0}
        elif salary['to'] is None:
            salary['to'] = 0
        return salary['to']

    def __lt__(self, other):
        """Сравнение заработной платы <"""

        # if not isinstance(other, int):
            # raise TypeError("Значение заработной платы справа должен иметь тип int")
        return (self.salary_from < other.salary_from) or (self.salary_to < other.salary_to)

    def __gt__(self, other):
        """Сравнение заработной платы >"""

        # if not isinstance(other, int):
            # raise TypeError("Значение заработной платы справа должен иметь тип int")
        return (self.salary_from > other.salary_from) or (self.salary_to > other.salary_to)

    def __eq__(self, other):
        """Сравнение заработной платы =="""

        # if not isinstance(other, int):
            # raise TypeError("Значение заработной платы справа должен иметь тип int")
        return (self.salary_from == other.salary_from) or (self.salary_to == other.salary_to)

    def __ne__(self, other):
        """Сравнение заработной платы !="""

        # if not isinstance(other, int):
        #     raise TypeError("Значение заработной платы справа должен иметь тип int")
        return (self.salary_from != other.salary_from) or (self.salary_to != other.salary_to)

    def __str__(self):
        """Вывод вакансии"""

        return (f"Наименование вакансии: {self.name},"
                f" Ссылка на вакансию: {self.url},"
                f" Опыт работы: {self.experience},"
                f" График работы: {self.schedule},"
                f" Зарплата: c {self.salary_from} по {self.salary_to},"
                f" Требования: {self.description}")

    @staticmethod
    def cast_to_object_list(vacancy_list: list) -> object:
        """Метод преобразование набора данных из JSON в список объектов"""

        objects_list = []
        for vacancy in vacancy_list:
            object_vacancy = Vacancy(name=vacancy["name"],
                                     url=vacancy["alternate_url"],
                                     experience=vacancy["experience"]['name'],
                                     schedule=vacancy["schedule"]['name'],
                                     salary=vacancy["salary"],
                                     description=vacancy["snippet"])
            objects_list.append(object_vacancy)
            # print(str(object_vacancy))
        return objects_list

    @staticmethod
    def vacancies_list(vacancy_object_list: list) -> list:
        """Метод преобразует список объектов класса Vacancy в список словарей"""

        if vacancy_object_list is None:
            return []
        new_vacancies_list = []
        for vacancy in vacancy_object_list:
            list_vacancy = class_to_dict(vacancy)
            new_vacancies_list.append(list_vacancy)
        return new_vacancies_list
