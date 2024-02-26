# Реализуйте класс HourClock, описывающий часы с одной лишь часовой стрелкой.
# При создании экземпляра класс должен принимать один аргумент:

# hours — количество часов. Если hours не является целым числом,
# принадлежащим диапазону [1; 12], должно быть возбуждено исключение ValueError с текстом:
# Некорректное время
# Класс HourClock должен иметь одно свойство:

# hours — свойство, доступное для чтения и записи, возвращающее
# текущее количество часов. При изменении свойство должно проверять,
# что новое значение является целым числом, принадлежащим диапазону [1; 12],
# в противном случае должно быть возбуждено исключение ValueError с текстом:
# Некорректное время


class HourClock:
    def __init__(self, hours) -> None:
        self.hours = hours  # присваиваем свойство в инициализаторе

    def get_hours(self):
        return self._hours  # метод возвращает значение self._hours

    def set_hours(self, hours):  # метод проверяет и меняет занчение self._hours
        if isinstance(hours, int) and 1 <= hours <= 12:
            self._hours = hours
        else:
            raise ValueError('Некорректное время')

    # свойство hours, где геттер - get_hours, сеттер - set_hours
    hours = property(get_hours, set_hours)


time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)


try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)
