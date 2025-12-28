def class_to_dict(vacancies: object) -> dict:
    """Метод преобразует объект класса в словарь"""

    return {'name': vacancies.name,
            'url': vacancies.url,
            'experience': vacancies.experience,
            'schedule': vacancies.schedule,
            'salary': vacancies.salary_from,
            'description': vacancies.description}

