from pprint import pprint

import requests

from src.file_workers import read_file, save_to_file


def get_employee_info():
    result = []
    data = read_file()

    for emp in data:
        response = requests.get(f'https://api.hh.ru/employers/{emp}')
        response.raise_for_status()
        result.append(response.json())

    return result

def get_vacancies(emp_info):
    emp_info["vacancies_url"]  # url для поиска вакансий

if __name__ == '__main__':
    save_to_file(get_employee_info())
