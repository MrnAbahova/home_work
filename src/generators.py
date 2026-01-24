from src.transaction_list import transactions

def filter_by_currency(transactions, target_currency ):
    for transaction in transactions:
        if transaction ["operationAmount"]["currency"]["code"] == target_currency:
            yield transaction






