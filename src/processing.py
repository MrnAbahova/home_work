def filter_by_state(DICTIONARIES, state: list) -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    new_dictionaries = []
    for slovar in DICTIONARIES:
        for value in slovar.values():
            if value == "EXECUTED":
                new_dictionaries.append(slovar)
    return new_dictionaries


def sort_by_date(DICTIONARIES_DATA: list) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_dictionaries_data = sorted(DICTIONARIES_DATA, key=lambda x: x["date"], reverse=True)
    return sorted_dictionaries_data
