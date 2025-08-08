from typing import Any

import psycopg2


class DBManager:
    """Класс для работы с базой данных"""

    def __init__(
        self, dbname: str, password: int, host: str = "localhost", user: str = "postgres", port: int = 5432
    ) -> None:
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self._params = {
            "dbname": self.dbname,
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "port": self.port,
        }

    @property
    def params(self) -> dict:
        return self._params

    def get_companies_and_vacancies_count(self) -> Any:
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        conn = psycopg2.connect(**self.params)

        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute(
                "SELECT employer_name, count(*) as count FROM vacancies "
                "INNER JOIN employers USING (employer_id) "
                "GROUP BY employer_name"
            )
            result = cur.fetchall()

        return result

    def get_all_vacancies(self) -> Any:
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        conn = psycopg2.connect(**self.params)

        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute(
                "SELECT employer_name, vacancy_name, salary_from, salary_to, vacancy_url FROM vacancies "
                "INNER JOIN employers USING (employer_id)"
            )
            result = cur.fetchall()

        return result

    def get_avg_salary(self) -> Any:
        """
        Получает среднюю зарплату по вакансиям.
        """
        conn = psycopg2.connect(**self.params)

        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute(
                "SELECT AVG(salary_from), AVG(salary_to) FROM vacancies " "WHERE salary_from > 0 or salary_to > 0;"
            )
            result = cur.fetchall()

        return result

    def get_vacancies_with_higher_salary(self) -> Any:
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        conn = psycopg2.connect(**self.params)

        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute(
                "SELECT vacancy_name, salary_from FROM vacancies "
                "WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies);"
            )
            result = cur.fetchall()

        return result

    def get_vacancies_with_keyword(self, keyword: str) -> Any:
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова.
        """
        conn = psycopg2.connect(**self.params)

        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute(f"SELECT vacancy_name, vacancy_url FROM vacancies WHERE vacancy_name ILIKE ('%{keyword}%')")
            result = cur.fetchall()

        return result
