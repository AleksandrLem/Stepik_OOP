# Реализуйте класс Month, описывающий месяц.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:

# year — год
# month — порядковый номер месяца
# Экземпляр класса Month должен иметь следующее формальное строковое представление:

# Month(<год>, <порядковый номер месяца>)
# И следующее неформальное строковое представление:

# <год>-<порядковый номер месяца>
# Также экземпляры класса Month должны поддерживать
# все операции сравнения с помощью операторов ==, !=, >, <, >=, <=.
# Два Month объекта считаются равными, если их годы и
# порядковые номера месяцев совпадают. Month объект считается
# больше другого Month объекта, если его год больше.
# В случае если два Month объекта имеют равные года, большим считается тот,
# чей месяц больше. Методы, реализующие операции сравнения, должны
# уметь сравнивать как два Month объекта между собой, так и Month объект
# с кортежем из двух чисел, представляющих год и месяц.

# Примечание 1. Если объект, с которым выполняется операция сравнения,
# некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

# Примечание 2. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.

# Примечание 3. Никаких ограничений касательно реализации класса
# Month нет, она может быть произвольной.


from functools import total_ordering


@total_ordering
class Month:

    def __init__(self, year, month) -> None:
        self.year = year
        self.month = month
        self.year_month = (self.year, self.month)

    def __str__(self) -> str:
        return f'{self.year}-{self.month}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.year}, {self.month})'

    def __eq__(self, other) -> bool:
        if isinstance(other, Month):
            return self.year_month == other.year_month
        elif isinstance(other, tuple):
            return self.year_month == other
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, Month):
            return self.year_month > other.year_month
        elif isinstance(other, tuple):
            return self.year_month > other
        return NotImplemented


print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]
print(sorted(months))
print(min(months))
print(max(months))

print(Month(1999, 12) == (1999, 12))
print(Month(1999, 12) < (2000, 1))
print(Month(1999, 12) > (2000, 1))
print(Month(1999, 12) <= (1999, 12))
print(Month(1999, 12) >= (2000, 1))
