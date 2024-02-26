# Реализуйте класс Gun, описывающий ружье.
# При создании экземпляра класс не должен принимать никаких аргументов.

# Класс Gun должен иметь один метод экземпляра:

# shoot() — метод, при первом вызове которого выводится строка pif,
# при втором — paf, при третьем — pif, при четвертом — paf, и так далее


class Gun:
    '''Класс, который описывает ружье'''

    def __init__(self):
        self.count = 0

    def shoot(self):
        self.count += 1
        if self.count % 2 == 0:
            print('paf')
        else:
            print('pif')


gun = Gun()
gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
print(gun.count)
print(gun.__doc__)
