import pytest

from src.API_vacancies import HH
from src.working_vacancies import Vacancy


@pytest.fixture
def api_connections():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HH()
    hh_vacancies = hh_api.load_vacancies("Программист", "3", 10)
    return hh_api._api_connections()


@pytest.fixture
def vacancies_object_list():
    hh_vacancies = [
        {
            "id": "128937519",
            "premium": False,
            "name": "Программист",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "3", "name": "Екатеринбург", "url": "https://api.hh.ru/areas/3"},
            "salary": {"from": 65000, "to": None, "currency": "RUR", "gross": False},
            "salary_range": {
                "from": 65000,
                "to": None,
                "currency": "RUR",
                "gross": False,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": {"id": "MONTHLY", "name": "Раз в\xa0месяц"},
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Екатеринбург",
                "street": "Вишнёвая улица",
                "building": "69С",
                "lat": 56.830413,
                "lng": 60.658344,
                "description": None,
                "raw": "Екатеринбург, Вишнёвая улица, 69С",
                "metro": None,
                "metro_stations": [],
                "id": "17636684",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-12-22T09:15:35+0300",
            "created_at": "2025-12-22T09:15:35+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=128937519",
            "show_contacts": False,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/128937519?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/128937519",
            "relations": [],
            "employer": {
                "id": "11470108",
                "name": "Грация",
                "url": "https://api.hh.ru/employers/11470108",
                "alternate_url": "https://hh.ru/employer/11470108",
                "logo_urls": None,
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=11470108",
                "country_id": 1,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Пунктуальность. Стрессоустойчивость. Грамотность. Уверенная работа с ПК. Умение работать с оборудованием.",
                "responsibility": "HTML / CSS / PHP / JSON (вёрстка). Работа с базами данных MySQL. Работа с телеграм ботами (разной сложности). Построение сети внутри организации. ",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [
                {"id": "from_four_to_six_hours_in_a_day", "name": "Можно сменами по\xa04-6\xa0часов в\xa0день"}
            ],
            "working_time_modes": [],
            "accept_temporary": False,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
            "working_hours": [{"id": "HOURS_6", "name": "6\xa0часов"}, {"id": "HOURS_8", "name": "8\xa0часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": True,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]
    vacancies_object_list = Vacancy.cast_to_object_list(hh_vacancies)
    return vacancies_object_list


@pytest.fixture
def vacancies_list():
    return [
        {
            "id": "128937519",
            "premium": False,
            "name": "Программист",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "3", "name": "Екатеринбург", "url": "https://api.hh.ru/areas/3"},
            "salary": {"from": 65000, "to": None, "currency": "RUR", "gross": False},
            "salary_range": {
                "from": 65000,
                "to": None,
                "currency": "RUR",
                "gross": False,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": {"id": "MONTHLY", "name": "Раз в\xa0месяц"},
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Екатеринбург",
                "street": "Вишнёвая улица",
                "building": "69С",
                "lat": 56.830413,
                "lng": 60.658344,
                "description": None,
                "raw": "Екатеринбург, Вишнёвая улица, 69С",
                "metro": None,
                "metro_stations": [],
                "id": "17636684",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-12-22T09:15:35+0300",
            "created_at": "2025-12-22T09:15:35+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=128937519",
            "show_contacts": False,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/128937519?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/128937519",
            "relations": [],
            "employer": {
                "id": "11470108",
                "name": "Грация",
                "url": "https://api.hh.ru/employers/11470108",
                "alternate_url": "https://hh.ru/employer/11470108",
                "logo_urls": None,
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=11470108",
                "country_id": 1,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Пунктуальность. Стрессоустойчивость. Грамотность. Уверенная работа с ПК. Умение работать с оборудованием.",
                "responsibility": "HTML / CSS / PHP / JSON (вёрстка). Работа с базами данных MySQL. Работа с телеграм ботами (разной сложности). Построение сети внутри организации. ",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [
                {"id": "from_four_to_six_hours_in_a_day", "name": "Можно сменами по\xa04-6\xa0часов в\xa0день"}
            ],
            "working_time_modes": [],
            "accept_temporary": False,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
            "working_hours": [{"id": "HOURS_6", "name": "6\xa0часов"}, {"id": "HOURS_8", "name": "8\xa0часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": True,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]


@pytest.fixture
def list_vac():
    return [
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
