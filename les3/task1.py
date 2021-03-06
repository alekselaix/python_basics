# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def deviders(a, b):
    """
    Функция принимает два числа и выполняющую их деление
    :param a: Значение числителя
    :param b: Значение знаменателя
    :return: Возвращает результат деления двух чисел
    """
    try:
        a = float(a)
        b = float(b)
        return a / b

    except TypeError:
        return "Числитель или знаменатель не является числом"

    except ZeroDivisionError:
        return "Ошибка деления на ноль"


user_a = input("Введите значение числителя >>>  ")
user_b = input("Введите значение знаменателя >>> ")

print(deviders(user_a, user_b))
