from pprint import pprint

import psycopg2

from config import config
from src.HH_parser import get_vacancies, get_employers_info
from src.database import DBworker, create_tables, fill_tables
from src.dbmanager import DBManager

from src.file_workers import read_file




def main():
    data = read_file('employers')  # Читаем файл с ID работодателей
    employers_info = get_employers_info(data)  # Получаем информацию о работодателях указанных в файле
    # employers_info = get_employers_info([{"HobbyWorld": 962612}])  # Получаем информацию о работодателях указанных в файле

    db_name = 'hh_employer'
    params = config()

    db = DBworker(**params)
    db.create_database(db_name) # создаём базу данных
    create_tables(db_name, params) # создаём таблицы
    fill_tables(db_name, params, employers_info) # заполняем таблицы данными

    # hh_employer = DBManager(db_name, **params)



    # try:
    #     with psycopg2.connect(**params) as conn:
    #         with conn.cursor() as cur:

    # except(Exception, psycopg2.DatabaseError) as error:
    #     print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()


if __name__=='__main__':
    main()