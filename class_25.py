# Квадратный трехчлен — это многочлен вида
# a*x**2+b*x+c
# Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.
# При создании экземпляра класс должен принимать три аргумента в следующем порядке:

# a — коэффициент a квадратного трехчлена
# b — коэффициент b квадратного трехчлена
# c — коэффициент c квадратного трехчлена
# Экземпляр класса QuadraticPolynomial должен иметь три атрибута:

# a — коэффициент a квадратного трехчлена
# b — коэффициент b квадратного трехчлена
# c — коэффициент c квадратного трехчлена
# Класс QuadraticPolynomial должен иметь два метода класса:

# from_iterable() — метод, принимающий в качестве аргумента
# итерируемый объект из трех элементов a, b и c, которые
# представляют коэффициенты квадратного трехчлена, и возвращающий
# экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов

# from_str() — метод, принимающий в качестве аргумента строку,
# которая содержит коэффициенты a, b и c квадратного трехчлена,
# записанные через пробел. Метод должен возвращать экземпляр класса QuadraticPolynomial,
# созданный на основе переданных коэффициентов, предварительно
# преобразованных в экземпляры класса float


class QuadraticPolynomial:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, list_abc):
        return cls(list_abc[0], list_abc[1], list_abc[2])

    @classmethod
    def from_str(cls, string_abc):
        string_abc = string_abc.split()
        string_abc = [float(i) for i in string_abc]
        return cls(string_abc[0], string_abc[1], string_abc[2])


# polynom = QuadraticPolynomial(1, -5, 6)

# print(polynom.a)
# print(polynom.b)
# print(polynom.c)


# polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

# print(polynom.a)
# print(polynom.b)
# print(polynom.c)

# polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

# print(polynom.a)
# print(polynom.b)
# print(polynom.c)
# print(polynom.a + polynom.b + polynom.c)
