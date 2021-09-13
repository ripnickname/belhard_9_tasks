"""
Реализация Haversine formula для Python.
https://en.wikipedia.org/wiki/Haversine_formula

Написать функцию distance, которая будет возвращать расстояние между
точками GPS на карте в метрах.

Функция должна принимать следующие аргументы:
* a_lat - широта первой точки
* a_lon - долгота первой точки
* b_lat - широта второй точки
* b_lon - долгота второй точки

Алгоритм:
1. Посчитать значение каждой координаты в радианах.
Формула: float(value) * pi / 180
2. Вычислить sin и cos радианов широт из п1.
3. Вычислить разницу (delta) радианов долгот из п1.
4. Вычислить sin и cos разницы долгот из п3.
5. Вычислить y = sqrt(pow(b_lat_cos * delta_sin, 2)) + pow(a_lat_cos * b_lat_sin - a_lat_sin * b_lat_cos * delta_cos, 2))
6. Вычислить x = a_lat_sin * b_lat_sin + a_lat_cos * b_lat_cos * delta_cos
7. Вычислить ad = atan2(y, x)
8. Вернуть ad * EARTH_R
"""

import math

# радиус сферы (Земли)
EARTH_R = 6372795


def distance(lat1, lon1, lat2, lon2):
    lat = math.radians(lat2 - lat1)
    lon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(lon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return EARTH_R * c


if __name__ == '__main__':
    print(distance(55.75, 37.6167, 53.8387, 27.5780))
