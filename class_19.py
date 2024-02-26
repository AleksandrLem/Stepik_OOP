# Вам доступен класс Person, описывающий человека.
# При создании экземпляра класс принимает два аргумента в следующем порядке:

# name — имя человека
# surname — фамилия человека
# Экземпляр класса Person имеет два атрибута:

# name — имя человека
# surname — фамилия человека
# Класс Person имеет одно свойство:

# fullname — свойство, доступное для чтения и записи,
# возвращающее полное имя человека в виде строки:
# <имя> <фамилия>
# Реализуйте свойство fullname класса Person с помощью декоратора @property.

# Примечание 1. При изменении имени и/или фамилии человека должно
# изменяться и его полное имя. Аналогично при изменении полного
# имени должны изменяться имя и фамилия.

# Примечание 2. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.

class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()


# person = Person('Mike', 'Pondsmith')
# print(person.name)
# print(person.surname)
# print(person.fullname)

# person = Person('Mike', 'Pondsmith')
# person.name = 'Troy'
# print(person.fullname)

# person = Person('Mike', 'Pondsmith')
# person.surname = 'Baker'
# print(person.fullname)

# person = Person('Mike', 'Pondsmith')
# person.fullname = 'Troy Baker'
# print(person.name)
# print(person.surname)
