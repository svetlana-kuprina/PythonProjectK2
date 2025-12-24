class Vacancy:
    __slots__ = ('name', 'url', 'experience','schedule' , 'salary', 'description')

    def __init__(self, name, url, experience, schedule, salary, description):
        self.name = name
        self.url = url
        self.experience = experience if experience else None
        self.schedule = schedule
        self.salary = salary if salary else 0
        self.description = description

    def __lt__(self, other):
        if not isinstance(other.salary, int):
            raise TypeError("Значение заработной платы справа должен иметь тип int")
        return self.salary < other.salary

    def __gt__(self, other):
        if not isinstance(other.salary, int):
            raise TypeError("Значение заработной платы справа должен иметь тип int")
        return self.salary > other.salary

    def __eq__(self, other):
        if not isinstance(other.salary, int):
            raise TypeError("Значение заработной платы справа должен иметь тип int")
        return self.salary == other.salary

    def __ne__(self, other):
        if not isinstance(other.salary, int):
            raise TypeError("Значение заработной платы справа должен иметь тип int")
        return self.salary != other.salary


    @staticmethod
    def cast_to_object_list(vacancy_list):
        objects_list = []
        for vacancy in vacancy_list:
            object_vacancy = Vacancy(name=vacancy["name"],
                                     url=vacancy["url"],
                                     experience=vacancy["experience"],
                                     schedule=vacancy["schedule"],
                                     salary=vacancy["salary"],
                                     description=vacancy["snippet"])
            objects_list.append(object_vacancy)
        return objects_list





class VacancyManager:

    def __init__(self):
        self.vacancies = []

    def add_vacancies(self, vacancies):
        self.vacancies.extend(vacancies)

    def remove_vacancy(self, vacancy):
        self.vacancies.remove(vacancy)