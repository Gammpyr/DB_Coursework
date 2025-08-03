

class Employer:
    def __init__(self, employer_id, name, alternate_url, vacancies_url, open_vacancies):
        self.id = employer_id
        self.name = name
        self.alternate_url = alternate_url
        self.vacancies_url = vacancies_url
        self.open_vacancies = open_vacancies
        self.vacancies = []



class Vacancy:
    def __init__(self, vacancy_id, name, salary, url, employer, requirements, experience):
        self.id = vacancy_id
        self.name = name
        self.salary = salary
        self.url = url
        self.employer = employer
        self.requirements = requirements
        self.experience = experience