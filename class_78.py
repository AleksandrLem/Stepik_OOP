class UpperPrintString(str):

    def __str__(self):
        return f'{self.words()}'

    def words(self):
        return self.upper()


s = UpperPrintString('beegeek')
print(list(s))
