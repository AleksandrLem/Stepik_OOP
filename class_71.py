# 1. Реализуйте класс BasicPlan, описывающий подписку базового
# уровня на некотором онлайн-сервисе. При создании экземпляра
# класс не должен принимать никаких аргументов.

# 2. Также реализуйте класс SilverPlan, наследника класса BasicPlan,
# описывающий подписку среднего уровня на некотором онлайн-сервисе.
# Процесс создания экземпляра класса SilverPlan должен совпадать с
# процессом создания экземпляра класса BasicPlan.

# 3. Наконец, реализуйте класс GoldPlan, наследника класса BasicPlan,
# описывающий подписку высокого уровня на некотором онлайн-сервисе.
# Процесс создания экземпляра класса GoldPlan должен совпадать с
# процессом создания экземпляра класса BasicPlan.


class BasicPlan:

    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'


class SilverPlan(BasicPlan):

    has_HD = True
    num_of_devices = 2
    price = '12.99$'


class GoldPlan(BasicPlan):

    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'


print(GoldPlan.can_stream)
print(GoldPlan.can_download)
print(GoldPlan.has_SD)
print(GoldPlan.has_HD)
print(GoldPlan.has_UHD)
print(GoldPlan.num_of_devices)
print(GoldPlan.price)
