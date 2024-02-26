
# Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс
# не должен принимать никаких аргументов.
# Класс Gun должен иметь один метод экземпляра:
# shoot() — метод, при вызове которого выводится строка pif

class Gun:

    def shoot(self):
        print('pif')


gun = Gun()
gun.shoot()

# Вам доступен класс User, описывающий интернет-пользователя.
# При создании экземпляра класс принимает один аргумент:
# name — имя пользователя
# Экземпляр класса User имеет два атрибута:
# name — имя пользователя
# friends — количество друзей пользователя, начальным значением является 0
# Класс User имеет один метод экземпляра:
# add_friends() — метод, принимающий в качестве аргумента
# целое число n и увеличивающий количество друзей пользователя на n


class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n


user = User('Aleksandr')
print('количество друзей', user.friends)
user.add_friends(3)
user.add_friends(2)
user.add_friends(2)
print('количество друзей', user.friends)
print('\n', 'имя: ', user.name, '\n', 'количество друзей: ', user.friends)
