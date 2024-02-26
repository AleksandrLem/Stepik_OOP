# Реализуйте класс StrExtension, описывающий набор функций для работы со строками.
# При создании экземпляра класс не должен принимать никаких аргументов.

# Класс StrExtension должен иметь три статических метода:

# remove_vowels() — метод, который принимает в качестве аргумента строку,
# удаляет из нее все гласные латинские буквы без учета регистра и возвращает полученный результат

# leave_alpha() — метод, который принимает в качестве аргумента строку,
# удаляет из нее все символы, не являющиеся латинскими буквами, и возвращает полученный результат

# replace_all() — метод, который принимает три строковых аргумента
# string, chars и char, заменяет в строке string все символы из chars на char
# с учетом регистра и возвращает полученный результат.


class StrExtension:

    def remove_vowels(stroka):
        '''метод принимает строку и удаляет все гласные из неё без учета регистра'''
        stroka_new = ''
        for i in stroka:
            if i not in 'aeiouyAEIOUY':
                stroka_new += i
        return stroka_new

    def leave_alpha(stroka):
        '''метод удаляет все символы, которые не являются латинскими буквами'''
        stroka_new = ''
        for i in stroka:
            if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                stroka_new += i
        return stroka_new

    def replace_all(string, chars, char):
        '''метод заменяет все символы из chars на char с учетом регистра'''
        for i in string:
            if i in chars:
                string = string.replace(i, char)
        return string


print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))

print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))

print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
