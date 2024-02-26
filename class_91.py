# is_snake() — метод, принимающий в качестве аргумента
# строку и возвращающий True, если переданная
# строка записана в стиле Snake Case, или False в противном случае

# is_upper_camel() — метод, принимающий в качестве
# аргумента строку и возвращающий True, если переданная
# строка записана в стиле Upper Camel Case, или False в
# противном случае

# to_snake() — метод, который принимает в качестве
# аргумента строку в стиле Upper Camel Case, записывает ее
# в стиле Snake Case и возвращает полученный результат

# to_upper_camel() — метод, который принимает в качестве
# аргумента строку в стиле Snake Case, записывает ее в стиле
# Upper Camel Case и возвращает полученный результат


class CaseHelper:

    @staticmethod
    def is_snake(str_text):
        alf_en = 'AEIOUYBCDFGHJKLMNPQRSTVWXZ'
        count = 0
        for i in range(len(str_text)-1):
            if str_text[i] in alf_en or (str_text[i] == '_' and str_text[i+1] == '_'):
                count += 1
        if count > 0:
            return False
        else:
            return True

    @staticmethod
    def is_upper_camel(str_text):
        simbol = '_ __'
        count = 0

        for i in str_text:
            if i in simbol:
                count += 1
        if count > 0:
            return False
        elif str_text[0] != str_text[0].upper():
            return False
        else:
            return True

    @staticmethod
    def to_snake(str_text):
        st = ''
        for i in str_text:
            if i == i.upper():
                st += '_' + i.lower()
            else:
                st += i
        return st[1:]

    @staticmethod
    def to_upper_camel(str_text):
        return str_text.replace('_', ' ').title().replace(' ', '')


#  INPUT DATA:
# TEST_1:
# print(CaseHelper.is_snake('beegeek'))
# print(CaseHelper.is_snake('bee_geek'))
# print(CaseHelper.is_snake('Beegeek'))
# print(CaseHelper.is_snake('BeeGeek'))

# TEST_2:
# print(CaseHelper.is_upper_camel('beegeek'))
# print(CaseHelper.is_upper_camel('bee_geek'))
# print(CaseHelper.is_upper_camel('Beegeek'))
# print(CaseHelper.is_upper_camel('BeeGeek'))

# TEST_3:
# print(CaseHelper.to_snake('Beegeek'))
# print(CaseHelper.to_snake('BeeGeek'))

# # TEST_4:
# print(CaseHelper.to_upper_camel('beegeek'))
# print(CaseHelper.to_upper_camel('bee_geek'))

# TEST_5:
# cases = ['assert_equal', 'tear_down', '__init__',
#          'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup']

# for case in cases:
#     print(CaseHelper.is_snake(case))

# TEST_6:
# cases = ['assert_equal', 'tear_down', '__init__',
#          'assertEqual', 'setUp', 'tearDown', 'run',
#          'exit', 'setup', 'AssertEqual', 'SetUp']

# for case in cases:
#     print(CaseHelper.is_upper_camel(case))

# TEST_7:
# cases = ['AssertEqual', 'SetUp', 'TearDown',
#          'AddModuleCleanup', 'AssertRaisesRegex',
#          'AssertAlmostEqual', 'AssertNotAlmostEqual']

# for case in cases:
#     print(CaseHelper.to_snake(case))

# # TEST_8:
# cases = ['assert_equal', 'tear_down', 'assert_raises_regex',
#          'assert_almost_equal', 'assert_not_almost_equal', 'beegeek']

# for case in cases:
#     print(CaseHelper.to_upper_camel(case))

# TEST_9:
# obj = CaseHelper()
# print(type(obj.is_snake))
# print(type(obj.is_upper_camel))
# print(type(obj.to_snake))
# print(type(obj.to_upper_camel))
