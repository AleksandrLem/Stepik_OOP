# Реализуйте пустой класс PiggyBank,
# а затем создайте экземпляр этого класса и присвойте его переменной money_box.

class PiggyBank:
    pass


money_box = PiggyBank()

# Реализуйте пустой класс PiggyBank, а затем
# создайте два экземпляра этого класса и присвойте их переменным money_box1 и money_box2.
# Экземпляр money_box1 должен иметь:
# атрибут coins со значением 10
# Экземпляр money_box2 должен иметь:
# атрибут coins со значением 15
# атрибут color со значением 'pink'


class PiggyBank:
    pass


money_box1 = PiggyBank()
money_box2 = PiggyBank()

money_box1.coins = 10
money_box2.coins = 15
money_box2.color = 'pink'

# Реализуйте класс PiggyBank, а затем
# создайте экземпляр этого класса и присвойте его переменной money_box.
# Класс PiggyBank должен иметь:
# атрибут content со значением 'coins'
# атрибут alternate_name со значением 'penny bank'


class PiggyBank:
    '''документация класса'''  # так реализуется документация класса
    content = 'coins'
    alternate_name = 'penny bank'


money_box = PiggyBank()
print(PiggyBank.__doc__)
print(money_box.__dir__)
print(PiggyBank.__dict__)
money_box.color = 'white'
print(money_box.__dict__)
