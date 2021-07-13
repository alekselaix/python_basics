# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
import math



def iter_count(start=1, stop=5):
    try:
        start = int(start)
        stop = int(stop)

        for el in count(start, 1):
            if el > stop:
                break
            else:
                print(el)
    except ValueError:
        print("Invalid args")
        exit()


print("а) итератор, генерирующий целые числа:")
iter_count(-1, 5)


def iter_cycle(abc="ABC", stop=5):
    try:
        abc = str(abc)
        stop = int(stop)

        if stop <= 0:
            print("Fail, Stop >=0")
            exit()

        с = 0
        for el in cycle(abc):
            if с > stop:
                break
            else:
                print(el)
            с += 1
    except ValueError:
        print("Invalid args")
        exit()


print("б) итератор, повторяющий элементы списка:")
iter_cycle("Hello world", 10)
