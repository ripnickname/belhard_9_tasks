"""
Написать функцию add_to_path, которая будет добавлять директорию, в которой находится
переданный файл (путь к файлу) в sys.path
"""

import sys


def add_to_path(path):
    result = sys.path.append(path)
    return result


if __name__ == '__main__':
    add_to_path("/test123")
