_author_= 'Швец Александр Николаевич'
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
a = equation.split(" ")   #записываем все элементы заданного уравнения в список
b=a[2].split('x')         #выделяем численную часть

print('Исходное уравнение:', equation)
print('x:',x)
if a[3]=='+':
 print('y:',x*int(b[0])+float(a[4]))
else: print('y:',x*int(b[0])-float(a[4]))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

date=input('Введите дату в формате '"'dd.mm.yyyy'"' ').split('.')
if len(date[0])==2 and len(date[1])==2 and len(date[2])==4 and 1<=int(date[2])<=9999 and 1<=int(date[1])<=12:
    pass
else:
    print('Дата введена неверно')
    exit()
if (date[1]=='04' or date[1]=='06' or date[1]=='09' or date[1]=='11' or date[1]=='02') and 1<=int(date[0])<=30:
    pass
elif (date[1]=='01' or date[1]=='03' or date[1]=='05' or date[1]=='07' or date[1]=='08' or date[1]=='10' or date[1]=='12') and 1<=int(date[0])<=31:
    pass
else:
    print('Дата была введена неверно (проверьте ввод дня)')
    exit()
print('Дата введена корректно!')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
n=int(input('Введите номер комнаты '))
kolvo_etajei=0
kolvo_komnat=0
a=1
f=1
d=1
z=0
kolvo_komnat2=0
while a <= n:                                                       #если раскомментировать принты, то нарисует башню
    while z<d and a<=n:                                             #но сверху вниз, на работу программы не влияет
        while kolvo_komnat<d and a<=n:
            #print(a,end=' ')
            a+=1
            kolvo_komnat+=1
            if a>n:
                kolvo_komnat2 = kolvo_komnat
            else: continue
        z+=1
        kolvo_komnat=0
        #print()
        kolvo_etajei+=1
    d+=1
    z=0
print('Этаж номер =',kolvo_etajei,'Комната номер =', kolvo_komnat2)