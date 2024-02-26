class TextHandler:
    def __init__(self) -> None:
        self.txt = []  # атрибут класса - пустой список

    def add_words(self, text):  # метод принимает текст
        self.txt += text.split()  # преобразуем текст в список, добавляем в список self.txt
        # делаем проверку
        if len(self.txt) != 0:  # если список не пустой self.txt
            # формируем список из длин слов
            self.list_num = [len(i) for i in self.txt]
            # находим минимальную длину слова
            self.min_num = min(self.list_num)
            # находим максимальную длину слова
            self.max_num = max(self.list_num)
        else:  # если список пустой
            self.min_num = 0  # минимальная длина слова равна нулю
            self.max_num = 0  # максимальная длина слова равна нулю

    def get_shortest_words(self):
        # метод создает список из слов, равных минимальной длине слова в списке self.txt
        return [i for i in self.txt if len(i) == self.min_num]

    def get_longest_words(self):
        # метод создает список из слов, равных максимальной длине слова в списке self.txt
        return [i for i in self.txt if len(i) == self.max_num]


texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
