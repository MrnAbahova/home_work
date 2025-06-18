def get_mask_card_number(card_number: str) -> str:
    """Функция скрывает некоторые символы номера карты"""
    mask_card_number = card_number[0:4] + " " + card_number[5:7] + "** ****" + " " + card_number[-4:]
    return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция скрывает номер счета и выводит последние цифры"""
    mask_account = "**" + account[-4:]
    return mask_account

# test
