# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
def create_dir(dir_name):
    os.mkdir(dir_name)

def delete_dir(dir_name):
    os.rmdir(dir_name)

def current_dir_list(dir_name):
    d=[]
    for o in os.listdir(dir_name):
       if os.path.isdir(o):
           d.append(o)
    return d

def copy_file(source, dest):
    shutil.copyfile(source, dest)

def change_dir(dir_name):
    os.chdir(dir_name)