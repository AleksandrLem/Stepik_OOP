from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

d1 = date(2024, 1, 22)
print(date.today())
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)

t1 = time(21, 27, 15)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)

print(date.max)
print(date.min)
print(time.max)
print(time.min)

dt = datetime(2024, 1, 22, 21, 32, 11)
print(dt)
print(dt.date().year)
print(dt.time().hour)

print(datetime.max)
print(datetime.min)
print(datetime.now())

now = datetime.now()
print(now.year)
print(now.month)
new_dt = now.replace(year=2023)
print(new_dt)

dt_str = datetime.strptime('30/05/2011', '%d/%m/%Y')
print(dt_str)
dt_str = datetime.strptime('30/05/2011 12:30', '%d/%m/%Y %H:%M')
print(dt_str)
dt_str = datetime.strptime('05-30-2011 12:30', '%m-%d-%Y %H:%M')
print(dt_str)

now = datetime.now()
print(now.strftime('%d %m %Y - (%a)'))
dt2 = date(2022, 11, 7)
print(dt2)
print(dt.strftime('%d.%m.%Y'))
