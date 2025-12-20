from src.API_vacancies import HH
from src.save_files import SaveFilesJSON

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HH()
# Получение вакансий с hh.ru в формате JSON
hh_vacancies = HH.load_vacancies(hh_api,'Программист Python')
print(hh_vacancies)
#
# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#
#
# f = SaveFilesJSON('vacancies.json')
# print(f)