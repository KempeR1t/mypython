# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
def fibonacci(n,m):
  if n > 0 and m > 0:
      a=[1,1]
      while len(a) <= m+1:
            a.append(a[-1]+a[-2])
      return a[n-1:m]
  else:
      print('Неверный ввод')

print(fibonacci(0,13))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

#def sort_to_max(origin_list):
#    pass
"""
обычная пузырьковая сортировка, которая меняет 2 элементами местами , если один больше другого, цикл завершается
когда при проходе всего списка не было ни одной замены
"""
def sort_to_max(origin_list):
  d=1
  while d!=0:
      d=0
      for x in range(len(origin_list)-1):
          if origin_list[x]>origin_list[x+1]:
              c = origin_list[x+1]
              origin_list[x+1] = origin_list[x]
              origin_list[x] = c
              d+=1
  return origin_list

print(sort_to_max([2, 10, -12, 4, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_own_filter(expr, data):
    itog_list= []                  #пустой список, для значений, которые удовлетворили условию
    for x in data:                 #перебор значений, которые мы подали
        if expr(x):                #если условие выполняется
            itog_list.append(x)    #заносим его в наш список
    return itog_list               #выводим список

v = [5, 2 , 3, 4 , 5, 6 , 7,  8 , 9 , -5 , -6 , 8]

print(my_own_filter(lambda y: y % 2 ==0 , v))          #вывод четных чисел
print(my_own_filter(lambda y: y < 0, v))               #вывод отрицательных чисел
print(my_own_filter(lambda y: y > 0 and y % 2 != 0, v))   #вывод нечетных положительных чисел


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
'''
Если противоположеные прямые ПОПАРНО параллельны  > параллелограмм.
'''
def proverka_na_parallelnost(x1,x2,y1,y2):
    return x1 * y2 - x2 * y1 == 0

def parallelogram(x1,y1,x2,y2,x3,y3,x4,y4):
    return (proverka_na_parallelnost(x2 - x1, y2 - y1, x3 - x4, y3 - y4)
            and proverka_na_parallelnost(x3 - x2, y2 - y3, x4 - x1, y4 - y1)) \
           or (proverka_na_parallelnost(x3 - x1, y3 - y1, x2 - x4, y2 - y4)
               and proverka_na_parallelnost(x2 - x3, y2 - y3, x1 - x4, y1 - y4))

print(parallelogram(0, 0, 1, 1, 2, 1, 1, 0))
print(parallelogram(3, 4, 4, 4, 3, 3, 4, 3))