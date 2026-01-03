from src.API_vacancies import HH
from unittest.mock import patch


def test_api_connections(api_connections):
    assert api_connections.status_code == 200


@patch.object(HH, "load_vacancies")
def test_load_vacancies(mock_api_connections):
    mock_api_connections.return_value = [
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

    hh_api = HH()
    hh_vacancies = hh_api.load_vacancies("Программист", "3", 10)
    assert hh_vacancies == [
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
