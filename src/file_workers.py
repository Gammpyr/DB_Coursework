import json
from pathlib import Path


def read_file(filename: str = 'employers') -> list:
    """
    Читает файл employers.json (по умолчанию) и возвращает id работодателей из него в виде списка
    """
    filepath = Path('../data/') / Path(f'{filename}.json')
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file).values()

    return list(data)


def save_to_file(data, filename='employers_info'):
    filepath = Path('../data/') / Path(f'{filename}.json')
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
