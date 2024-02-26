# Реализуйте класс NonNegativeObject. При создании экземпляра класс
# должен принимать произвольное количество именованных аргументов.
# Все передаваемые аргументы должны устанавливаться создаваемому
# экземпляру в качестве атрибутов, причем если значением атрибута
# является отрицательное число, оно должно быть взято с противоположным знаком.

# Примечание 1. Числами будем считать экземпляры классов int и float.

# Примечание 2. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.


class NonNegativeObject:

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        for key, value in self.__dict__.items():
            if isinstance(value, (int, float)) and value < 0:
                self.__dict__[key] = abs(value)


point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)

# Решение автора курса
# class NonNegativeObject:
#     def __init__(self, **kwargs):
#         for name, value in kwargs.items():
#             setattr(self, name, value)

#     def __setattr__(self, name, value):
#         if isinstance(value, (int, float)):
#             value = abs(value)
#         object.__setattr__(self, name, value)
