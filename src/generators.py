from src.transaction_list import transactions

def filter_by_currency(transactions, target_currency ):
    for transaction in transactions:
        if transaction ["operationAmount"]["currency"]["code"] == target_currency:
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start , stop ):
    for i in range(start, stop+1):
        number = str(i).zfill(16)
        yield number[:4] + " " + number[4:8] + " " + number[8:12] + " " + number[12:16]



