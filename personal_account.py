"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os
import json


def refill(account):
    val = float(input('Введите сумму пополнения: '))
    account += val
    return account


def purchase(account, history):
    val = float(input('Введите сумму покуаки: '))
    if val > account:
        print('Не достаточно денег на счету.')
    else:
        name = input('Название покупки: ')
        account -= val
        history.append((name, val))
    return account, history


def print_history(history):
    for k, v in history:
        print(f'{k}: {v}')


def load_or_create_account_info(file_name='account_info.json'):
    account_info = {'account': 0, 'history': []}
    if os.path.exists(file_name):
        with open(file_name) as f:
            loaded_info = json.load(f)
        account_info.update(loaded_info)
    return account_info


def save_account_info(account_info, file_name='account_info.json'):
    with open(file_name, 'w') as f:
        json.dump(account_info, f)


def operate_account(account_info):
    account = account_info['account']
    history = account_info['history']

    while True:
        print(f'Личный счет {account}')
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account = refill(account)
        elif choice == '2':
            account, history = purchase(account, history)
        elif choice == '3':
            print_history(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

    account_info['account'] = account
    account_info['history'] = history
    return account_info


if __name__ == '__main__':
    file_name = 'account_info.json'
    account_info = load_or_create_account_info(file_name)
    account_info = operate_account(account_info)
    save_account_info(account_info, file_name)
