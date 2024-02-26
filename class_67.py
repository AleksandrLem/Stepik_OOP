# Будем считать атрибут защищенным, если его имя начинается
# с символа нижнего подчеркивания (_). Например, _password, __email и __dict__.

# Реализуйте класс ProtectedObject. При создании экземпляра
# класс должен принимать произвольное количество именованных аргументов.
# Все передаваемые аргументы должны устанавливаться создаваемому
# экземпляру в качестве атрибутов.

# Класс ProtectedObject должен запрещать получать и изменять значения
# защищенных атрибутов своих экземпляров, а также удалять эти атрибуты.
# При попытке получить или изменить значение защищенного атрибута,
# а также попытке удалить атрибут, должно возбуждаться исключение AttributeError с текстом:

# Доступ к защищенному атрибуту невозможен
# Примечание 1. Дополнительная проверка данных на корректность не
# требуется. Гарантируется, что реализованный класс используется
# только с корректными данными.


class ProtectedObject:

    def __init__(self, **kwargs) -> None:
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)

    def __getattribute__(self, attr):
        if attr[0] == '_':
            raise AttributeError(f'Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):
        if attr[0] == '_':
            raise AttributeError(f'Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        if attr[0] == '_':
            raise AttributeError(f'Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, attr)


user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

del user.login

try:
    print(user.login)
except AttributeError:
    print('Атрибут отсутствует')
