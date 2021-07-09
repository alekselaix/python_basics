# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def summa():
    """
    Программа запрашивает у пользователя строку чисел, разделенных пробелом.
    Далее текст по заданию, не пишу его.
    Для выхода используется q.
    :return:
    """

    temp = 0
    while True:
        user_data = input("Введите строку чисел через пробел (выход q)>>>").split()

        for elem in user_data:
            try:
                temp = temp + float(elem)
            except ValueError:

                if elem == 'Q' and elem == 'q':
                    print(temp)
                    exit(0)
                else:
                    print(temp)
                    exit(0)
        print(temp)


summa()