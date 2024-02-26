# Реализуйте класс Rectangle, описывающий прямоугольник.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:

# length — длина прямоугольника
# width — ширина прямоугольника
# Экземпляр класса Rectangle должен иметь два атрибута:

# length — длина прямоугольника
# width — ширина прямоугольника
# Класс Rectangle должен иметь два свойства:

# perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
# area — свойство, доступное только для чтения, возвращающее площадь прямоугольника

class Rectangle:
    def __init__(self, length=0, width=0) -> None:
        self.length = length
        self.width = width

    def perimeter_fun(self):
        return 2*self.length+2*self.width

    def area_fun(self):
        return self.length*self.width

    perimeter = property(perimeter_fun)
    area = property(area_fun)


rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
