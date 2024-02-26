# Реализуйте класс Todo, описывающий список дел.
# При создании экземпляра класс не должен принимать никаких аргументов.

# Экземпляр класса Todo должен иметь один атрибут:

# things — изначально пустой список дел, которые нужно выполнить
# Класс Todo должен иметь четыре метода экземпляра:

# add() — метод, принимающий название дела и его приоритет (целое число)
# и добавляющий данное дело в список дел в виде кортежа:
# (<название дела>, <приоритет>)
# get_by_priority() — метод, принимающий в качестве аргумента целое
# число n и возвращающий список названий дел, имеющих приоритет n
# get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет
# get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет

# Примечание 1. Названия дел в списках,
# возвращаемых методами get_by_priority(), get_low_priority() и get_high_priority(),
# должны располагаться в том порядке, в котором они были добавлены в список.

# Примечание 2. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.


class Todo:
    '''Список дел'''

    def __init__(self) -> None:
        self.things = []  # список всех дел с приоритетами
        self.list_visual = []  # список, с делами по приоритету n
        self.list_num = []  # список с номерами приоритетов
        self.list_low = []  # список дел с минимальным приоритетом
        self.list_high = []  # список дел с макисмальным приоритетом

    def add(self, name, num_priority):
        '''Метод принимает название дела и его приоритет'''
        case_num = (name, num_priority)
        self.things.append(case_num)  # += self.things.append(case_num)
        self.list_num.append(num_priority)

    def get_by_priority(self, n=0):
        '''Метод возвращает список дел с приоритетом n'''
        for i in self.things:
            if i[1] == n:
                self.list_visual.append(i[0])
        return self.list_visual

    def get_low_priority(self):
        '''Метод возвращает список дел с самым низким приоритетом'''
        if len(self.list_num) != 0:
            min_num = min(self.list_num)
            for i in self.things:
                if i[1] == min_num:
                    self.list_low.append(i[0])
            return self.list_low
        else:
            return self.list_num

    def get_high_priority(self):
        '''Метод возвращает список дел с самым высоким приоритетом'''
        if len(self.list_num) != 0:
            max_num = max(self.list_num)
            for i in self.things:
                if i[1] == max_num:
                    self.list_high.append(i[0])
            return self.list_high
        else:
            return self.list_num


print('Пример_1')
todo = Todo()
print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())
print()

print('Пример_2')
todo = Todo()
todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)
print(todo.get_by_priority(2))
print(todo.things)
print()

print('Пример_3')
todo = Todo()
todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))
