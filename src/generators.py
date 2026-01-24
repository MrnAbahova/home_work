from src.transaction_list import transactions

def filter_by_currency(transactions, target_currency ):
    for transaction in transactions:
        if transaction ["operationAmount"]["currency"]["code"] == target_currency:
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]





