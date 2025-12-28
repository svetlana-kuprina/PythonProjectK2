import os

from src.save_files import SaveFilesJSON


def test_save_to_file(list_vac):
    """Тест создания и сохранения в файл"""

    json_saver = SaveFilesJSON("test.json")
    json_saver.save_to_file(list_vac)
    pathfile = os.path.join(os.path.dirname(__file__), "../data", "test.json")
    with open(pathfile, "r", encoding="utf-8") as f:
        file_content = f.read()
        assert file_content == (
            "[\n"
            "  {\n"
            '    "name": "Программист",\n'
            '    "url": "https://hh.ru/vacancy/128937519",\n'
            '    "experience": "Нет опыта",\n'
            '    "schedule": "Полный день",\n'
            '    "salary": 65000,\n'
            '    "description": {\n'
            '      "requirement": "Пунктуальность. Стрессоустойчивость. Грамотность. '
            'Уверенная работа с ПК. Умение работать с оборудованием.",\n'
            '      "responsibility": "HTML / CSS / PHP / JSON (вёрстка). Работа с базами '
            "данных MySQL. Работа с телеграм ботами (разной сложности). Построение сети "
            'внутри организации. "\n'
            "    }\n"
            "  }\n"
            "]"
        )


def test_save_to_file_with_employment_form(list_vac):
    """Тест дозаписи в файл с проверкой на добавление только уникальных данных"""
    vac1 = SaveFilesJSON("test.json")
    vac1.save_to_file(list_vac)
    vac2 = SaveFilesJSON("test.json")
    vac2.load_write_from_file(list_vac)
    pathfile = os.path.join(os.path.dirname(__file__), "../data", "test.json")
    with open(pathfile, "r", encoding="utf-8") as f:
        file_content = f.read()
        assert file_content == (
            "[\n"
            "  {\n"
            '    "name": "Программист",\n'
            '    "url": "https://hh.ru/vacancy/128937519",\n'
            '    "experience": "Нет опыта",\n'
            '    "schedule": "Полный день",\n'
            '    "salary": 65000,\n'
            '    "description": {\n'
            '      "requirement": "Пунктуальность. Стрессоустойчивость. Грамотность. '
            'Уверенная работа с ПК. Умение работать с оборудованием.",\n'
            '      "responsibility": "HTML / CSS / PHP / JSON (вёрстка). Работа с базами '
            "данных MySQL. Работа с телеграм ботами (разной сложности). Построение сети "
            'внутри организации. "\n'
            "    }\n"
            "  }\n"
            "]"
        )


def test_load_from_file():
    vac1 = SaveFilesJSON("test.json")
    file_content = vac1.load_from_file()
    assert file_content == [
        {
            "description": {
                "requirement": "Пунктуальность. Стрессоустойчивость. "
                               "Грамотность. Уверенная работа с ПК. Умение "
                               "работать с оборудованием.",
                "responsibility": "HTML / CSS / PHP / JSON (вёрстка). Работа "
                                  "с базами данных MySQL. Работа с телеграм "
                                  "ботами (разной сложности). Построение "
                                  "сети внутри организации. ",
            },
            "experience": "Нет опыта",
            "name": "Программист",
            "salary": 65000,
            "schedule": "Полный день",
            "url": "https://hh.ru/vacancy/128937519",
        }
    ]


def test_load_from_file_err(capsys):
    vac1 = SaveFilesJSON("test1.json")
    vac1.load_from_file()
    captured = capsys.readouterr()
    assert captured.out == "Не верный путь к файлу\n"
