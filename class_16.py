# Реализуйте класс Person, описывающий человека.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:

# name — имя человека
# surname — фамилия человека
# Экземпляр класса Person должен иметь два атрибута:

# name — имя человека
# surname — фамилия человека
# Класс Person должен иметь одно свойство:

# fullname — свойство, доступное для чтения и записи,
# возвращающее полное имя человека в виде строки:
# <имя> <фамилия>
# Примечание 1. При изменении имени и/или фамилии человека
# должно изменяться и его полное имя. Аналогично при
# изменении полного имени должны изменяться имя и фамилия.

# Примечание 2. Дополнительная проверка данных на
# корректность не требуется. Гарантируется, что реализованный
# класс используется только с корректными данными.

class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_full_name(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_full_name, set_full_name)


print('Пример_1:')
person = Person('Меган', 'Фокс')
print(person.name)
print(person.surname)
print(person.fullname)
print()

print('Пример_2:')
person = Person('Меган', 'Фокс')
person.name = 'Стефани'
print(person.fullname)
print()

print('Пример_3:')
person = Person('Алан', 'Тьюринг')
person.surname = 'Вирт'
print(person.fullname)
print()

print('Пример_4:')
person = Person('Джон', 'Маккарти')
person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)
