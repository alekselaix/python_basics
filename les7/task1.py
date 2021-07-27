# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, lists):
        self.lists = deepcopy(lists)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.lists])

    def size(self):
        return len(self.lists), len(self.lists[0])

    def __add__(self, other):
        if isinstance(other, Matrix) and self.size() == other.size():
            return Matrix([[a + b for a, b in zip(x, y)] for x, y in zip(self.lists, other.lists)])
        else:
            print("Matrix size Error")


matrix1 = Matrix([[5, 1, 55], [1, 4, 2]])
print(matrix1, '\n')

matrix2 = Matrix([[1, 2, 1], [1, 2, 77], [1, 0, 0]])
print(matrix2, '\n')

print(matrix1 + matrix2)
