from functools import total_ordering


@total_ordering
class Version:

    def __init__(self, version) -> None:
        # сначала определяем вид строки
        self.version = version
        if '.' not in version:
            version = version + '.0.0'
            self.version = version
        elif version.count('.') == 1:
            version = version + '.0'
            self.version = version
        elif version.count('.') == 2:
            self.version = version
        # далее вытаскиваем числа между точек
            # список с индексами, где расположены точки
        list_index = [i for i in range(
            len(self.version)) if self.version[i] == '.']
        index1 = list_index[0]  # индекс первой точки
        index2 = list_index[1]  # индекс всторой точки
        num1 = int(self.version[:index1])
        num2 = int(self.version[index1+1:index2])
        num3 = int(self.version[index2+1:])
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.tuple_num = (num1, num2, num3)

    def __str__(self) -> str:
        return self.version

    def __repr__(self) -> str:
        return f"Version('{self.version}')"

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.tuple_num == other.tuple_num
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Version):
            return self.tuple_num > other.tuple_num
        return NotImplemented


a = Version('33')
print(str(a))
print(repr(a))
print(a.num1, a.num2, a.num3)
b = Version('1.100')
print(str(b))
print(repr(b))
c = Version('3.123.2')
print(str(c))
print(repr(c))
# print(a.version_int)
# print()

print(Version('3.0.3') == Version('1.11.28'))
print(Version('3.0.3') < Version('1.11.28'))
print(Version('3.0.3') > Version('1.11.28'))
print(Version('3.0.3') <= Version('1.11.28'))
print(Version('3.0.3') >= Version('1.11.28'))

print()
print(Version('3') == Version('3.0'))
print(Version('3') == Version('3.0.0'))
print(Version('3.0') == Version('3.0.0'))

versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))


'''Р Е Ш Е Н И Е   П Р Е П О Д А В А Т Е Л Я'''


class Version:
    def __init__(self, version):
        self._parts = [int(i) for i in version.split('.')]
        self._parts += [0] * (3 - len(self._parts))

    def __str__(self):
        return '{}.{}.{}'.format(*self._parts)

    def __repr__(self):
        return "Version('{}.{}.{}')".format(*self._parts)

    def __eq__(self, other):
        if isinstance(other, Version):
            return self._parts == other._parts
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self._parts < other._parts
        return NotImplemented
