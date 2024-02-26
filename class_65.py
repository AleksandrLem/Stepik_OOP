# Реализуйте класс AttrsNumberObject. При создании экземпляра класс
# должен принимать произвольное количество именованных аргументов.
# Все передаваемые аргументы должны устанавливаться создаваемому
# экземпляру в качестве атрибутов.

# Экземпляр класса AttrsNumberObject должен иметь один атрибут:

# attrs_num — количество атрибутов, которыми обладает экземпляр класса
# AttrsNumberObject на данный момент, включая сам атрибут attrs_num
# Примечание 1. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.

class AttrsNumberObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
        self.attrs_num = 0

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    def __getattribute__(self, attr):
        if attr == 'attrs_num':
            attr = len(self.__dict__)
            return attr
        return object.__getattribute__(self, attr)


music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)


# Решение автора курса
# class AttrsNumberObject:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)

#     def __getattr__(self, name):
#         if name == 'attrs_num':
#             return len(self.__dict__) + 1
