"""
Настроить логгирование с модулем logging.

Настроить формат вывода.
Настроить, чтобы вывод шел в файл и в консоль.
Настроить ротацию файла лога по времени (полночь).
"""

import logging
from logging.handlers import TimedRotatingFileHandler

logs = logging.getLogger(__name__)
logs.setLevel(logging.INFO)
log_file = TimedRotatingFileHandler("logs.log", when='midnight')
file_format = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s", datefmt="%H:%M:%S")
log_file.setFormatter(file_format)
logs.addHandler(log_file)


console = logging.StreamHandler()
console_format = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s", datefmt="%H:%M:%S")
console.setFormatter(console_format)
logs.addHandler(console)


if __name__ == '__main__':
    logs.info('INTERNAL SERVER ERROR')
    logs.error('500')
