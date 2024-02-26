# Реализуйте класс WeatherWarning, описывающий объект,
# предупреждающий о погодных изменениях. При создании экземпляра
# класс не должен принимать никаких аргументов.

# Класс WeatherWarning должен иметь три метода экземпляра:

# rain() — метод, выводящий текст:
# Ожидаются сильные дожди и ливни с грозой
# snow() — метод, выводящий текст:
# Ожидается снег и усиление ветра
# low_temperature() — метод, выводящий текст:
# Ожидается сильное понижение температуры
# Также реализуйте класс WeatherWarningWithDate,
# наследника класса WeatherWarning, описывающий объект,
# предупреждающий о погодных изменениях с указанием даты.
# Процесс создания экземпляра класса WeatherWarningWithDate
# должен совпадать с процессом создания экземпляра класса WeatherWarning.

# Класс WeatherWarningWithDate должен иметь три метода экземпляра:

# rain() — метод, принимающий в качестве аргумента
# дату (тип date) и выводящий текст:
# <дата в формате DD.MM.YYYY>
# Ожидаются сильные дожди и ливни с грозой
# snow() — метод, принимающий в качестве аргумента дату
# (тип date) и выводящий текст:
# <дата в формате DD.MM.YYYY>
# Ожидается снег и усиление ветра
# low_temperature() — метод, принимающий в качестве
# аргумента дату (тип date) и выводящий текст:
# <дата в формате DD.MM.YYYY>
# Ожидается сильное понижение температуры
# Примечание 1. Дополнительная проверка данных на
# корректность не требуется. Гарантируется, что реализованный
# класс используется только с корректными данными.


from datetime import date


class WeatherWarning:

    def __init__(self) -> None:
        pass

    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):

    def __init__(self) -> None:
        super().__init__()

    def rain(self, date):
        self.date = date.strftime('%d.%m.%Y')
        print(self.date)
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self, date):
        self.date = date.strftime('%d.%m.%Y')
        print(self.date)
        print('Ожидается снег и усиление ветра')

    def low_temperature(self, date):
        self.date = date.strftime('%d.%m.%Y')
        print(self.date)
        print('Ожидается сильное понижение температуры')


weatherwarning = WeatherWarningWithDate()
dates = [date(2004, 6, 29), date(2012, 2, 1), date(1973, 2, 1), date(2020, 7, 8), date(2003, 2, 19), date(2022, 12, 25),
         date(2012, 8, 24), date(1977, 8, 5), date(2017, 5, 26), date(
             1976, 1, 8), date(2017, 11, 13), date(1989, 3, 4),
         date(1971, 12, 9), date(2011, 11, 13), date(
             1970, 6, 29), date(1983, 5, 11), date(1984, 8, 9),
         date(1999, 6, 15), date(2011, 3, 14), date(1980, 5, 26)]

for dt in dates:
    weatherwarning.rain(dt)
    weatherwarning.snow(dt)
    weatherwarning.low_temperature(dt)

# РЕШЕНИЕ АВТОРА КУРСА
# from datetime import date


# class WeatherWarning:
#     @staticmethod
#     def rain():
#         print('Ожидаются сильные дожди и ливни с грозой')

#     @staticmethod
#     def snow():
#         print('Ожидается снег и усиление ветра')

#     @staticmethod
#     def low_temperature():
#         print('Ожидается сильное понижение температуры')


# class WeatherWarningWithDate(WeatherWarning):
#     def rain(self, d: date):
#         print(d.strftime('%d.%m.%Y'))
#         super().rain()

#     def snow(self, d: date):
#         print(d.strftime('%d.%m.%Y'))
#         super().snow()

#     def low_temperature(self, d: date):
#         print(d.strftime('%d.%m.%Y'))
#         super().low_temperature()
