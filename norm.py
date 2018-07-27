_author_= 'Швец Александр Николаевич'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
def zadacha1():
    a = [2, -5, 8, 9, -25, 25, 4, 00000000, 9, 0]
    b=[]
    print('Исходный список ',a)
    import math
    for i in a:
     if (i > 0) and (math.sqrt(i)-int(math.sqrt(i))==0):        #Делаем проверку, что число не отрицательное
      if math.sqrt(i) in b:                                    #а затем что его корень не имеет дробной части
        continue
      else:
        b.append(int(math.sqrt(i)))
     else:
        continue
    print('Итоговый список ',b)



# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
def zadacha2():
    a = input('Введите дату в формате '"'dd.mm.yyyy'"' ').split('.')       #принимаем, что дата по умолчанию вводится верно
                                                                         #проверку на правильность ввода даты сделали в hard
    c = {"01":"Первое", "02":"Второе", "03":"Третье", "04":"Четвёртое", "05":"Пятое", "06":"Шестое", "07":"Седьмое",
     "08":"Восьмое", "09":"Девятое", "10":"Десятое", "11":"Одинадцатое", "12":"Двенадцатое", "13":"Тринадцатое",
     "14":"Четырнадцатое", "15":"Пятнадцатое", "16":"Шестнадцатое", "17":"Семнадцатое", "18":"Восемнадцатое",
     "19":"Девятнадцатое", "20":"Двадцатое", "21":"Двадцать первое", "22":"Двадцать второе", "23":"Двадцать третье",
     "24":"Двадцать четвёртое", "25":"Двадцать пятое", "26":"Двадцать шестое", "27":"Двадцать седьмое",
     "28":"Двадцать восьмое", "29":"Двадцать девятое", "30":"Тридцатое", "31":"Тридцать первое"}
    d = {"01":"Января", "02":"Февраля", "03":"Марта", "04":"Апреля", "05":"Мая", "06":"Июня", "07":"Июля", "08":"Августа",
     "09":"Сентября", "10":"Октября", "11":"Ноября", "12":"Декабря"}
    print("{} {} {} года".format(c[a[0]], d[a[1]], a[2]))


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
def zadacha3():
  import random
  n = int(input('Введите число элементов \n'))
  b=[]
  a=0
  while a < n:
    b.append(random.randint(-100,100))
    a += 1
  print('Итоговый список ',b)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
def zadacha4():
  a = [2, 2, 2, 2, 2, 2, 2, 4, 5, 6, 2, 5 , 2, 1]
  b =[]
  c =[]
  d=[]
  print('Начальный список ',a)         #цикл добавляет неповторяющиеся элементы списка а в новый список b
  for i in a[:]:
    if i in b:
      continue
    else:
      b.append(i)
  for z in a[:]:                         #цикл берет по одному элементу и удаляет их списка
    a.remove(z)                          #если такой элемент есть в исходном списке либо в промежуточном,
    if z in a or z in d:                 #добавляем его в промежуточный - он точно повторяется
      d.append(z)                        #если нет ни в исходном списке, ни в промежуточном - элемент встречается
    else:                                #только 1 раз и мы его выводим
      c.append(z)
  print('Элементы списка a без повторов ',b)
  print('Элементы списка а, которые присутствуют только 1 раз ',c)

print(_author_)
print('---------------------------------------------------------------------')
print('Задача1')
zadacha1()
print('---------------------------------------------------------------------')
print('Задача2')
zadacha2()
print('---------------------------------------------------------------------')
print('Задача3')
zadacha3()
print('---------------------------------------------------------------------')
print('Задача4')
zadacha4()
print('---------------------------------------------------------------------')