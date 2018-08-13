_author_= 'Швец Александр Николаевич'
# Задание-1: Решите задачу (дублированную ниже):
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import os
z = 'F:\Загрузки'
class Sotrudnik:
    def __init__(self, stroka):
        self.stroka = stroka

    def full_name(self):
        return str(self.stroka).split(' ')[0][2:] + ' ' + str(self.stroka).split(' ')[1][:-2]

    def zarplata(self):
        norma = float(str(self.stroka).split(' ')[3][0:-1])
        otrabotal = float(str(self.stroka).split(' ')[2][0:-1])
        stavka = float(str(self.stroka).split(' ')[4][0:-1])
        if otrabotal > norma:
            zp = stavka + 2*((stavka/norma)*(otrabotal-norma))
        else:
            zp = stavka * (otrabotal/norma)
        return zp


def analiz_faila(papka, file, poziciya):
    path = os.path.join(papka, file)
    with open(path, 'r', encoding='UTF-8') as f:
        yy = dict()
        for line in f:
            line = line.split(' ')
            line = list(filter(len, line))
            line[-1] = line[-1].replace('\n', '')
            if line[poziciya].isdigit() or line[poziciya].find('.') != -1:
                yy[line[0] + ' ' + line[1]] = float(line[poziciya])
        return yy
otrabotano_chasov = analiz_faila(z, 'hours_of',2)
polojeno_chasov = analiz_faila(z, 'workers', 4)
zarplata = analiz_faila(z, 'workers',2)

new_spisok = []
for key in otrabotano_chasov.keys():
    new_spisok.append(key)
    new_spisok.append(otrabotano_chasov.get(key))
    new_spisok.append(polojeno_chasov.get(key))
    new_spisok.append(zarplata.get(key))
x=0
while x < len(new_spisok):
    print('Получает на вход строку - ', new_spisok[x:x+4])
    a = Sotrudnik(new_spisok[x:x+4])
    print('Получаем на выходе - ', a.full_name(), a.zarplata())
    x+=4
    print()