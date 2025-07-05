def filter_by_state(DICTIONARIES, state):
    new_dictionaries = []
    for slovar in DICTIONARIES:
        for value in slovar.values():
            if value == 'EXECUTED':
                new_dictionaries.append(slovar)
    return new_dictionaries

filter_by_state(DICTIONARIES, 'EXECUTED')

def sort_by_date(DICTIONARIES_DATA):
    sorted_dictionaries_data = sorted(DICTIONARIES_DATA, key=lambda x: x['date'], reverse=True)
    #print(sorted_dictionaries_data)
    return sorted_dictionaries_data

sort_by_date(DICTIONARIES_DATA)