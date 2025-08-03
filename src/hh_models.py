

class Employer:
    """
    Класс для хранения информации о работодателе
    """
    def __init__(self, employer_id, name, alternate_url, vacancies_url, open_vacancies):
        self.id = employer_id
        self.name = name
        self.alternate_url = alternate_url
        self.vacancies_url = vacancies_url
        self.open_vacancies = open_vacancies
        self.vacancies = []

    def __str__(self):
        return (f'ID: {self.id}\n'
                f'Название: {self.name}\n'
                f'URL: {self.alternate_url}\n'
                f'Количество вакансий: {self.open_vacancies}\n')



class Vacancy:
    """
    Класс для хранения информации о вакансии
    """
    def __init__(self, vacancy_id, name, salary, url, employer_id, employer, requirements, responsibility, experience):
        self.id = vacancy_id
        self.name = name
        self.salary = salary
        self.url = url
        self.employer_id = employer_id
        self.employer = employer
        self.requirements = requirements
        self.responsibility = responsibility
        self.experience = experience

    def __str__(self):
        return (f'ID: {self.id}\n'
                f'Название: {self.name}\n'
                f'URL: {self.url}\n'
                f'Работодатель: {self.employer}\n'
                f'Зарплата: от: {self.salary['from'] if self.salary and self.salary['from'] else None}, '
                f'до: {self.salary['to'] if self.salary and self.salary['to'] else None}\n'
                f'Опыт работы: {self.experience}\n'
                f'Требования: {self.requirements}\n'
                f'Обязанности: {self.responsibility}\n'
                )