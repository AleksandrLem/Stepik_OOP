# Коды состояния HTTP представляют собой трехзначные целые
# числа и используются для указания успешности конкретного
# HTTP запроса. Выделяют пять групп кодов состояния:

# информация (100-199)
# успех (200-299)
# перенаправление (300-399)
# ошибка клиента (400-499)
# ошибка сервера (500-599)

# Реализуйте класс HTTPStatusCodes, описывающий
# перечисление с  кодами состояния HTTP.
# Перечисление должно иметь пять элементов:

# CONTINUE — элемент со значением 100
# OK — элемент со значением 200
# USE_PROXY — элемент со значением 305
# NOT_FOUND — элемент со значением 404
# BAD_GATEWAY — элемент со значением 502
# Элемент перечисления должен иметь два метода:

# info() — метод, возвращающий двухэлементный
# кортеж, содержащий имя элемента и его значение
# code_class() — метод, возвращающий название
# группы на русском, к которой относится элемент

from enum import Enum


class HTTPStatusCodes(Enum):

    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        rus_info = {'CONTINUE': 'информация',
                    'OK': 'успех',
                    'USE_PROXY': 'перенаправление',
                    'NOT_FOUND': 'ошибка клиента',
                    'BAD_GATEWAY': 'ошибка сервера'}
        return rus_info[self.name]


# TEST_1:
print(HTTPStatusCodes.OK.info())
print(HTTPStatusCodes.OK.code_class())

# TEST_2:
print(HTTPStatusCodes.CONTINUE.info())
print(HTTPStatusCodes.CONTINUE.code_class())

# TEST_3:
print(HTTPStatusCodes.USE_PROXY.info())
print(HTTPStatusCodes.USE_PROXY.code_class())

# TEST_4:
print(HTTPStatusCodes.NOT_FOUND.info())
print(HTTPStatusCodes.NOT_FOUND.code_class())

# TEST_5:
print(HTTPStatusCodes.BAD_GATEWAY.info())
print(HTTPStatusCodes.BAD_GATEWAY.code_class())

# TEST_6:
for instance in HTTPStatusCodes:
    print(f'{instance.name} -> {instance.value}')
