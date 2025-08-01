import requests


def get_employers_info(data: list) -> list:
    """
    Принимает словарь с работодателями и возвращает информацию о них
    """
    result = []

    for key, value in data[0].items():
        response = requests.get(f'https://api.hh.ru/employers/{value}')
        response.raise_for_status()
        response = response.json()
        result.append({
            'id': response['id'],
            'name': response['name'],
            'alternate_url': response['alternate_url'],
            'vacancies_url': response['vacancies_url'],
            'open_vacancies': response['open_vacancies'],
        })

    return result


def get_vacancies(emps_info: list):
    """Принимает список словарей с информацией о работодателях и возвращает список вакансий"""
    result = []

    for emp in emps_info:
        params = {'per_page': 100, 'page': 0}
        emp["vacancies"] = []
        emp_vacancy_url = emp["vacancies_url"]
        print(f'Получаем вакансии от: {emp['name']}')
        while True:
            response = requests.get(f'{emp_vacancy_url}', params)
            response.raise_for_status()
            response = response.json()

            items = []
            for item in response['items']:
                items.append({
                    "id": item["id"],
                    "name": item["name"],
                    "salary": item["salary"],
                    "url": item["alternate_url"],
                    "employer": item["employer"]["name"],
                    "snippet": item["snippet"],
                    "experience": item["experience"]["name"]}
                )

            emp["vacancies"].extend(items)

            if params['page'] == response['pages'] - 1:
                result.append({emp['name']: emp})
                break
            else:
                params['page'] += 1

    return result
