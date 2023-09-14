from pprint import pprint
from typing import Iterator

goods = [
    {
        'name': 'Iphone 14',
        'brand': 'Apple',
        'price': 1200,
    },
    {
        'name': 'Samsung Galaxy A53',
        'brand': 'Samsung',
        'price': 500,
    },
    {
        'name': 'REALME C25s',
        'brand': 'REALME',
        'price': 400,
    }
]

if __name__ == "__main__":


    names_list = ['Данил', 'Никита', 'Настя', 'Катя']
    surnames_list = ['Петров', 'Иванов', 'Даниловна', 'Никитовна']
    full_names_list = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames_list))
    print(full_names_list)
    patronymic_list = ['Данилович', 'Никитич', 'Ивановна']
    for name, surname, patronymic in zip(surnames_list, names_list,  patronymic_list):
        print(name, surname, patronymic)
    full_name = [f'{name} {surname} {patronymic}' for name, surname, patronymic in zip(surnames_list, names_list,  patronymic_list)]
    print(full_name)