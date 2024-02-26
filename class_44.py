# Реализуйте класс FoodInfo, описывающий пищевую ценность продуктов.
# При создании экземпляра класс должен принимать три аргумента в следующем порядке:

# proteins — количество белков в граммах
# fats — количество жиров в граммах
# carbohydrates — количество углеводов в граммах
# Экземпляр класса FoodInfo должен иметь три атрибута:

# proteins — количество белков в граммах
# fats — количество жиров в граммах
# carbohydrates — количество углеводов в граммах
# И следующее формальное строковое представление:

# FoodInfo(<количество белков>, <количество жиров>, <количество углеводов>)
# Также экземпляры класса FoodInfo должны поддерживать между собой операцию
# сложения с помощью оператора +, результатом которой должен являться новый
# экземпляр класса FoodInfo с суммарным количеством белков,
# жиров и углеводов исходных экземпляров.

# Наконец, экземпляр класса FoodInfo должен поддерживать операции умножения,
# деления и деления нацело на число n с помощью операторов *, / и // соответственно:

# результатом умножения должен являться новый экземпляр класса FoodInfo,
# количество белков, жиров и углеводов которого умножены на n
# результатом деления должен являться новый экземпляр класса FoodInfo,
# количество белков, жиров и углеводов которого поделены на n
# результатом деления нацело должен являться новый экземпляр класса FoodInfo,
# количество белков, жиров и углеводов которого поделены нацело на n
# Примечание 1. Числами будем считать экземпляры классов int и float.
# Также будем гарантировать, что экземпляр класса FoodInfo всегда делится на ненулевое число.

# Примечание 2. Если объект, с которым выполняется арифметическая операция,
# некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

# Примечание 3. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.

# Примечание 4. Никаких ограничений касательно реализации класса
# FoodInfo нет, она может быть произвольной.


class FoodInfo:

    def __init__(self, proteins, fats, carbohydrates) -> None:
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self) -> str:
        # Чтобы получить название класса внутри класса можно использовать запись self.__class__.__name__
        return f'{self.__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins,
                            self.fats + other.fats,
                            self.carbohydrates + other.carbohydrates)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            return FoodInfo(self.proteins * n,
                            self.fats * n,
                            self.carbohydrates * n)
        elif isinstance(n, float):
            return FoodInfo(self.proteins * n,
                            self.fats * n,
                            self.carbohydrates * n)
        return NotImplemented

    def __truediv__(self, n):
        if isinstance(n, int):
            return FoodInfo(self.proteins / n,
                            self.fats / n,
                            self.carbohydrates / n)
        elif isinstance(n, float):
            return FoodInfo(self.proteins / n,
                            self.fats / n,
                            self.carbohydrates / n)
        return NotImplemented

    def __floordiv__(self, n):
        if isinstance(n, int):
            return FoodInfo(self.proteins // n,
                            self.fats // n,
                            self.carbohydrates // n)
        elif isinstance(n, float):
            return FoodInfo(self.proteins // n,
                            self.fats // n,
                            self.carbohydrates // n)
        return NotImplemented


food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 10, 20)
print(food1 * 2)
print(food1 / 2)
print(food1 // 2)
print(food1 + food2)

food1 = FoodInfo(10, 20, 30)
not_supported = [1826, -4950968.5187661, 'CpORszTrvuNBLTkwONAK', True,
                 {'their': 1160, 'turn': True,
                     'administration': 75837.8091359427, 'consider': True},
                 (4282, 'pEXkpjHTDfoOodeUvrxX', -65273.7710503699, -
                  630510186.232982, 4626, -20236163552005.9),
                 [9477, 'NevIfZUdzUJrJQMwZvOS', False, True],
                 {False, -1700220.7807578, 'pevZgAzpRcsOVKRoTWsL', 'iQfadxHjqbThjFhieudU'}]

for item in not_supported:
    try:
        food2 = item + food1
    except TypeError:
        print('Некорректный тип данных')
