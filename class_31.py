# Реализуйте для экземпляров класса Rectangle следующее
# формальное и неформальное строковое представление:

# Rectangle(<длина прямоугольника>, <ширина прямоугольника>)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    # Если в классе реализован метод __repr__(), но не реализован метод __str__(),
    # то при передаче экземпляра данного класса в функцию str()
    # вызывается реализованный метод __repr__().
    # def __str__(self):
    #     return f'Rectangle({self.length}, {self.width})' # это можно не писать

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


rectangle = Rectangle(1, 2)
print(str(rectangle))
print(repr(rectangle))

rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(3, 4)
print(rectangle1)
print(repr(rectangle2))
