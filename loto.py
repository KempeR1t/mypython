_author_= 'Швец Александр Николаевич'
import random
vse_bochonki = [a for a in range(1, 91)]
stroka = []
stroka_igroka = []
stroka_igroka_print = []
stroka_compa_print = []
def delaem_bilet():          #функция отвечает за формирование билета для игроков
    global stroka            #обращаемся к глобальным переменным
    global vse_bochonki
    while len(stroka) < 27:  #в нашей карточке должно быть 27 элементов
        karta = random.sample(vse_bochonki, 5) #берём 5 рандомных чисел из общего пула(1-90)
        karta.sort()        #и сортируем по возрастанию
        vse_bochonki = list(set(vse_bochonki) - set(karta)) #из общего пула вычитаем взятые числа, чтобы не повторились
        for x in range(9):      #в каждой строке у нас 9 элементрв
            if random.randint(0,1)==1 and len(karta[:])<9-x or len(karta)==0: #начинаем формировать строку
                stroka.append('-')  #надо сформировать строку из 9 элементов, в которой будет 5 чисел и 4 пропуска
            else:  #в формирование включим рандом, делаем рандом от 0 до 1, если выпало 1, то ставим прочерк, если 0
                stroka.append(karta.pop(0)) #то число. Плюс дополнительная проверка на то, что у нас осталось достаточно
    vse_bochonki = [a for a in range(1, 91)] #мест в карточке для всех чисел(если впритык, то без рандом просто вставляем
    return stroka                                                                                          #число

def print_bileta(strochka):               #функция из полученной строки билета , в которой 27 элементов (15 чисед
    print('-------------------------')                                          #и 12 прочерков)
    for x in range(len(strochka)):        #делает красивый вывод билет в 3 строки по 9 элементов
        if x % 9 ==0 and x!=0:
            print()
        print(strochka[x],end = ' ')
    print()
    print('-------------------------')

def vivodim_bileti():                        #эта функция экономит нам место, потому что эти принты нужны нам были часто
    print('\033[91m' + 'Карточка игрока')
    print_bileta(stroka_igroka_print)
    print('\033[0m' + '\033[92m' + 'Карточка компа')
    print_bileta(stroka_compa_print)
    print('\033[0m')


delaem_bilet()                            #формируем билет игрока
stroka_igroka += stroka
stroka_igroka_print += stroka
stroka.clear()
delaem_bilet()                            #формируем билет компа
stroka_compa_print += stroka

while len(stroka) !=12 and len(stroka_igroka)!=12 :   #ну а дальше мы берём общий пул бочонков и каждый ход берём из него
    print('В корзине осталось %s бочонков' % len(vse_bochonki))  #один рандомный, и удаляем при необходимости
    noviy_bochonok = random.sample(vse_bochonki, 1)[0]          #из билета игроков
    print('осталось у компа -', len(stroka)-12, 'осталось у игрока - ', len(stroka_igroka)-12)
    vivodim_bileti()
    d=input('Зачеркнуть в карточке число {} ? \ny - зачеркиваем, n - берём следующий бочонок '
            .format( '\033[1m' + '\033[91m' + str(noviy_bochonok) + '\033[0m'))
    if d == 'y':
        if noviy_bochonok in stroka_igroka:     #долго думал как оформлять числа, которые были в билетах
            print('\nВЕРНО! Продолжаем...')     # и выпали на бочонках и игрок их вычеркнул, сначала хотел
            stroka_igroka.remove(noviy_bochonok) #выводить их зачеркнутыми или другим цветом
            stroka_igroka_print[stroka_igroka_print.index(noviy_bochonok)] = '-'   #но не получилось применить это
            vse_bochonki.remove(noviy_bochonok)                                #к элементу списка
        else:
            print('\nТы проиграл, такого числа не было в твоём билете!')    #потому я просто стал их в билете игрока
            break                                                        #заменять на '-', так удобнее для глаз
        if noviy_bochonok in stroka:
            stroka.remove(noviy_bochonok)
            stroka_compa_print[stroka_compa_print.index(noviy_bochonok)] = '-'
    elif d== 'n':
        if noviy_bochonok in stroka_igroka:
            print('\nТы проиграл, такое число было в твоём билете!')
            break
        else:
            vse_bochonki.remove(noviy_bochonok)
        if noviy_bochonok in stroka:
            stroka.remove(noviy_bochonok)
            stroka_compa_print[stroka_compa_print.index(noviy_bochonok)] = '-'
    else:
        print('Повторите ввод\n')

if len(stroka) ==12 and len(stroka_igroka) ==12:
    print('НИЧЕГО СЕБЕ - НИЧЬЯ')
elif len(stroka) == 12:
    print('\n\nМашина оказалась удачливее, попробуй еще раз')
elif len(stroka_igroka) == 12:
    print('\n\nТЫ ПОБЕДИЛ, ПОЗДРАВЛЯЮ')