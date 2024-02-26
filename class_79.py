# Реализуйте класс Filter, описывающий объект для фильтрации
# элементов итерируемых объектов. При создании экземпляра класс
# должен принимать один аргумент:

# predicate — функция-предикат; если имеет значение None, то
# работает аналогично функции bool()
# Экземпляр класса Filter должен являться вызываемым
# объектом и принимать один аргумент:

# iterable — итерируемый объект
# Экземпляр класса Filter должен возвращать список, элементами
# которого являются элементы итерируемого объекта iterable, для
# которых функция predicate вернула значение True.

# Примечание 1. Предикат — это функция, которая возвращает True или False
# в зависимости от переданного в качестве аргумента значения.

class Filter:

    def __init__(self, func=None) -> None:
        self.predicate = func or bool
        # self.predicate = predicate if predicate is not None else bool
        # Выражение равнозначно выражению ниже:
        # if predicate is not None:
        #     self.predicate = predicate
        # else:
        #     self.predicate = bool

        # или можно записать так:
        # def __init__(self, func=None):
        #     self.predicate = func or bool

    def __call__(self, iterable):
        # itog_list = []
        # for i in iterable:
        #     if self.predicate(i)==True: # обязательно вызываем i  в self.predicate
        #         itog_list.append(i)
        return [i for i in iterable if self.predicate(i) == True]


leave_even = Filter(lambda x: x % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6]

print(leave_even(numbers))
