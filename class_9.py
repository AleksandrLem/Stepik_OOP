# Реализуйте класс Circle, описывающий круг. При создании экземпляра
# класс должен принимать один аргумент:

# radius — радиус круга
# Экземпляр класса Circle должен иметь три атрибута:

# _radius — радиус круга
# _diameter — диаметр круга
# _area — площадь круга
# Класс Circle должен иметь три метода экземпляра:

# get_radius() — метод, возвращающий радиус круга
# get_diameter() — метод, возвращающий диаметр круга
# get_area() — метод, возвращающий площадь круга


from math import pi


class Circle:
    '''Данные и площадь круга'''

    def __init__(self, radius):
        self._radius = radius  # защищенный атрибут
        self._diameter = 2*radius  # защищенный атрибут
        self._area = pi*radius**2  # защищенный атрибут

    def get_radius(self):  # геттер - метод, который позволяет внешнему коду увидеть радиус
        return self._radius

    def get_diameter(self):  # геттер - метод, который позволяет внешнему коду увидеть диаметр
        return self._diameter

    def get_area(self):  # геттер - метод, который позволяет внешнему коду увидеть площадь
        return self._area


circle = Circle(3)  # создаем объект класса Circle и передаем значение радиуса

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
