# Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.

# Класс Processor имеет один статический метод:

# process() — метод, который принимает в качестве аргумента
# произвольный объект, преобразует его в зависимости от его типа
# и возвращает полученный результат. Если тип переданного объекта
# не поддерживается методом, возбуждается исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается
# Перепишите метод process() класса Processor с использованием
# декоратора @singledispatchmethod, чтобы он выполнял ту же задачу.

# class Processor:
#     @staticmethod
#     def process(data):
#         if isinstance(data, (int, float)):
#             return data * 2
#         elif isinstance(data, str):
#             return data.upper()
#         elif isinstance(data, list):
#             return sorted(data)
#         elif isinstance(data, tuple):
#             return tuple(sorted(data))
#         raise TypeError('Аргумент переданного типа не поддерживается')

from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def process_1(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def process_2(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def process_3(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def process_4(data):
        return tuple(sorted(data))


print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))
