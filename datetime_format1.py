from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

tdata = {
    "ru": "%d.%m.%Y",
    "us": "%m-%d-%Y",
    "ca": "%Y-%m-%d",
    "br": "%d/%m/%Y",
    "fr": "%d.%m.%Y",
    "pt": "%d-%m-%Y"
}

str_country = 'ru'
d = date(2022, 11, 7)

for key, value in tdata.items():
    if key == str_country:
        print(d.strftime(value))
print(d.strftime(tdata[str_country]))
