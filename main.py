from config import config
from src.database import DBworker, create_tables, fill_tables
from src.dbmanager import DBManager
from src.file_workers import read_file
from src.HH_parser import get_employers_info


def main() -> None:
    data = read_file("employers")  # Читаем файл с ID работодателей
    employers_info = get_employers_info(data)  # Получаем информацию о работодателях указанных в файле
    # employers_info = get_employers_info([{"HobbyWorld": 962612}])  # для теста

    db_name = "hh_employer"
    params = config()

    db = DBworker(**params)
    db.create_database(db_name)  # создаём базу данных
    create_tables(db_name, params)  # создаём таблицы
    fill_tables(db_name, params, employers_info)  # заполняем таблицы данными

    hh_employer = DBManager(db_name, **params)  # Создаём класс для работы с базой данных
    companies_and_vacancies_count = hh_employer.get_companies_and_vacancies_count()
    all_vacancies = hh_employer.get_all_vacancies()
    avg_salary = hh_employer.get_avg_salary()
    vacancies_with_higher_salary = hh_employer.get_vacancies_with_higher_salary()
    vacancies_with_keyword = hh_employer.get_vacancies_with_keyword("Python")


if __name__ == "__main__":
    main()
