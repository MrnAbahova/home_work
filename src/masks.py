def get_mask_card_number(card_number: str) -> str:
    """ Функция скрывает некоторые цифры номера карты """
    if len(card_number) < 16 or len(card_number) > 16:
        if '-' in card_number:
            divide_by_dash = card_number.split('-')
            remove_the_dash = ''.join(divide_by_dash)
            return remove_the_dash[0:4] + " " + remove_the_dash[4:6] + "** ****" + " " + remove_the_dash[-4:]
        return "Введите корректный номер карты!"
    return card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]


def get_mask_account(mask_account: str) -> str:
    """Функция скрывает номер счета и выводит последние цифры"""
    if '-' in mask_account:
        divide_by_dash = mask_account.split('-')
        remove_the_dash = ''.join(divide_by_dash)
    mask_account = "**" + mask_account[-4:]
    return mask_account
