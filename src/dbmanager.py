import psycopg2


class DBManager:
    """Класс для работы с базой данных"""

    def __init__(self, dbname, password, host='localhost', user='postgres', port=5432):
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self._params = {'dbname': self.dbname,
                        'host': self.host,
                        'user': self.user,
                        'password': self.password,
                        'port': self.port}

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        pass

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        pass

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.
        """
        pass

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        pass

    def get_vacancies_with_keyword(self):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова.
        """
        pass
