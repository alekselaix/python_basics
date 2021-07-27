# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно.


class Cell:

    def __init__(self, count: int):
        self.count = count

    def __str__(self):
        return f'Результат операции {self.count * "*"}'

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __sub__(self, other):
        if (self.count - other.count) > 0:
            return Cell(self.count - other.count)
        else:
            print("Ошибка операции вычетания")

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.count / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.count % cells_in_row)}'
        return row


cells1 = Cell(1)
cells2 = Cell(9)
# print(cells1)
# print(cells2)
#
# print(cells1 + cells2)
# print(cells1 * cells2)

print(cells2.make_order(3))

print(cells2 - cells1)

print(cells1 / cells2)
