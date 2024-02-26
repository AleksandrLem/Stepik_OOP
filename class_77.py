# Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости.
# При создании экземпляра класс должен принимать три аргумента в следующем порядке:

# x — координата точки по оси x
# y — координата точки по оси y
# color — цвет точки
# Класс ColoredPoint должен иметь три свойства:

# x — свойство, доступное только для чтения, возвращающее координату точки по оси x
# y — свойство, доступное только для чтения, возвращающее координату точки по оси y
# color — свойство, доступное только для чтения, возвращающее цвет точки
# Экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:

# ColoredPoint(<координата x>, <координата y>, '<цвет точки>')
# Также экземпляры класса ColoredPoint должны поддерживать между собой
# операции сравнения с помощью операторов == и !=. Две цветные точки
# считаются равными, если их цвета и координаты по обеим осям совпадают.

# Наконец, при передаче экземпляра класса ColoredPoint в функцию hash()
# должно возвращаться его хеш-значение, вычисленное с помощью функции hash()
# на основе кортежа, первым элементом которого является координата точки по оси
# x, вторым — координата точки по оси
# y, третьим — цвет точки.

# Примечание 1. Если объект, с которым происходит сравнение, некорректен,
# метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.

# Примечание 2. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными


class ColoredPoint:

    def __init__(self, x, y, color) -> None:
        self._x = x
        self._y = y
        self._color = color

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_color(self):
        return self._color

    x = property(get_x)
    y = property(get_y)
    color = property(get_color)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}, '{self.color}')"

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self.x == other.x and self.y == other.y and self.color == other.color
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ColoredPoint):
            return self.x != other.x or self.y != other.y or self.color != other.color
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))


point1 = ColoredPoint(10, 20, 'black')
point2 = ColoredPoint(10, 20, 'black')

print(point1 == point2)
print(point1 != point2)
