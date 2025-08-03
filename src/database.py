import psycopg2


def create_tables(db_name, params):
    conn = psycopg2.connect(dbname=db_name, **params)

    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute(f'CREATE TABLE employers ('
                    f'employer_id integer PRIMARY KEY,'
                    f'employer_name varchar(50),'
                    f'alternate_url varchar(100) ,'
                    f'vacancies_url varchar(100),'
                    f'open_vacancies integer'
                    f')')
        cur.execute(f'CREATE TABLE vacancies ('
                    f'vacancy_id integer PRIMARY KEY,'
                    f'vacancy_name varchar(100),'
                    f'salary_from integer,'
                    f'salary_to integer,'
                    f'vacancy_url varchar(100),'
                    f'employer_id integer REFERENCES employers(employer_id),'
                    f'employer_name varchar(50),'
                    f'requirements text,'
                    f'responsibility text,'
                    f'experience varchar(20)'
                    f')')

    conn.close()


def fill_tables(db_name, params, employers_info):
    conn = psycopg2.connect(dbname=db_name, **params)

    conn.autocommit = True

    with conn.cursor() as cur:
        for employer in employers_info:
            cur.execute(f'INSERT INTO employers VALUES (%s, %s, %s, %s, %s)',
                        (employer.id,
                         employer.name,
                         employer.alternate_url,
                         employer.vacancies_url,
                         employer.open_vacancies)
                        )

            vacancies = []
            for vacancy in employer.vacancies:
                vacancies.append((vacancy.id,
                                  vacancy.name,
                                  vacancy.salary['from'] if vacancy.salary else None,
                                  vacancy.salary['to'] if vacancy.salary else None,
                                  vacancy.url,
                                  vacancy.employer_id,
                                  vacancy.employer,
                                  vacancy.requirements,
                                  vacancy.responsibility,
                                  vacancy.experience
                                  )
                                 )

            cur.executemany(f'INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', vacancies)

    conn.close()


class DBworker:
    """Класс для работы с базой данных"""

    def __init__(self, password, host='localhost', user='postgres', port=5432):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self._params = {'host': self.host, 'user': self.user, 'password': self.password, 'port': self.port}

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value: dict):
        """Обновляет словарь self.params"""
        self._params.update(value)

    def create_database(self, db_name: str) -> None:
        """
        Создаёт базу данных с указанным именем
        """
        conn = psycopg2.connect(dbname='postgres', **self.params)

        conn.autocommit = True
        # self.drop_database(db_name)

        with conn.cursor() as cur:
            cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
            cur.execute(f'CREATE DATABASE {db_name}')

        conn.close()

    def drop_database(self, db_name: str) -> None:
        """Удаляет базу данных"""
        conn = psycopg2.connect(dbname='postgres', **self.params)

        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f'DROP DATABASE IF EXISTS {db_name}')

        conn.close()
