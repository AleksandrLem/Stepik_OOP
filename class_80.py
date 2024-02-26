# Реализуйте класс DateFormatter, экземпляры которого позволяют
# преобразовывать даты в формат определенной страны из таблицы выше.
# При создании экземпляра класс должен принимать один аргумент:

# country_code — код страны
# Экземпляр класса DateFormatter должен являться вызываемым
# объектом и принимать один аргумент:

# d — дата (тип date)
# Экземпляр класса DateFormatter должен возвращать строку с
# датой d в формате страны с кодом country_code.


from datetime import date


class DateFormatter:

    def __init__(self, country_code) -> None:
        self.country_code = country_code
        self.__dt = {
            "ru": "%d.%m.%Y",
            "us": "%m-%d-%Y",
            "ca": "%Y-%m-%d",
            "br": "%d/%m/%Y",
            "fr": "%d.%m.%Y",
            "pt": "%d-%m-%Y"
        }

    def __call__(self, d):
        for key, value in self.__dt.items():
            if key == self.country_code:
                return (d.strftime(value))


ru_format = DateFormatter('ru')
print(ru_format(date(2022, 11, 7)))

us_format = DateFormatter('us')
print(us_format(date(2022, 11, 7)))

ca_format = DateFormatter('ca')
print(ca_format(date(2022, 11, 7)))
