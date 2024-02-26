# Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен
# a*x**2 + b*x + c
# При создании экземпляра класс должен принимать три аргумента в следующем порядке:

# a — коэффициент a квадратного трехчлена
# b — коэффициент b квадратного трехчлена
# c — коэффициент c квадратного трехчлена
# Экземпляр класса QuadraticPolynomial должен иметь три атрибута:

# a — коэффициент a квадратного трехчлена
# b — коэффициент b квадратного трехчлена
# c — коэффициент c квадратного трехчлена
# Класс QuadraticPolynomial должен иметь четыре свойства:

# x1 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена,
# вычисленный по формуле:

# Если квадратный трехчлен не имеет корней, значением свойства должно быть значение None
# x2 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена,
# вычисленный по формуле:

# Если квадратный трехчлен не имеет корней, значением свойства должно быть значение None

# view — свойство, доступное только для чтения, возвращающее строку вида:
# ax^2 + bx + c
# где a, b и с представляют коэффициенты квадратного трехчлена

# coefficients — свойство, доступное для чтения и записи, возвращающее кортеж вида:
# (a, b, c)
# где a, b и с представляют коэффициенты квадратного трехчлена


class QuadraticPolynomial:

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        self.discriminant = (self.b**2)-(4*self.a*self.c)
        if self.discriminant >= 0:
            x_1 = (-self.b-(self.discriminant)**0.5)/(2*self.a)
            return x_1
        else:
            return None

    @property
    def x2(self):
        self.discriminant = (self.b**2)-(4*self.a*self.c)
        if self.discriminant >= 0:
            x_2 = (-self.b+(self.discriminant)**0.5)/(2*self.a)
            return x_2
        else:
            return None

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, tuple_abc):
        self.a, self.b, self.c = tuple_abc


polynom = QuadraticPolynomial(1, 2, -3)
print('a =', polynom.a)
print('b =', polynom.b)
print('c =', polynom.c)

polynom.coefficients = (1, -5, 6)
print('a =', polynom.a)
print('b =', polynom.b)
print('c =', polynom.c)
print('x1 =', polynom.x1)
print('x2 =', polynom.x2)
print(polynom.view)
