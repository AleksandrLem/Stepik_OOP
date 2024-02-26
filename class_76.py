# Реализуйте класс Time, описывающий время на цифровых часах.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:

# hours — количество часов; каждые 24 часа должны преобразовываться в 0 часов
# minutes — количество минут; каждые 60 минут должны преобразовываться в 1 час
# Экземпляр класса Time должен иметь следующее неформальное строковое представление:

# <количество часов в формате HH>:<количество минут в формате MM>
# Также экземпляры класса Time должны поддерживать между собой
# операцию сложения с помощью операторов + и +=:

# результатом сложения с помощью оператора + должен являться новый
# экземпляр класса Time, количество часов которого равно сумме часов
# исходных экземпляров класса Time, количество минут — сумме минут исходных экземпляров класса Time
# результатом сложения с помощью оператора += должен являться
# левый экземпляр класса Time, количество часов которого увеличено
# на количество часов правого экземпляра класса Time, количество
# минут — на количество минут правого экземпляра класса Time
# Примечание 1. Если объект, с которым выполняется арифметическая
# операция, некорректен, метод, реализующий эту операцию, должен
# вернуть константу NotImplemented.

# Примечание 2. Никаких ограничений касательно реализации класса
# Time нет, она может быть произвольной.


class Time:

    def __init__(self, hours, minutes) -> None:

        self.hours = self.hour_itog(hours, minutes)
        self.minutes = self.minut(minutes)

    def __str__(self) -> str:
        return f'{self.hours:02}:{self.minutes:02}'

    @staticmethod
    def minut(m):
        return m % 60

    @staticmethod
    def hour_itog(h, m):
        h = (h + m//60) % 24
        return h

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours,
                        self.minutes + other.minutes)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, Time):

            self.hours += other.hours
            self.hours = (self.hours + (self.minutes + other.minutes)//60) % 24
            self.minutes += other.minutes
            self.minutes = self.minutes % 60
            return self
        return NotImplemented


t1 = Time(15, 50)
t2 = Time(2, 20)
print(t1 + t2)

t1 += Time(2, 20)
print(t1)
