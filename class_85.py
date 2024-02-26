# 1. Реализуйте класс USADate, описывающий дату в американском формате.
# При создании экземпляра класс должен принимать три аргумента в следующем порядке:

# year — год
# month — месяц
# day — день
# Класс USADate должен иметь два метода экземпляра:

# format() — метод, который возвращает строку, представляющую собой дату в формате MM-DD-YYYY
# iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
# 2. Также реализуйте класс ItalianDate, описывающий дату в итальянском формате,
# конструктор которого принимает три аргумента:

# year — год
# month — месяц
# day — день
# Класс ItalianDate должен иметь два метода экземпляра:

# format() — который возвращает строку, представляющую собой дату в формате DD/MM/YYYY
# iso_format() — который возвращает строку, представляющую собой дату в формате YYYY-MM-DD


class USADate:

    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{self.month:02}-{self.day:02}-{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month:02}-{self.day:02}'


class ItalianDate(USADate):

    def format(self):
        return f'{self.day:02}/{self.month:02}/{self.year}'


usadate = USADate(2023, 4, 6)
print(usadate.format())
print(usadate.iso_format())

italiandate = ItalianDate(2023, 4, 6)
print(italiandate.format())
print(italiandate.iso_format())
