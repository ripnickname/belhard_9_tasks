"""
Написать функцию count_words, которая будет считать количество слов в тексте,
с учетом, что в начале могут быть пробелы, в конце могут быть пробелы, между слов
может встречаться больше одного пробела подряд.
"""

import re


def check_phone(words: str):
    regex = r"\w+"
    result = re.findall(regex, words)
    print(len(result))


if __name__ == '__main__':
    check_phone('hello world hello world hello world')
