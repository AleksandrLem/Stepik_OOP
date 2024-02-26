# Реализуйте класс Vector, описывающий вектор на плоскости.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:

# x — координата вектора по оси x
# y — координата вектора по оси y
# Экземпляр класса Vector должен иметь следующее неформальное строковое представление:

# (<координата x>, <координата y>)
# Также экземпляр класса Vector должен поддерживать приведение
# к типам bool, int, float и complex:

# при приведении к типу bool значением вектора должно являться значение True,
# если хотя бы одна его координата не равна нулю, или False в противном случае

# при приведении к типу int значением вектора должен являться его модуль
# в виде целого числа с отброшенной дробной частью

# при приведении к типу float значением вектора должен являться его
# модуль в виде вещественного числа
# при приведении к типу complex значением вектора должно являться
# комплексное число, вещественная часть которого равна координате вектора по оси
# x, мнимая часть — координате вектора по оси y

# Примечание 1. Модуль вектора с координатами

# (x,y) вычисляется по формуле sqrt(x**2+y**2)

# Примечание 2. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.

# Примечание 3. Никаких ограничений касательно реализации класса
# Vector нет, она может быть произвольной.


from math import sqrt


class Vector:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        modul = sqrt(x**2+y**2)
        self.modul = modul

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __int__(self):
        return int(self.modul)

    def __float__(self):
        return float(self.modul)

    def __complex__(self):
        return complex(self.x, self.y)


vector = Vector(8, -1)
print(vector)
print(bool(vector))
print(complex(vector))
