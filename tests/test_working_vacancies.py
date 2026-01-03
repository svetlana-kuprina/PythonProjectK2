from src.working_vacancies import Vacancy


def test_cast_to_object_list(vacancies_list):
    assert type(Vacancy.cast_to_object_list(vacancies_list)) == list


def test_vacancies_list(vacancies_object_list):
    assert type(Vacancy.vacancies_list(vacancies_object_list)) == list
    assert Vacancy.vacancies_list(vacancies_object_list) == [
        {
            "name": "Программист",
            "url": "https://hh.ru/vacancy/128937519",
            "experience": "Нет опыта",
            "schedule": "Полный день",
            "salary": 65000,
            "description": {
                "requirement": "Пунктуальность. Стрессоустойчивость. Грамотность. Уверенная работа с ПК. Умение работать с оборудованием.",
                "responsibility": "HTML / CSS / PHP / JSON (вёрстка). Работа с базами данных MySQL. Работа с телеграм ботами (разной сложности). Построение сети внутри организации. ",
            },
        }
    ]


def test___str__(vacancies_object_list, capsys):
    for vacancies in vacancies_object_list:
        print(vacancies)
    captured = capsys.readouterr()
    assert captured.out == (
        "Наименование вакансии: Программист, Ссылка на вакансию: "
        "https://hh.ru/vacancy/128937519, Опыт работы: Нет опыта, График работы: "
        "Полный день, Зарплата: c 65000 по 0, Требования: {'requirement': "
        "'Пунктуальность. Стрессоустойчивость. Грамотность. Уверенная работа с ПК. "
        "Умение работать с оборудованием.', 'responsibility': 'HTML / CSS / PHP / "
        "JSON (вёрстка). Работа с базами данных MySQL. Работа с телеграм ботами "
        "(разной сложности). Построение сети внутри организации. '}\n"
    )
