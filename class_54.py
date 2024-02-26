# Реализуйте класс Temperature, описывающий температуру в градусах по шкале Цельсия.
# При создании экземпляра класс должен принимать один аргумент:

# temperature — температура в градусах по шкале Цельсия
# Класс Temperature должен иметь один метод экземпляра:

# to_fahrenheit() — метод, возвращающий температуру по шкале Фаренгейта
# Класс Temperature должен иметь один метод класса:

# from_fahrenheit() — метод, принимающий в качестве аргумента
# температуру по шкале Фаренгейта и возвращающий экземпляр класса
# Temperature, созданный на основе переданной температуры
# Экземпляр класса Temperature должен иметь следующее неформальное
# строковое представление:

# <температура в градусах по шкале Цельсия с округлением
# до двух знаков после запятой>°C
# Также экземпляр класса Temperature должен поддерживать
# приведение к типам bool, int и float:

# при приведении к типу bool значением экземпляра класса Temperature
# должно являться значение True, если его температура выше нуля, или False в противном случае
# при приведении к типу int значением экземпляра класса
# Temperature должна являться его температура в виде целого числа с отброшенной дробной частью
# при приведении к типу float значением экземпляра класса
# Temperature должна являться его температура в виде вещественного числа


class Temperature:

    def __init__(self, temperature) -> None:
        self.temperature = temperature

    def to_fahrenheit(self):
        self.fahrenheit = self.temperature*1.8+32
        return self.fahrenheit

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsium = round((5/9)*(fahrenheit-32), 2)
        return cls(celsium)

    def __str__(self) -> str:
        return f'{self.temperature}°C'

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)


t = Temperature.from_fahrenheit(-459.67)

print(t)
print(bool(t))
print(int(t))
print(f'{float(t):.2f}')
print(f'{t.to_fahrenheit():.2f}')
