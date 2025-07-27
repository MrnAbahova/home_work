def get_mask_card_number(card_number: str) -> str:
    """Функция скрывает некоторые символы номера карты"""

    mask_card_number = card_number[0:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]
    if '-' in card_number:
        divide_by_dash = card_number.split('-')
        remove_the_dash = ''.join(divide_by_dash)
        mask_card_number = remove_the_dash[0:4] + " " + remove_the_dash[4:6] + "** ****" + " " + remove_the_dash[-4:]
        if '' in card_number:
            raise Exception('Введите номер карты!')
        return mask_card_number
    return mask_card_number


def get_mask_account(mask_account: str) -> str:
    """Функция скрывает номер счета и выводит последние цифры"""
    mask_account = "**" + mask_account[-4:]
    return mask_account
