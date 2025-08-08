import psycopg2


def create_tables(db_name: str, params: dict) -> None:
    """Создает таблицы employers и vacancies"""
    conn = psycopg2.connect(dbname=db_name, **params)

    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE employers ("
            "employer_id integer PRIMARY KEY,"
            "employer_name varchar(50),"
            "alternate_url varchar(100) ,"
            "vacancies_url varchar(100),"
            "open_vacancies integer"
            ")"
        )
        cur.execute(
            "CREATE TABLE vacancies ("
            "vacancy_id integer PRIMARY KEY,"
            "vacancy_name varchar(100),"
            "salary_from integer,"
            "salary_to integer,"
            "vacancy_url varchar(100),"
            "employer_id integer REFERENCES employers(employer_id),"
            "requirements text,"
            "responsibility text,"
            "experience varchar(20)"
            ")"
        )

    conn.close()


def fill_tables(db_name: str, params: dict, employers_info: list) -> None:
    """Заполняет таблицы employers и vacancies информацией о работодателях и вакансиях"""
    conn = psycopg2.connect(dbname=db_name, **params)

    conn.autocommit = True

    with conn.cursor() as cur:
        for employer in employers_info:
            cur.execute(
                "INSERT INTO employers VALUES (%s, %s, %s, %s, %s)",
                (employer.id, employer.name, employer.alternate_url, employer.vacancies_url, employer.open_vacancies),
            )

            vacancies = [
                (
                    vacancy.id,
                    vacancy.name,
                    vacancy.salary["from"] if vacancy.salary else None,
                    vacancy.salary["to"] if vacancy.salary else None,
                    vacancy.url,
                    vacancy.employer_id,
                    vacancy.requirements,
                    vacancy.responsibility,
                    vacancy.experience,
                )
                for vacancy in employer.vacancies
            ]

            cur.executemany("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", vacancies)

    conn.close()


class DBworker:
    """Класс для работы с базой данных"""

    def __init__(self, password: int, host: str = "localhost", user: str = "postgres", port: int = 5432) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self._params = {"host": self.host, "user": self.user, "password": self.password, "port": self.port}

    @property
    def params(self) -> dict:
        return self._params

    @params.setter
    def params(self, value: dict) -> None:
        """Обновляет словарь self.params"""
        self._params.update(value)

    def create_database(self, db_name: str) -> None:
        """
        Создаёт базу данных с указанным именем
        """
        conn = psycopg2.connect(dbname="postgres", **self.params)

        conn.autocommit = True
        # self.drop_database(db_name)

        with conn.cursor() as cur:
            cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
            cur.execute(f"CREATE DATABASE {db_name}")

        conn.close()

    def drop_database(self, db_name: str) -> None:
        """Удаляет базу данных"""
        conn = psycopg2.connect(dbname="postgres", **self.params)

        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"DROP DATABASE IF EXISTS {db_name}")

        conn.close()
