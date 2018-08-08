# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
#создание

import os
import time
def create_dir(dir_name):
    os.mkdir(dir_name)

def delete_dir(dir_name):
    os.rmdir(dir_name)

#создание
for x in range (9):
    create_dir('dir_'+str(x))

print('Через 5 секунд папки будут удалены')
time.sleep(1)
print('Через 4 секунды папки будут удалены')
time.sleep(1)
print('Через 3 секунды папки будут удалены')
time.sleep(1)
print('Через 2 секунды папки будут удалены')
time.sleep(1)
print('Через 1 секунду папки будут удалены')
time.sleep(1)
print('Папки удалены')
#удаление
for x in range (9):
    delete_dir('dir_' + str(x))



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('Список папок в текущей директории %s' % os.getcwd())

def current_dir_list(dir_name):
    d=[]
    for o in os.listdir(dir_name):
       if os.path.isdir(o):
           d.append(o)
    return d

for x in current_dir_list(os.getcwd()):
    print(x)



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import shutil

def copy_file(source, dest):
    shutil.copyfile(source, dest)

copy_file(sys.argv[0], sys.argv[0][:-3] + '_copy.py')  # делаем [:-3] чтобы не было проблем с расширением
