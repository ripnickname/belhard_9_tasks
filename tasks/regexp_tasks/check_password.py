"""
Написать функцию check_password, которая будет принимать строку и проверять,
что она является паролем, который соответствует следующим правилам:
1. Длина от 8 до 40 символов
2. Должен включать букву верхнего регистра
3. Должен включать букву нижнего регистра
4. Должен включать цифру
5. Должен включать символ (из некоторого набора или исключения)

Подсказка:
Понадобится позитивный просмотр вперед (?=чтото)
"""

import re


def check_password(password: str):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,40}$"
    if re.fullmatch(regex, password):
        print('Ok')
    else:
        print('Not Ok')


if __name__ == '__main__':
    check_password('H3ll@w0r1D')
    check_password('he_ll_o_wo_rL_d96')
    check_password('@HELLOworlD05@')
    check_password('@helloworld')
    check_password('h311@_w@rldh311@_w@rldh311@_w@rldh311@_w@rldh311@_w@rldh311@_w@rld')
