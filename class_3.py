# Вам доступен класс House, описывающий дом.
# При создании экземпляра класс принимает два аргумента в следующем порядке:

# color — цвет дома
# rooms — количество комнат в доме
# Экземпляр данного класса имеет два атрибута:

# color — цвет дома
# rooms — количество комнат в доме
# Реализуйте для класса House два метода экземпляра:

# paint() — метод, принимающий в качестве аргумента
# значение new_color и изменяющий текущий цвет дома на new_color
# add_rooms() — метод, принимающий в качестве аргумента целое
# число n и увеличивающий количество комнат в доме на n

class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_rooms(self, n):
        self.rooms += n


# экземпляр класса
house = House('white', 4)
print('цвет дома', house.color)
print('количество комнат', house.rooms)

# экземпляр класса
house = House('white', 4)
# меняем цвет
house.paint('black')
# добавляем комнату
house.add_rooms(1)

print('цвет дома', house.color)
print('количество комнат', house.rooms)
