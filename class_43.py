# Реализуйте класс Color, описывающий цвет.
# При создании экземпляра класс должен принимать один аргумент:

# hexcode — шестнадцатеричное значение цвета
# Экземпляр класса Color должен иметь три атрибута:

# r — интенсивность красного компонента цвета в виде десятичного числа
# g — интенсивность зеленого компонента цвета в виде десятичного числа
# b — интенсивность синего компонента цвета в виде десятичного числа
# Класс Color должен иметь одно свойство:

# hexcode — свойство, доступное для чтения и записи, возвращающее шестнадцатеричное значение цвета


class Color:

    def __init__(self, hexcode) -> None:
        self._hexcode = hexcode
        self.r = int(self._hexcode[:2], 16)
        self.g = int(self._hexcode[2:4], 16)
        self.b = int(self._hexcode[4:], 16)

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, color_inp):
        self._hexcode = color_inp
        self.r = int(self._hexcode[:2], 16)
        self.g = int(self._hexcode[2:4], 16)
        self.b = int(self._hexcode[4:], 16)


color = Color('0000FF')
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
