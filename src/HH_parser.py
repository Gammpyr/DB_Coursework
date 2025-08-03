import requests

from src.hh_models import Employer, Vacancy


def get_employers_info(data: list) -> list:
    """
    Принимает словарь с работодателями [{Название:ID}] и возвращает информацию о них
    """
    result = []

    for key, value in data[0].items():
        response = requests.get(f'https://api.hh.ru/employers/{value}')
        response.raise_for_status()
        response = response.json()
        result.append(
            Employer(response['id'],
                     response['name'],
                     response['alternate_url'],
                     response['vacancies_url'],
                     response['open_vacancies'])
        )

    get_vacancies(result)

    return result


def get_vacancies(emps_info: list[Employer]):
    """
    Принимает список словарей объектами Employer и присваивает каждому объекту список его вакансий
    """
    for emp in emps_info:
        params = {'per_page': 100, 'page': 0}

        print(f'Получаем вакансии от: {emp.name}')
        while True:
            response = requests.get(f'{emp.vacancies_url}', params)
            response.raise_for_status()
            response = response.json()

            items = []
            for item in response['items']:
                items.append(
                    Vacancy(
                        item["id"],
                        item["name"],
                        item["salary"],
                        item["alternate_url"],
                        item["employer"]["id"],
                        item["employer"]["name"],
                        item["snippet"]['requirement'],
                        item["snippet"]['responsibility'],
                        item["experience"]["name"]
                    )
                )

            emp.vacancies.extend(items)

            if params['page'] == response['pages'] - 1:
                break
            else:
                params['page'] += 1
