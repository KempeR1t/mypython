# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
"""
Алгоритм работы моей программы:
Сразу же нафиг избавляемся от вычитания отрицательного числа и заменяем эту ситуацию на сложение.
Далее берём нашу строку с выражением и отрезаем по одному элементу, если это дробь или число то суммируем. Самое
главное это контролировать знак действий. В конце полученную  дробь мы сокращаем при необходимости
Если снять комментарии с принтов в теле программы, то можно наглядно посмотреть как она работает.
"""
from fractions import Fraction
try:
    s = input()
    #s = '1 + 0 1/5'
    print('Исходное выражение =', s)
    s = s.replace('- -', '+ ')          #самым простым способом обыграть ситуацию когда идет вычитание отрицательного
    d = len(s.split(' '))               #числа это сразу заменить его на '+'
    g=0
    znak=1
    for _ in range(d):                   #цикл исполняющийся столько раз, сколько у нас элементов
        s = s.partition(' ')             #делим строку на части
        '''print(s)'''
        if s[0] != '+' and s[0] != '-':    #если наш первый элемент это не знак действия , а число или дробь
            '''print('Полученный элемент {} записываем в нашу конечную дробь с учетом знака {}'.format(Fraction(s[0]),
                                                    '+' if znak==1 else '-'))'''
            g = Fraction(g)+Fraction(s[0])*znak                 #то мы его плюсуем
        if (not s[0].isdigit() and s[0][1:].isdigit() and s[2][1] != ' ') or (s[0]== '-'):
            znak = -1                 #Данное условие обыгрывает ситуацию, когда перед целой частью стоит знак минус
        elif s[0] == '+':             #чтобы дробная тоже имела такой же знак. по сути это была единственная
            znak = 1                  #сложность, а именно корректно взять знак дробной части, имеющей целую
        s = s[2]
    #при необходимости выделим целую часть
    if (g != 0) and (not g==int(g)):
        itog_drob = str(g).split('/')
        if abs(int(itog_drob[0])) >= int(itog_drob[1]):  #если числитель по модулю больше знаменателя, делим нацело
            znak = (1 if int(itog_drob[0]) > 0 else -1)  #чтобы получить целую часть, а затем сокращаем дробь, сохранив знак
            celoe = abs(int(itog_drob[0])) // int(itog_drob[1]) * znak
            itog_drob[0] = abs(int(itog_drob[0])) % abs(int(itog_drob[1]))
            print('Итоговая дробь =',celoe, Fraction(itog_drob[0], int(itog_drob[1])))
            exit()
    print('Итоговая дробь =', g)
except Exception:
    print('Итоговая дробь =', g)



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
'''
Алгоритм работы программы состоит в том, чтобы создать 2 словаря, где ключами будут ФИО, а данными все остальное -
реальная зп, отработанные часы, и количество часов, которое нужно было реально отработать.
'''
import os
z = 'F:/Загрузки/'              #сюда пишем адрес папки, где лежат файлы
try:

    def analiz_faila(papka, file, poziciya):
        path = os.path.join(papka, file)
        with open(path, 'r', encoding='UTF-8') as f:
            yy=dict()
            for line in f:
                line = line.split(' ')
                line = list(filter(len, line))
                line[-1] = line[-1].replace('\n', '')
                if line[poziciya].isdigit() or line[poziciya].find('.') != -1:
                    yy[line[0] + ' ' + line[1]] = float(line[poziciya])
            return yy

    otrabotano_chasov = analiz_faila(z, 'hours_of',2)
    print(otrabotano_chasov)
    polojeno_chasov = analiz_faila(z, 'workers', 4)
    print(polojeno_chasov)
    zarplata = analiz_faila(z, 'workers',2)
    print(zarplata)

    realnaya_zp=dict()
    for key, value in otrabotano_chasov.items():
        if value <= polojeno_chasov[key]:
            realnaya_zp[key] = round(value * zarplata[key] / polojeno_chasov[key], 2)
        else:
            realnaya_zp[key] = round(2 * int(value - polojeno_chasov[key]) * zarplata[key] / polojeno_chasov[key] + zarplata[key], 2)

    path = os.path.join(z, 'itog.txt')
    with open(path, 'w', encoding='UTF-8') as f:
        f.write('Имя Фамилия Фактическая_зарплата\n')
        for key, value in realnaya_zp.items():
            f.write('{} {}\n'.format(key, str(value)))

    print('Результаты выгружены по адресу ' ,z ,'itog.txt', sep= '')
except FileNotFoundError:
    print('Ошибка! Не найдены файлы , либо неверно указан путь к ним')



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
import os
path = os.path.join('F:/', 'Загрузки/', 'fruits.txt')
f = open(path, 'r', encoding='UTF-8')
# Считываем всю информацию из файла
v=f.read()
f.close()
v = v.split('\n')
dl=0
print(v)
exit()
while dl < len(v):               #удаляем пустые элементы из списка
    if v[dl] == '':
        del v[dl]
    else:
        dl += 1
bukva = v[0][0]
path=os.path.join('F:/Загрузки/', str('fruits_'+bukva+'.txt'))
for x in range(len(v)):
    if v[x][0]==bukva:
        f = open(path, 'a', encoding='UTF-8')
        f.write(v[x]+'\n')
        f.close
    else:
        bukva=str(v[x][0])
        path=os.path.join('F:/Загрузки/', str('fruits_'+bukva+'.txt'))
        f = open(path, 'a', encoding='UTF-8')
        f.write(v[x] + '\n')
        f.close
    x+=1