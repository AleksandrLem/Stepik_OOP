# Реализуйте класс Strip, экземпляры которого позволяют удалять из начала
# и конца строки определенные символы. При создании экземпляра
# класс должен принимать один аргумент:

# chars — строка, в которой перечислены удаляемые символы
# Экземпляр класса Strip должен являться вызываемым объектом и
# принимать один аргумент:

# string — строка
# Экземпляр класса Strip должен удалять из начала и конца строки
# string все символы, перечисленные в chars, и возвращать полученный результат.

# Примечание 1. Дополнительная проверка данных на корректность
# не требуется. Гарантируется, что реализованный класс используется
# только с корректными данными.

# Примечание 2. Никаких ограничений касательно реализации класса
# Strip нет, она может быть произвольной.


class Strip:

    def __init__(self, chars) -> None:
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)


strip = Strip('!? ')

print(strip('     ?beegeek!'))
print(strip('!bee?geek!'))
strip = Strip('.,+-')

print(strip('     --++beegeek++--'))
print(strip('-bee...geek-'))
print(strip('-+,.b-e-e-g-e-e-k-+,.'))
