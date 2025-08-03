import json
from pathlib import Path


def read_file(filename: str = "employers") -> list:
    """
    Читает JSON файл
    """
    filepath = Path("./data/") / Path(f"{filename}.json")

    result = []
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        for e in data:
            result.append(e)

    return result


def save_to_file(data: dict, filename: str = "employers_info") -> None:
    """Сохраняет информацию в JSON файл"""
    filepath = Path("./data/") / Path(f"{filename}.json")
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
