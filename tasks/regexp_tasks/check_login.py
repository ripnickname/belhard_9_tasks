"""
Написать функцию check_login, которая будет принимать строку и проверять,
что она является логином, который соответствует следующим правилам:
1. Длина от 5 до 20 символов
2. Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания
"""

import re


def check_login(login: str):
    regex = '[A-Za-z0-9_]{5,20}'
    if re.fullmatch(regex, login):
        print('Ok')
    else:
        print('Not Ok')


if __name__ == '__main__':
    check_login('Hello_World')
    check_login('h3110_w0r1d')
    check_login('hell')
    check_login('h311@_w@rld')
    check_login('h311@_w@rldh311@_w@rldh311@_w@rldh311@_w@rldh311@_w@rldh311@_w@rld')
