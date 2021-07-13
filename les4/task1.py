# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
from les4 import salary_mod

try:
    file, time, rate, bonus = argv
except ValueError:
    print("Invalid args")
    exit()

print(salary_mod.calc(time, rate, bonus))
