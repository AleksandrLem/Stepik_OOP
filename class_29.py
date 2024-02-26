# Реализуйте класс Formatter. При создании экземпляра
# класс не должен принимать никаких аргументов.

# Класс Formatter должен иметь один статический метод:

# format() — метод, принимающий в качестве аргумента объект
# типа int, float, tuple, list или dict и выводящий информацию о
# переданном объекте в формате, зависящем от его типа.
# Если переданный объект принадлежит какому-либо другому типу,
# должно быть возбуждено исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается


from functools import singledispatchmethod


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def format_int(data):
        print(f'Целое число: {data}')

    @format.register(float)
    @staticmethod
    def format_float(data):
        print(f'Вещественное число: {data}')

    @format.register(tuple)
    @staticmethod
    def format_tuple(data):
        print(f'Элементы кортежа: {str(data)[1:-1]}')

    @format.register(list)
    @staticmethod
    def format_list(data):
        outp = [str(i) for i in data]
        outp = ', '.join(outp)
        print(f'Элементы списка: {outp}')

    @format.register(dict)
    @staticmethod
    def format_dict(data):
        print(f'Пары словаря: {str(data.items())[12:-2]}')


Formatter.format(1337)
Formatter.format(20.77)
Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))
Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})

try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)
