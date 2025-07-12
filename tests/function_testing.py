from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number('11111111111111111111') == "1111 11** **** 1111"


def test_get_mask_account():
    assert get_mask_account('111111111111') == "**1111"

