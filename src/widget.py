from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """ Функция обрабатывает информацию как о картах, так и о счетах"""
    parts = info.split()
    type_info = " ".join(parts[:-1])
    number = parts[-1]
    if "счет" in info.lower():
        mask_number = get_mask_account(number)
    else:
        mask_number = get_mask_card_number(number)
    return f"{type_info} {mask_number}"


def get_date(data: str) -> str:
    """ Функция, которая принимает на вход строку и возвращает строку с датой  """
    return f"'{data[8:10]}.{data[5:7]}.{data[0:4]}'"
