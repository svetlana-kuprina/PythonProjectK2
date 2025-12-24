from src.API_vacancies import HH
from src.working_vacancies import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HH()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.load_vacancies('Программист','3', 10)
for vacancy in hh_vacancies:
    print(vacancy)

 # Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
print(vacancies_list)

#
# # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

