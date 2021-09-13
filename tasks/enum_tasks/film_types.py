"""
Написать класс FilmTypes, который будет наследоваться от Enum и содержать
константы-названия жанров фильмов.
"""

from enum import Enum


class FilmTypes(Enum):
    COMEDY = 1
    BIOPIC = 2
    ANIME = 3
    DRAMA = 4
    DETECTIVE = 5
    THRILLER = 6
