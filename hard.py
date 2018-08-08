_author_= 'Швец Александр Николаевич'
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

'''
Как сейчас работает программа. Внимательно прочитайте раздел help , я туда добавил описание изменений, которые я внёс.
Вкратце: если не использовать классы и промежуточные файлы, то результат операции chdir() никак не сохранялся, т.к.
каждый раз мы заново обращаемся к скрипту и он забывает о том, что мы меняли активную папку. Потому теперь если вы
делаете cd , то путь пишется в файл options.txt и далее для всех остальных операций путь всегда подгружается оттуда,
если ввести команду cd без аргумента, то файл options.txt удалится и программа будет работать
с папкой по умолчанию - той, откуда запущен был скрипт.
'''

import os
import sys
import shutil

print('sys.argv = ', sys.argv)
path = os.path.join(os.getcwd(), 'options.txt')
if os.path.isfile(path):
    with open(path, 'r', encoding='UTF-8') as f:
        active_papka = f.read()
else:
    active_papka = os.getcwd()
print('Ваша текущая активная папка - ', active_papka, '\n')

def change_dir():
    path = os.path.join(os.getcwd(), 'options.txt')
    if not dir_name:
        print('Активная папка сброшена на значение по умолчанию(папка запуска скрипта) - %s' % os.getcwd())
        os.remove(path)
        return
    dir_path = os.path.join(active_papka, dir_name)
    if os.path.isdir(dir_path):
        with open(path, 'w', encoding='UTF-8') as f:
            f.write(dir_path)
        print('Успешно перешли в папку - ', dir_path)
    else:
        print('Такой папки нет')

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную, НО если ввести команду cd без аргумента"
          "то активная папка сбросится на папку по умолчанию - ту из которой запущен скрипт")
    print("ls - отображение полного пути текущей директории")
    print('ВАЖНО! \n При самом первом запуске скрипта папкой по умолчанию считается папка, из которой запущен скрипт, '
          'а затем любые переходы в другую папку сохраняются в файле options.txt')

def current_dir():
        print('Полный путь текущей директории -',active_papka)

def remove_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        file_path = os.path.join(active_papka, file_name)
        print('Вы собираетесь удалить файл %s' % file_path)
        if input('Введите Y для подтверждения удаления ')=='Y':
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
    dir_path = os.path.join(active_papka, dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_path))
    except OSError:
        print('директория {} уже существует'.format(dir_path))

def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(active_papka, file_name)
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
