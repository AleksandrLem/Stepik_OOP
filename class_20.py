# Реализуйте класс Postman, описывающий почтальона.
# При создании экземпляра класс не должен принимать никаких аргументов.

# Экземпляр класса Postman должен иметь один атрибут:

# delivery_data — изначально пустой список адресов, по которым следует доставить письма
# Экземпляр класса Postman должен иметь три метода экземпляра:

# add_delivery() — метод, принимающий в качестве аргументов улицу,
# дом и квартиру, и добавляющий в список адресов эти данные в виде кортежа:
# (<улица>, <дом>, <квартира>)
# get_houses_for_street() — метод, принимающий в качестве аргумента
# улицу и возвращающий список всех домов на этой улице, в которые требуется доставить письма
# get_flats_for_house() — метод, принимающий в качестве аргументов
# улицу и дом и возвращающий список всех квартир в этом доме, в которые требуется доставить письма
# Примечание 1. Дома и квартиры в списках, возвращаемых методами
# get_houses_for_street() и get_flats_for_house(), должны располагаться
# в том порядке, в котором они были добавлены.

# Примечание 2. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.

class Postman:
    '''Класс почтальон'''

    def __init__(self) -> None:
        self.delivery_data = []

    def add_delivery(self, name_street, num_house, num_apartment):
        '''метод создает список картежей, в картеже улица, дом, квартира'''
        self.delivery_data.append((name_street, num_house, num_apartment))

    def get_houses_for_street(self, name_street):
        '''метод принимает название улицы и выводит список всех домов на этой улице'''
        num_house = []  # номер дома
        for i in self.delivery_data:
            if i[0] == name_street and i[1] not in num_house:
                num_house.append(i[1])
        return num_house

    def get_flats_for_house(self, name_street, num_house):
        '''метод принимает улиц, дом и выводит номер квартиры'''
        num_apartment = []  # номер квартиры
        for i in self.delivery_data:
            if i[0] == name_street and i[1] == num_house and i[2] not in num_apartment:
                num_apartment.append(i[2])
        return num_apartment


postman = Postman()

print(postman.delivery_data)
print(postman.get_houses_for_street('3-я ул. Строителей'))
print(postman.get_flats_for_house('3-я ул. Строителей', 25))


postman = Postman()

postman.add_delivery('Советская', 131, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Громова', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.delivery_data)
print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
