"""
Написать функцию find_emails, которая принимает текст и находит в нем
все email вида some@some.some
"""

import re


def find_emails(text: str):
    emails = re.findall(r"[A-Za-z0-9]+@[a-z0-9]+\.[a-z]+", text)
    print(emails)


if __name__ == '__main__':
    find_emails("pavel@gmail.com, pavel, johndoe@outlook.com, john_@.com")
