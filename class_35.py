# Реализуйте класс Vector, описывающий вектор на плоскости.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:

# x — координата вектора по оси x
# y — координата вектора по оси y
# Экземпляр класса Vector должен иметь следующее формальное строковое представление:

# Vector(<координата x>, <координата y>)
# Также экземпляры класса Vector должны поддерживать операции
# сравнения с помощью операторов == и!=. Два вектора считаются равными,
# если их координаты по обеим осям совпадают. Методы, реализующие операции
# сравнения, должны уметь сравнивать как два вектора между собой,
# так и вектор с кортежем из двух чисел, представляющих координаты x и y.


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return (self.x, self.y) == other
        return NotImplemented

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"


a = Vector(1, 2)
b = Vector(3, 4)
c = Vector(5, 6)

vectors = [a, b, c]
print(vectors)
