# Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс
# не должен принимать никаких аргументов.

# Класс Gun должен иметь три метода экземпляра:

# shoot() — метод, при первом вызове которого выводится строка pif,
# при втором — paf, при третьем — pif, при четвертом — paf, и так далее
# shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
# shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля


class Gun:
    '''Класс для ружья'''

    def __init__(self):
        self.count = 0   # создаем счетчик

    def shoot(self):
        # плюсуем 1 при каждом вызове функции, выводим нужную запись
        self.count += 1
        if self.count % 2 != 0:
            return print('pif')
        else:
            return print('paf')

    def shots_count(self):  # функция возвращает значение счетчика
        print('количество pif-paf:', end=' ')
        return self.count

    def shots_reset(self):  # обнуляем счетчит
        self.count = 0
        return print('счетчик обнулен')


gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
