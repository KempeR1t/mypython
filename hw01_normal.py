__author__ = 'Швец Александр Николаевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

a = int(input('Введите любое число '))
max=0
while a !=0:
  if a%10 > max:
    max = a%10
  a = (a-a%10)//10
print(max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
a = a + b
b = a - b
a = a - b
print(a,b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
a=int(input('Введите первый коэффициент '))
b=int(input('Введите второй коэффициент '))
c=int(input('Введите третий коэффициент '))
d = b**2 - 4 * a * c
import math
d = math.sqrt(d)
x1=(b*-1+d)/(2*a)
x2=(b*-1-d)/(2*a)
print(x1,x2)