# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
'''
Алгоритм работы программы: берём число и делим его на 2 части : целую и дробную, далее все операции уже идут с дробной
от дробной части отрезаем последние символы, которые округлить: например было число 2.55555, нужно округлить
до 2 символов после запятой, целая часть - 2, дробная - 55555, лишняя дробной части - 555 , затем нам необходимо
определить в какую сторону будет округление , мы создаем число , которое на 1 порядок больше лишней дробной части,
то есть в данной ситуации 555 - лишнее, создаваемое число 1000. Из созданного числа вычитаем лишнюю дробную часть
и пониманием в какую сторону нужно производить округление + доп проверки если в результате округления изменится так же
и целая часть
'''
def my_round(number, ndigits):
 b=str(number).split('.')
 d=b[1]                                #вся дробная часть
 try:
     c=int((b[1])[ndigits:])            #лишняя часть дробной части
 except Exception:
     return number
 k = (len(str(d))-ndigits if len(str(d))-ndigits > 0 else 1)
 z='1'+'0'*k    #число по которому мы смотрим в какую сторону будет округление
 if (int(z)-c) >= c:
     itog = b[0]+ '.' + (b[1])[:ndigits]
 else:
     if len(str(int((b[1])[:ndigits]) + 1)) == ndigits:           #доп проверка на случай увеличения целой части числа
        itog = float(b[0] + '.' + str(int((b[1])[:ndigits])+1))
     else:
         itog = float(str(int(b[0])+1) + '.0')
 return itog

print(my_round(5.09999999999999999999, 2) , round(5.09999999999999999999, 2))
print(my_round(2.1999967, 5), round(2.1999967, 5))
print(my_round(2.9999967, 5), round(2.9999967, 5))



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

"""
Программа не работает со значениями билетов, у которых первая цифра - 0
т.к. инт() ее просто сокращает и число не проходит проверку на длина = 6
"""
def lucky_ticket(ticket_number):
    if len(str(ticket_number))==6:
      ch1 = int(str(ticket_number)[0]) + int(str(ticket_number)[1]) + int(str(ticket_number)[2])
      ch2=  int(str(ticket_number)[3]) + int(str(ticket_number)[4]) + int(str(ticket_number)[5])
      return (ch1==ch2)
    else:
      return False
print(lucky_ticket(000000))
print(lucky_ticket(123321))
print(lucky_ticket(456096))
print(lucky_ticket(117018))