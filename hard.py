# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil
print('sys.argv = ', sys.argv)

def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        print('Успешно перешли в папку - ', dir_path)
    except Exception:
        print('Такой папки не существует')

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - копирование файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def current_dir():
        print('Текущая директория -',os.getcwd())

def remove_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        if input('Введите Y для подтверждения удаления ')=='Y':
            file_path = os.path.join(os.getcwd(), file_name)
            os.remove(file_path)
            print('Файл успешно удален')
        else:
            print('Отмена удаления')
    except Exception:
        print('Такого файла нет')

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_path))
    except OSError:
        print('директория {} уже существует'.format(dir_path))

def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        shutil.copyfile(file_path, (file_path.split('.')[0]) + '_copy.' + (file_path.split('.')[1]))
        print('Файл %s успешно скопирован' % file_path)
    except Exception:
        print('Такого файла нет')

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "ls": current_dir,
    "cd": change_dir
}
try:
   file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")