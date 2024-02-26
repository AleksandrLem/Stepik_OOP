class Vector:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x,
                          self.y - other.y)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return Vector(self.x * n,
                          self.y * n)
        return NotImplemented

    def __rmul__(self, n):
        return self.__mul__(n)

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return Vector(self.x / n,
                          self.y / n)
        return NotImplemented

# a = Vector(1, 2)
# b = Vector(3, 4)

# print(a + b)
# print(a - b)
# print(b + a)
# print(b - a)


a = Vector(3, 4)

print(a * 2)
print(2 * a)
print(a / 2)
