_author_= 'Швец Александр Николаевич'
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class School:
    def __init__(self, class_room):
        self.class_room = {
            "class_num": int(class_room.split()[0]),
            "class_letter": class_room.split()[1]
        }
    def get_name(self):
        return str(self.class_room["class_num"]) + " " + self.class_room["class_letter"]

class Person:
    def __init__(self, name, surname, second_name):
        self.name = name
        self.surname = surname
        self.second_name = second_name

    def full_name(self):
        return self.surname + " " + self.name + " " + self.second_name

class Pupil(Person):
    def __init__(self, name, surname, second_name, class_room, father, mother):
        Person.__init__(self, name, surname, second_name)
        self.class_room = class_room
        self.father = father
        self.mother = mother

    def get_class(self):
        return self.class_room

    def roditeli(self):
        return self.father.full_name(), self.mother.full_name()

class Teacher(Person):
    def __init__(self, name, surname, second_name, classes, subject):
        Person.__init__(self, name, surname, second_name)
        self.class_room = classes
        self.subject = subject

    def classes(self):
        return self.class_room

    def subject1(self):
        return self.subject

class_rooms = ["8 А", "9 Б", "10 В"]
father = [Person("Иван", "Сидоров", "Игоревич"),
            Person("Игорь", "Иванов", "Александрович"),
            Person("Николай", "Петров", "Александрович")]
mother = [Person("Татьяна", "Сидорова", "Максимовна"),
            Person("Ирина", "Иванова", "Александровна"),
            Person("Светлана", "Петрова", "Николаевна")]
pupils = [Pupil("Александр", "Иванов", "Игоревич", class_rooms[0], father[1], mother[1]),
            Pupil("Петр", "Сидоров", 'Иванович', class_rooms[1], father[0], mother[0]),
            Pupil("Иван", "Петров", 'Николаевич', class_rooms[1], father[2], mother[2]),
            Pupil("Алексей", "Иванов", "Игоревич", class_rooms[2], father[1], mother[1]),
            Pupil("Евгений", "Сидоров", 'Иванович', class_rooms[2], father[0], mother[0]),
            Pupil("Андрей", "Петров", 'Николаевич', class_rooms[2], father[2], mother[2])]
teachers = [Teacher("Иван", "Сидоров", "Игоревич", [class_rooms[0], class_rooms[1], class_rooms[2]], 'Математика'),
            Teacher("Игорь", "Иванов", "Александрович", [class_rooms[1], class_rooms[2]], 'История'),
            Teacher("Николай", "Петров", "Александрович", class_rooms[2], 'Английский')]
# 1. Получить полный список всех классов школы
print("Получить полный список всех классов школы ")
for School in class_rooms:
    print(School)
print()
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
print("Получить список всех учеников в указанном классе")
for num, Pupil in enumerate(pupils, start=1):
    print("Все ученики в классе: {}) {} {}".format(num, Pupil.get_class(), Pupil.full_name()))
print()
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
print("Получить список всех предметов указанного ученика")
for num, Pupil in enumerate(pupils, start=1):
    print('ученик - ', Pupil.full_name(), 'изучает:')
    for num, Teacher in enumerate(teachers, start=1):
        if Pupil.get_class() in Teacher.classes():
            print(Teacher.subject1())
print()
# 4. Узнать ФИО родителей указанного ученика
print("Узнать ФИО родителей указанного ученика")
for num, Pupil in enumerate(pupils, start=1):
    print("Родители всех учеников: {}) Ученик: {} Родители: {} и {}".format(num, Pupil.full_name(), Pupil.roditeli()[1], Pupil.roditeli()[0]))
print()
# 5. Получить список всех Учителей, преподающих в указанном классе
print("Получить список всех Учителей, преподающих в указанном классе")
for num, Teacher in enumerate(teachers, start=1):
    print(Teacher.classes(), Teacher.full_name())