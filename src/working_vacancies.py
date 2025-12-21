class Vacancy:
    __slots__ = ('name', 'url', 'experience','schedule' , 'salary', 'description')

    def __init__(self, name, url, experience, schedule, salary, description):
        self.name = name
        self.url = url
        self.experience = experience
        self.schedule = schedule
        self.salary = salary #по умолчанию должен быть 0
        self.description = description

    def __lt__(self, other):
        if not isinstance(other, int):
            raise TypeError("Значение заработной платы справа должен иметь тип int")

        sal = other if isinstance(other, int) else other.seconds
        return self.salary < sal




class VacancyManager:

    def __init__(self):
        self.vacancies = []

    def add_vacancies(self, vacancies):
        self.vacancies.extend(vacancies)

    def remove_vacancy(self, vacancy):
        self.vacancies.remove(vacancy)