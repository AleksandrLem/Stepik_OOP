# IP-адрес — это уникальный адрес, идентифицирующий устройство в
# интернете или локальной сети. IP-адреса представляют собой набор из
# четырех целых чисел, разделенных точками. Например, 192.158.1.38.
# Каждое число в наборе принадлежит интервалу от 0 до 255. Таким образом,
# полный диапазон IP-адресации — это адреса от 0.0.0.0 до 255.255.255.255.

# Реализуйте класс IPAddress, описывающий IP-адрес. При создании экземпляра
# класс должен принимать один аргумент:

# ipaddress — IP-адрес, представленный в одном из следующих вариантов:
# строка из четырех целых чисел, разделенных точками
# список или кортеж из четырех целых чисел
# Экземпляр класса IPAddress должен иметь следующее формальное строковое представление:

# IPAddress('<IP-адрес в виде четырех целых чисел, разделенных точками>')
# И следующее неформальное строковое представление:

# <IP-адрес в виде четырех целых чисел, разделенных точками>


from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress) -> None:
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def list_ip(self, ipaddress):
        ip_list = [str(i) for i in ipaddress]
        str_ipaddress = '.'.join(ip_list)
        self.ipaddress = str_ipaddress

    def __str__(self) -> str:
        return self.ipaddress

    def __repr__(self) -> str:
        return f"IPAddress('{self.ipaddress}')"


# Строка
ip = IPAddress('8.8.1.1')
print(str(ip))
print(repr(ip))
# Список
ip = IPAddress([1, 1, 10, 10])
print(str(ip))
print(repr(ip))
# Кортеж
ip = IPAddress((1, 1, 11, 11))
print(str(ip))
print(repr(ip))


# Решение от преподователя
# Чтобы получить название класса внутри класса можно использовать запись self.__class__.__name__.
class IPAddress:
    def __init__(self, ipadress):
        if isinstance(ipadress, str):
            self.ipadress = ipadress
        elif isinstance(ipadress, (list, tuple)):
            self.ipadress = '.'.join(map(str, ipadress))

    def __str__(self):
        return self.ipadress

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.ipadress}')"
