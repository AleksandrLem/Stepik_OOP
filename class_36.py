# Будем называть словом любую последовательность из одной или более латинских букв.

# Реализуйте класс Word, описывающий слово.
# При создании экземпляра класс должен принимать один аргумент:

# word — слово
# Экземпляр класса Word должен иметь следующее формальное строковое представление:

# Word('<слово в исходном виде>')
# И следующее неформальное строковое представление:

# <слово, в котором первая буква заглавная, а все остальные строчные>
# Также экземпляры класса Word должны поддерживать между собой все
# операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два
# слова считаются равными, если их длины совпадают. Слово считается больше
# другого слова, если его длина больше.

# Примечание 1. Если объект, с которым выполняется операция сравнения,
# некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

# Примечание 2. Дополнительная проверка данных на корректность не требуется.
# Гарантируется, что реализованный класс используется только с корректными данными.

# Примечание 3. Никаких ограничений касательно реализации класса Word нет,
# она может быть произвольной.


from functools import total_ordering


@total_ordering
class Word:

    def __init__(self, word) -> None:
        self.word = word

    def __str__(self) -> str:
        return self.word.capitalize()

    def __repr__(self) -> str:
        return f"Word('{self.word}')"

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Word):
            return len(self.word) > len(other.word)
        return NotImplemented


a = Word('python')
print(str(a))
print(repr(a))

print(Word('bee') == Word('hey'))
print(Word('bee') < Word('geek'))
print(Word('bee') > Word('geek'))
print(Word('bee') <= Word('geek'))
print(Word('bee') >= Word('gee'))


words = [Word('python'), Word('bee'), Word('geek')]

print(sorted(words))
print(min(words))
print(max(words))


words = [Word('miss'), Word('notice'), Word('forget'), Word('six'), Word('son'), Word('every'), Word('response'),
         Word('success'), Word('million'), Word('game'), Word(
             'most'), Word('economic'), Word('guy'), Word('worry'),
         Word('professional'), Word('sea'), Word('role'), Word(
             'determine'), Word('drive'), Word('value'), Word('tend'),
         Word('forget'), Word('policy'), Word('bit'), Word(
             'property'), Word('officer'), Word('truth'), Word('reduce'),
         Word('suggest'), Word('rest'), Word('seat'), Word(
             'candidate'), Word('according'), Word('he'), Word('reach'),
         Word('five'), Word('food'), Word('purpose'), Word(
             'center'), Word('last'), Word('power'), Word('goal'),
         Word('happy'), Word('pattern'), Word('pretty'), Word(
             'control'), Word('share'), Word('better'), Word('this'),
         Word('give'), Word('and'), Word('clear'), Word(
             'argue'), Word('into'), Word('alone'), Word('sea'),
         Word('hour'), Word('response'), Word('occur'), Word(
             'consumer'), Word('bring'), Word('expect'), Word('until'),
         Word('race'), Word('fall'), Word('charge'), Word(
             'meet'), Word('still'), Word('single'), Word('consider'),
         Word('less'), Word('special'), Word('building'), Word(
             'body'), Word('often'), Word('window'), Word('dinner'),
         Word('small'), Word('stop'), Word('above'), Word(
             'lead'), Word('huge'), Word('despite'), Word('direction'),
         Word('city'), Word('couple'), Word('conference'), Word(
             'purpose'), Word('oil'), Word('chance'), Word('home'),
         Word('practice'), Word('perhaps'), Word('coach'), Word(
             'gas'), Word('may'), Word('quickly'), Word('officer'),
         Word('free'), Word('let')]

print(sorted(words))
print(min(words))
print(max(words))

word = Word('Beegeek')

print(word.__eq__(1))
print(word.__ne__(1.1))
print(word.__gt__(range(5)))
print(word.__lt__([1, 2, 3]))
print(word.__ge__({4, 5, 6}))
print(word.__le__({1: 'one'}))
