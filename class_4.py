# Реализуйте класс Circle, описывающий круг.
# При создании экземпляра класс должен принимать один аргумент:

# radius — радиус круга
# Экземпляр класса Circle должен иметь три атрибута:

# radius — радиус круга
# diameter — диаметр круга
# area — площадь круга
from math import pi


class Circle:
    '''Класс <Круг>, с атрибутами радуса, диаметра и площади'''

    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2*radius
        self.area = pi*radius**2


circle = Circle(3)
print(circle.radius)
print(circle.diameter)
print(round(circle.area, 2))
print(Circle.__doc__)
