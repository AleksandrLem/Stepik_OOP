from functools import singledispatchmethod
import datetime
from datetime import date


class BirthInfo:

    @singledispatchmethod
    def __init__(self, birth_date) -> None:
        self.birth_date = birth_date

    @__init__.register(date)
    def date_init(self, birth_date):
        self.birth_date = date(birth_date)

    @__init__.register(str)
    def date_init(self, birth_date):
        self.birth_date = datetime.datetime.fromisoformat(birth_date)

    @__init__.register(list)
    def date_init(self, birth_date):
        self.birth_date = datetime.datetime(*birth_date)

    # @__init__.register(tuple)
    # def date_init(self, birth_date):
    #     self.birth_date = datetime.datetime(birth_date)


birth_dates = ['20200918', '2020-0918',
               '202009-18', ' 2020-09-18 ', '2020-9-18']

for birth_date in birth_dates:
    try:
        birthinfo1 = BirthInfo(birth_date)
    except TypeError as e:
        print(e)
