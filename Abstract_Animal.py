from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        print('Не определен')

    @abstractmethod
    def move(self):
        print('move Animal')
        print('Животное движется')


class Cat(Animal):
    def sound(self):
        print('sound Cat')
        print('мяу')

    def move(self):
        print('move Cat')
        super().move()
        print('Кот движется')


cat = Cat()

cat.move()
cat.sound()
