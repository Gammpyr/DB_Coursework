class Employer:
    """
    Класс для хранения информации о работодателе
    """

    def __init__(
        self, employer_id: int, name: str, alternate_url: str, vacancies_url: str, open_vacancies: int
    ) -> None:
        self.id = employer_id
        self.name = name
        self.alternate_url = alternate_url
        self.vacancies_url = vacancies_url
        self.open_vacancies = open_vacancies
        self.vacancies: list = []

    def __str__(self) -> str:
        return (
            f"ID: {self.id}\n"
            f"Название: {self.name}\n"
            f"URL: {self.alternate_url}\n"
            f"Количество вакансий: {self.open_vacancies}\n"
        )


class Vacancy:
    """
    Класс для хранения информации о вакансии
    """

    def __init__(
        self,
        vacancy_id: int,
        name: str,
        salary: dict,
        url: str,
        employer_id: int,
        requirements: str,
        responsibility: str,
        experience: str,
    ) -> None:
        self.id = vacancy_id
        self.name = name
        self.salary = salary
        self.url = url
        self.employer_id = employer_id
        self.requirements = requirements
        self.responsibility = responsibility
        self.experience = experience

    def __str__(self) -> str:
        return (
            f"ID: {self.id}\n"
            f"Название: {self.name}\n"
            f"URL: {self.url}\n"
            f"ID Работодателя: {self.employer_id}\n"
            f"Зарплата: от: {self.salary['from'] if self.salary and self.salary['from'] else None}, "
            f"до: {self.salary['to'] if self.salary and self.salary['to'] else None}\n"
            f"Опыт работы: {self.experience}\n"
            f"Требования: {self.requirements}\n"
            f"Обязанности: {self.responsibility}\n"
        )
