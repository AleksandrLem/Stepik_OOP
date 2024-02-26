# Реализуйте класс Negator. При создании экземпляра класс не должен принимать никаких аргументов.

# Класс Negator должен иметь один статический метод:

# neg() — метод, принимающий в качестве аргумента объект и возвращающий
# его противоположное значение. Если методу передается целое или вещественное
# число, он должен возвращать это число, взятое с противоположным знаком.
# Если методу в качестве аргумента передается булево значение, он должен
# возвращать булево значение, противоположное переданному. Если
# переданный объект принадлежит какому-либо другому типу, должно быть
# возбуждено исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается


from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def neg_1(data):
        return -1*data

    @neg.register(bool)
    @staticmethod
    def neg_2(data):
        if data == True:
            return False
        else:
            return True


print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))

try:
    Negator.neg('number')
except TypeError as e:
    print(e)
