from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("12345678901234567890", "1234 5678 **** **** 7890"),
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        ("1234-5678-9012-3456", "1234 56** **** 3456"),
        ("12345678901234567890", "Введите корректный номер карты!"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    """Тест корректности маскировки номера карты"""
    assert get_mask_card_number


@pytest.mark.parametrize(
    "mask_account, expected",
    [("12345678901234567890", "**7890"), ("1234567890", "**7890"), ("12345", "**2345"), ("1234567890", "**7890")],
)
def test_get_mask_account(mask_account, expected):
    """Тест корректности маскировки номера счета"""
    assert get_mask_account
