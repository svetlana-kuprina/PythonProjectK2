from src.API_vacancies import HH
from src.save_files import SaveFilesJSON
from src.working_vacancies import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HH()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.load_vacancies('Программист', '3', 10)
# for vacancy in hh_vacancies:
#     print(vacancy)

# Преобразование набора данных из JSON в список объектов
vacancies_object_list = Vacancy.cast_to_object_list(hh_vacancies)
# print(vacancies_object_list)

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
hh_vacancies2 = hh_api2.load_vacancies('Программист', '3', 10)
# Преобразование набора данных из JSON в список объектов
vacancies_object_list2 = Vacancy.cast_to_object_list(hh_vacancies2)
# Преобразует из объектов класса в список словарей для записи в файл
new_vacancies_list2 = Vacancy.vacancies_list(vacancies_object_list2)
json_saver2 = SaveFilesJSON()
json_saver2.load_write_from_file(new_vacancies_list2)


# Функция для взаимодействия с пользователем
def user_interaction():
    """Функция для взаимодействия с пользователем"""

    platforms = ["HeadHunter"]

    search_query = input("Введите поисковый запрос: ")
    search_region = input("Введите код региона (можно посмотреть по ссылке https://api.hh.ru/areas/ ,"
                          " по умолчанию Россия): ")
    try:
        search_days = int(input("Введите количество дней поиска: "))
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except ValueError:
        print("количество дней поиска и количество вакансий для вывода в топ N  должен иметь тип int")
    salary_range = input("Введите диапазон зарплат: ").split('-')  # Пример: 100000 - 150000
    yes_no = str.upper(input("Сохранить результат отбора в файл? Y/N: "))

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh = HH()

    try:
        # Получение вакансий с hh.ru в формате JSON
        hh_request = hh.load_vacancies(search_query, search_region, search_days)

        # Преобразование набора данных из JSON в список объектов и вывод на экран
        vacancies_obj_list = Vacancy.cast_to_object_list(hh_request)
        print('Вакансии соответствующие отбору:')
        for vacancy in vacancies_obj_list:
            print(vacancy)

        # Сортировка списка объектов для вывода топ N

        sort_top = sorted(vacancies_obj_list, reverse=True)
        print(f'Топ {top_n}')
        for vacancy in sort_top[:top_n]:
            print(vacancy)

        salary_range_from = int(salary_range[0])
        salary_range_to = int(salary_range[1])
        print('Вакансии в заданном диапазоне зарплат:')
        list_search_sal = []
        for vac in vacancies_obj_list:
            if (salary_range_from < vac.salary_from) and (salary_range_to > vac.salary_to):
                print(vac)
                list_search_sal.append(vac)

        if yes_no == 'Y':
            # Преобразует из объектов класса в список словарей для записи в файл
            new_vac_list = Vacancy.vacancies_list(list_search_sal)

            # Работа с файлом
            j_saver = SaveFilesJSON()
            # Создание файла и запись в пустой файл информации
            j_saver.save_to_file(new_vac_list)
    except ValueError:
        print("Значение заработной платы справа должен иметь тип int")
    except UnboundLocalError:
        print("Не верно заданы параметры запроса для отбора вакансий")


if __name__ == "__main__":
    user_interaction()
