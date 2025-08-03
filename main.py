from pprint import pprint

import psycopg2

from config import config
from src.HH_parser import get_vacancies, get_employers_info
from src.file_workers import read_file, save_to_file

data = read_file('employers')  # Читаем файл с ID работодателей

# employers_info = get_employers_info([{"Компания 05.ру": 1150295}])
employers_info = get_employers_info(data)  # Получаем информацию о работодателях

get_vacancies(employers_info)  # Получаем список вакансий



# def main():
#     script_file = 'fill_db.sql'
#     json_file = 'suppliers.json'
#     db_name = 'HH_employer'
#
#     params = config()
#     conn = psycopg2.connect(**params)
#
#     create_database(params, db_name)
#     print(f"БД {db_name} успешно создана")
#
#     params.update({'dbname': db_name})
#     try:
#         with psycopg2.connect(**params) as conn:
#             with conn.cursor() as cur:
#                 execute_sql_script(cur, script_file)
#                 print(f"БД {db_name} успешно заполнена")
#
#                 create_suppliers_table(cur)
#                 print("Таблица suppliers успешно создана")
#
#                 suppliers = get_suppliers_data(json_file)
#                 insert_suppliers_data(cur, suppliers)
#                 print("Данные в suppliers успешно добавлены")
#
#                 add_foreign_keys(cur, json_file)
#                 print(f"FOREIGN KEY успешно добавлены")
#
#     except(Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
