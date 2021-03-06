# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# ** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x=1, y=-1):
    """
    Решение задачи первым способом — возведение в степень с помощью оператора **
    :param x: целое положительное число x
    :param y:целое отрицательнре число y
    :return:возращает x в степени y
    """

    try:
        if x > 0 and y < 0 and y % 1 == 0:
            return x ** y
        else:
            print("Численные занчения аргументов заданы некорректно")

    except TypeError:
        return "Один или более аргументов не являются числом"


print("Решение первым способом")
print(my_func(10, -1))
print(my_func(3, -5))
print(my_func(1.5, -1))
print(my_func("text", -4))


def my_func1(x=1, y=-1):
    """
    Решение задачи вторым способом — более сложная реализация без оператора **,
    предусматривающая использование цикла.
    :param x: целое положительное число x
    :param y: целое отрицательнре число y
    :return: возращает x в степени y
    """
    try:
        if x > 0 and y < 0 and y % 1 == 0:
            for i in range(1, abs(y)):
                x *= x
            return 1 / x
        else:
            print("Численные занчения аргументов заданы некорректно")

    except TypeError:
        return "Один или более аргументов не являются числом"


print("\nРешение вторым способом")
print(my_func1(10, -1))
print(my_func1(3, -5))
print(my_func1(1.5, -1))
print(my_func1("text", -4))
