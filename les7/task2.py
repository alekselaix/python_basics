# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def rate_coat(self):
        return self.width / 6.5 + 0.5

    def rate_costume(self):
        return self.height * 2 + 0.3

    @property
    def full_clothes(self):
        return str(f'Общая площадь ткани:'
                   f'{(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, _width, _height):
        super().__init__(_width, _height)
        self.rate_coat = self.width / 6.5 + 0.5

    def __str__(self):
        return f'Площадь ткани на пальто: {self.rate_coat}'


class Costume(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.rate_costume = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площаль ткани на костюм: {self.rate_costume}'


coat = Coat(2, 1)
costume = Costume(1, 4)
print(coat)
print(costume)
print(coat.full_clothes)
print(costume.full_clothes)

print(coat.rate_coat)
print(costume.rate_costume)
