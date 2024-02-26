# Требовалось реализовать класс Logger. При создании экземпляра
# класс не должен был принимать никаких аргументов.

# Предполагалось, что при установке или изменении значения
# атрибута экземпляра класса Logger будет выводиться текст:

# Изменение значения атрибута <имя атрибута> на <новое значение атрибута>
# Также планировалось, что при удалении атрибута будет выводиться текст:

# Удаление атрибута <имя атрибута>


class Logger:

    def __setattr__(self, attr, value):
        print(f'Изменение значения атрибута {attr} на {value}')
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print(f'Удаляю атрибут {attr}')
        del self.__dict__[attr]


class Set_Del:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        object.__delattr__(self, name)

obj = Logger()

obj.name = 'pygen'
obj.rating = '5*'
obj.ceo = 'Timur'
obj.rating = '6*'
del obj.rating
