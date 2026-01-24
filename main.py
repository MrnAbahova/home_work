from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date,mask_account_card
from src.generators import filter_by_currency
from src.transaction_list import transactions

print(get_mask_card_number("7000792289606361"))
print(get_mask_account("7000792289606361"))

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card('Счет 73654108430135874305'))

print(get_date("2024-03-11T02:26:18.671407"))

trans = input('Введите код валюты - ')
usd_transactions = filter_by_currency(transactions,trans.upper())

for cod in usd_transactions:
    print(cod)

