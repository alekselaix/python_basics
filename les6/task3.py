# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name: str, surname: str, position: str,
                 profit: float = 0, bonus: float = 0):
        """
        :param name: Имя
        :param surname: Фамилия
        :param position: Должность
        :param profit: Оклад
        :param bonus: Премия
        """
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus


class Position(Worker):

    def get_full_name(self):
        return {self.name + " " + self.surname}

    def get_total_income(self):
        self._income = {"profit": self.profit, "bonus": self.bonus}
        return self._income


user1 = Position("Вася", "Пупкин", "plumber", 35000, 5000)
user2 = Position("Иван", "Иванович", "electric", 55000, 10000)

print("Position full name:", user1.get_full_name(), "position:", user1.position)
print("Position total income:", user1.get_total_income())

print("Position full name:", user2.get_full_name(), "position:", user2.position)
print("Position total income:", user2.get_total_income())
