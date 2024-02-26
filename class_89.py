from enum import Enum, auto


class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, country):

        country_ru = {'WINTER': 'зима',
                      'SPRING': 'весна',
                      'SUMMER': 'лето',
                      'FALL': 'осень'}

        country_en = {'WINTER': 'winter',
                      'SPRING': 'spring',
                      'SUMMER': 'summer',
                      'FALL': 'fall'}

        if country == 'ru':
            return country_ru[self.name]
        return country_en[self.name]


# INPUT DATA:

# TEST_1:
# print(Seasons.FALL.text_value('ru'))
# print(Seasons.FALL.text_value('en'))

# TEST_2:
# for season in Seasons:
#     print(season.text_value('en'), '->', season.text_value('ru'))

# TEST_3:
# for season in Seasons:
#     print(season.name, season.value)
