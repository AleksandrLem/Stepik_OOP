# Реализуйте функцию get_method_owner(), которая принимает два
# аргумента в следующем порядке:

# cls — произвольный класс
# method — строковое название метода
# Функция должна возвращать класс, от которого класс cls
# унаследовал метод method.
# Если метода method нет ни в самом классе, ни в одном другом
# классе из его иерархии, функция get_method_owner() должна вернуть значение None.

def get_method_owner(cls, method):
    for i in cls.mro():
        if method in i.__dict__:
            return i
    return None


class A:
    def m(self):
        pass


class B(A):
    pass


print(get_method_owner(B, 'm'))
print(B.mro())
