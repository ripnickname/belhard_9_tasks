"""
Написать функцию convert_date, которая будет конвертировать время
из одной временной зоны в другую.

Функция должна принимать 3 аргумента: timestamp, current_zone, new_zone.

Функция должна возвращать время в новой временной зоне.
"""

from datetime import datetime

import pytz


def convert_date(timestamp, current_zone, new_zone):
    current_date = datetime.fromtimestamp(timestamp)
    current_location = pytz.timezone(current_zone)
    new_location = pytz.timezone(new_zone)
    new_location_timezone = current_location.localize(current_date)
    return new_location_timezone.astimezone(new_location)


if __name__ == '__main__':
    print(convert_date(1545730073, "Etc/Greenwich", "Australia/Melbourne"))
