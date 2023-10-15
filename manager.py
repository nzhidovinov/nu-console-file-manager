import os
import sys
import shutil
from victory import victory
from personal_account import operate_account, load_or_create_account_info, save_account_info


def get_menu_item(menu: dict, title=None) -> int:
    menu_items = sorted(menu, reverse=True)

    # print menu
    print(title)
    for i, item in enumerate(menu_items, start=1):
        print(f'{i:2}. {item}.')

    # get menu index
    while True:
        # last part of cwd
        cwd = os.path.split(os.getcwd())[-1]
        choice = int(input(f'({cwd}) Выберите пункт меню: '))
        if 1 <= choice <= len(menu_items):
            return menu_items[choice-1]
        else:
            print(f'Неверный пункт меню.')


def process(menu: dict):
    while True:
        # get menu item
        menu_item = get_menu_item(menu, title='Консольный файловый менеджер')
        # process program state
        exit_proc = menu[menu_item]()
        # exit processing
        if exit_proc:
            break


############################################################
# Commands
############################################################
def exit_command():
    return True


def cwd_command():
    new_work_dir = input('Ввыдите новую рабочую директорию: ')
    os.chdir(new_work_dir)


def print_creator_command():
    print('Жидовинов Никита.')


def make_dir_command():
    dir_name = input('Ввыдите имя новой папки: ')
    os.mkdir(dir_name)


def del_file_or_dir_command():
    dir_name = input('Ввыдите имя файла/папки: ')
    if os.path.isdir(dir_name):
        os.rmdir(dir_name)
    if os.path.isfile(dir_name):
        os.remove(dir_name)


def list_dir_command():
    print(os.listdir())


def save_list_dir_command():
    filename = 'listdir.txt'
    dirs = list_only_dirs()
    files = list_only_files()
    with open(filename, 'w') as f:
        for file_name in files:
            f.write(file_name + '\n')
        for dir_name in dirs:
            f.write(dir_name + '\n')


def list_only_dirs():
    return [dir_name for dir_name in os.listdir()
            if os.path.isdir(dir_name)]


def list_only_dirs_command():
    print(list_only_dirs())


def list_only_files():
    return [dir_name for dir_name in os.listdir()
            if os.path.isfile(dir_name)]


def list_only_files_command():
    print(list_only_files())


def sys_info_command():
    print(f'{sys.platform} {os.name}')


def victory_command():
    victory()


def operate_account_command():
    file_name = 'account_info.json'
    account_info = load_or_create_account_info(file_name)
    account_info = operate_account(account_info)
    save_account_info(account_info, file_name)


def copy_file_or_dir_command():
    src = input('Введите путь к файлу/папке: ')
    dst = input('Введите путь к папке назначения: ')
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    if os.path.isfile(src):
        shutil.copy(src, dst)


if __name__ == '__main__':
    menu = {
        'Создать папку': make_dir_command,
        'Удалить (файл/папку)': del_file_or_dir_command,
        'Копировать (файл/папку)': copy_file_or_dir_command,
        'Просмотр содержимого рабочей директории': list_dir_command,
        'Сохранение содержимого рабочей директории': save_list_dir_command,
        'Посмотреть только папки': list_only_dirs_command,
        'Посмотреть только файлы': list_only_files_command,
        'Просмотр информации об операционной системе': sys_info_command,
        'Создатель программы': print_creator_command,
        'Играть в викторину': victory_command,
        'Мой банковский счет': operate_account_command,
        'Смена рабочей директории': cwd_command,
        'Bыход': exit_command
    }

    process(menu)
