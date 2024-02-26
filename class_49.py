# Реализуйте класс RaiseTo, экземпляры которого позволяют
# возводить числа в фиксированную степень. При создании
# экземпляра класс должен принимать один аргумент:

# degree — показатель степени
# Экземпляр класса RaiseTo должен являться вызываемым
# объектом и принимать один аргумент:

# x — число
# Экземпляр класса RaiseTo должен возвращать значение
# x в степени degree.


class RaiseTo:

    def __init__(self, degree) -> None:
        self.degree = degree

    def __call__(self, x):
        return x**self.degree


raise_to_three = RaiseTo(3)
raise_to_four = RaiseTo(4)

print(raise_to_three(3))
print(raise_to_four(2))
