# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class Treug:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def ploshad(self):
        return abs((0.5*(((self.x1-self.x3)*(self.y2-self.y3))-((self.x2-self.x3)*(self.y1-self.y3)))))

    def storoni(self):
        st1 = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        st2 = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        st3 = math.sqrt(((self.x3 - self.x1) ** 2) + ((self.y3 - self.y1) ** 2))
        return st1, st2, st3

    def perimetr(self):
        return Treug.storoni(self)[0] + Treug.storoni(self)[1] + Treug.storoni(self)[2]

    def visota(self):
        p = Treug.perimetr(self)*0.5
        st1 = Treug.storoni(self)[0]
        st2 = Treug.storoni(self)[1]
        st3 = Treug.storoni(self)[2]
        h1= 2*(math.sqrt(p*(p-st1)*(p-st2)*(p-st3)))/st1
        h2= 2*(math.sqrt(p*(p-st1)*(p-st2)*(p-st3)))/st2
        h3= 2*(math.sqrt(p*(p-st1)*(p-st2)*(p-st3)))/st3
        return h1,h2,h3


#treugolnik1 = Treug(3,2,7,5,0,0)
treugolnik1 = Treug(-1,4,-1,2,-7,3)
print('Площадь - ', treugolnik1.ploshad())
print('Периметр - ', treugolnik1.perimetr())
print('Все 3 возможные высоты данного треугольника - \n', treugolnik1.visota(), sep='')




# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
'''
Принимаем что точки фигуры задаются таким образом  - 12
                                                     43
'''
import math
try:
    class Trapecia:
        def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
            self.x3 = x3
            self.y3 = y3
            self.x4 = x4
            self.y4 = y4

        def storoni(self):
            st1 = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
            st2 = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
            st3 = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
            st4 = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
            return st1,st2,st3,st4

        def proverka(self):
            #если 12 параллельно 34
            if abs(self.y2-self.y1)/abs(self.x2-self.x1)==abs(self.y3-self.y4)/abs(self.x3-self.x4):
                if abs(self.x3-self.x2)==abs(self.x4-self.x1) and abs(self.y3-self.y2)==abs(self.y4-self.y1):
                    return True, 1
            #если 14 параллельно 23
            elif abs(self.y3-self.y2)/abs(self.x3-self.x2)==abs(self.y4-self.y1)/abs(self.x4-self.x1):
                if self.x2-self.x1==self.x3-self.x4 and self.y2-self.y1==self.y3-self.y4:
                    return True, 2
            return False

        def perimetr(self):
            return Trapecia.storoni(self)[0] + Trapecia.storoni(self)[1] + Trapecia.storoni(self)[2] + \
                   Trapecia.storoni(self)[3]

        def ploshad(self):
            #смотри какие стороны были параллельны: 12 к 34 или 14 к 23
            if Trapecia.proverka(self)[1] == 1:
                st1 = Trapecia.storoni(self)[0]
                st2 = Trapecia.storoni(self)[1]
                st3 = Trapecia.storoni(self)[2]
                st4 = Trapecia.storoni(self)[3]
                return ((st1+st3)/2)*math.sqrt(st4**2-((((st3-st1)**2+(st4)**2-(st2)**2)/(2*(st3-st1)))**2))
            else:
                return ((st2+st4)/2)*math.sqrt(st1**2-((((st4-st2)**2+(st1)**2-(st3)**2)/(2*(st4-st2)))**2))
except Exception:
    print('Что-то вы не так ввели')


trapecia1 = Trapecia(-1,3,1,3,3,-3,-3,-3)
print('ДА, она равнобочная' if trapecia1.proverka()[0] else 'Нет, не равнобочная')
print('Длины сторон - ', trapecia1.storoni())
print('Периметр фигуры - ' , trapecia1.perimetr())
print('Площадь фигуры  - ', trapecia1.ploshad())