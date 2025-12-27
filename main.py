from os import write

from src.API_vacancies import HH
from src.save_files import SaveFilesJSON
from src.working_vacancies import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HH()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.load_vacancies('Программист','3', 10)
# for vacancy in hh_vacancies:
#     print(vacancy)

 # Преобразование набора данных из JSON в список объектов
vacancies_object_list = Vacancy.cast_to_object_list(hh_vacancies)
#print(vacancies_object_list)

# Преобразует из объектов класса в список словарей для записи в файл
new_vacancies_list = Vacancy.vacancies_list(vacancies_object_list)



# Работа с файлом
json_saver = SaveFilesJSON()
# Создание файла и запись в пустой файл информации
json_saver.save_to_file(new_vacancies_list)
# Чтение из файла
from_file = json_saver.load_from_file()


# Дозапишем файл с новым набором вакансий
hh_api2 = HH()
hh_vacancies2 = hh_api2.load_vacancies('Программист','3', 10)
# Преобразование набора данных из JSON в список объектов
vacancies_object_list2 = Vacancy.cast_to_object_list(hh_vacancies2)
# Преобразует из объектов класса в список словарей для записи в файл
new_vacancies_list2 = Vacancy.vacancies_list(vacancies_object_list2)
json_saver2 = SaveFilesJSON()
json_saver2.load_write_from_file(new_vacancies_list2)




#
# # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

