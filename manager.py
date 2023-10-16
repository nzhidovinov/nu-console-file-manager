import os
import sys
import shutil
from victory import victory
from personal_account import operate_account, load_or_create_account_info, save_account_info

menu = {}


def no_fail(fn):
    def wrapper(input_fn, output_fn):
        res = None
        try:
            res = fn(input_fn, output_fn)
        except Exception as e:
            output_fn(f'Ошибка: {e}')
            return res
    return wrapper


def menu_item(name, input_fn=input, output_fn=print, catch_err=True):
    # register menu item
    def decorator(fn):
        global menu
        item_id = len(menu) + 1
        fn = no_fail(fn) if catch_err else fn
        menu[item_id] = dict(name=name, fn=fn, input_fn=input_fn, output_fn=output_fn)
        return fn

    return decorator


def get_menu_item(menu: dict, title=None) -> int:
    # print menu
    print(title)
    for i, item in sorted(menu.items()):
        print(f'{i:2}. {item["name"]}.')

    # get menu index
    while True:
        # last part of cwd
        cwd = os.path.split(os.getcwd())[-1]
        choice = int(input(f'({cwd}) Выберите пункт меню: '))
        if 1 <= choice <= len(menu):
            return choice
        else:
            print(f'Неверный пункт меню.')


def process(menu: dict):
    while True:
        # get menu item
        menu_item = get_menu_item(menu, title='Консольный файловый менеджер')
        # process program state
        item = menu[menu_item]
        fn = item['fn']
        input_fn = item['input_fn']
        output_fn = item['output_fn']
        exit_proc = fn(input_fn, output_fn)
        # exit processing
        if exit_proc:
            break


############################################################
# Functions
############################################################
def creator_info():
    return 'Жидовинов Никита'


def sys_info():
    return f'{sys.platform} {os.name}'


def lsd():
    return (d for d in os.listdir())


def list_only_dirs():
    return filter(lambda x: os.path.isdir(x), lsd())


def list_only_files():
    return filter(lambda x: os.path.isfile(x), lsd())


############################################################
# Commands
############################################################
@menu_item('Смена рабочей директории')
def cwd_command(input_fn, output_fn):
    new_work_dir = input_fn('Ввыдите новую рабочую директорию: ')
    os.chdir(new_work_dir)


@menu_item('Создать папку')
def make_dir_command(input_fn, output_fn):
    dir_name = input_fn('Ввыдите имя новой папки: ')
    os.mkdir(dir_name)


@menu_item('Удалить (файл/папку)')
def del_file_or_dir_command(input_fn, output_fn):
    dir_name = input_fn('Ввыдите имя файла/папки: ')
    if os.path.isdir(dir_name):
        os.rmdir(dir_name)
    if os.path.isfile(dir_name):
        os.remove(dir_name)


@menu_item('Просмотр содержимого рабочей директории')
def list_dir_command(input_fn, output_fn):
    for d in lsd():
        output_fn(d)


@menu_item('Сохранение содержимого рабочей директории')
def save_list_dir_command(input_fn, output_fn):
    filename = 'listdir.txt'
    with open(filename, 'w') as f:
        for file_name in list_only_dirs():
            f.write(file_name + '\n')
        for dir_name in list_only_files():
            f.write(dir_name + '\n')


@menu_item('Посмотреть только папки')
def list_only_dirs_command(input_fn, output_fn):
    for i in list_only_dirs():
        output_fn(i)


@menu_item('Посмотреть только файлы')
def list_only_files_command(input_fn, output_fn):
    for i in list_only_files():
        output_fn(i)


@menu_item('Копировать (файл/папку)')
def copy_file_or_dir_command(input_fn, output_fn):
    src = input_fn('Введите путь к файлу/папке: ')
    dst = input_fn('Введите путь к папке назначения: ')
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    if os.path.isfile(src):
        shutil.copy(src, dst)


@menu_item('Играть в викторину')
def victory_command(input_fn, output_fn):
    victory(input_fn, output_fn)


@menu_item('Мой банковский счет')
def operate_account_command(input_fn, output_fn):
    file_name = 'account_info.json'
    account_info = load_or_create_account_info(file_name)
    account_info = operate_account(account_info, input_fn, output_fn)
    save_account_info(account_info, file_name)


@menu_item('Создатель программы')
def print_creator_command(input_fn, output_fn):
    output_fn(creator_info())


@menu_item('Просмотр информации об операционной системе')
def sys_info_command(input_fn, output_fn):
    output_fn(sys_info())


@menu_item('Bыход')
def exit_command(input_fn, output_fn):
    return True


if __name__ == '__main__':
    process(menu)
