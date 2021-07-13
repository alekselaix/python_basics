# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

# первый вариант решения
from functools import reduce

user_list = [el for el in range(100, 1001) if el % 2 == 0]


def user_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


print(reduce(user_func, user_list))

# второй вариант решения
print(reduce(lambda result, i: result * i, range(100, 1001, 2)))
