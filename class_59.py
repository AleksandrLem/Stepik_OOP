# Реализуйте класс DefaultObject. При создании экземпляра класс должен
# принимать один именованный аргумент default, имеющий значение
# по умолчанию None, а после произвольное количество именованных
# аргументов. Аргументы, передаваемые после default, должны устанавливаться
# создаваемому экземпляру в качестве атрибутов.

# При обращении к несуществующему атрибуту экземпляра класса
# DefaultObject должно возвращаться значение default.

class DefaultObject:

    def __init__(self, default=None, **kwargs) -> None:
        self.__dict__.update(kwargs)
        self.default = default

    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):
        return self.default

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value

# god = DefaultObject()
# god.name = 'Ares'
# print(god.name)
# god.mythology = 'greek'
# print(god.mythology)
# print(god.age)


god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')

print(god.name)
print(god.mythology)
print(god.age)

'''Решение автора курса'''
# class DefaultObject:
#     def __init__(self, default=None, **kwargs):
#         self.default = default
#         self.__dict__.update(kwargs)

#     def __getattr__(self, name):
#         return self.default
