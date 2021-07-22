# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        """

        :param speed: скорость
        :param color: цвет
        :param name: модель
        :param is_police: полиция
        """

        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):

        return f'{self.name} is started'

    def stop(self):

        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher'
        else:
            return f'Speed of {self.name} is normal'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher'
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police'
        else:
            return f'{self.name} is not from police'


audi_rs = SportCar(100, 'Red', 'Audi RS 6', False)
bmw_m5 = SportCar(200, 'Black', 'BMW M5', True)
print(bmw_m5.go())
print(bmw_m5.stop())
print(bmw_m5.turn_right())
print(bmw_m5.turn_left())
print(bmw_m5.show_speed())
print(bmw_m5.is_police)

lada2101 = TownCar(120, 'Red', 'Lada 2101', False)
print(lada2101.show_speed())

largus = WorkCar(100, 'blue', 'Lada Largus', False)
print(largus.show_speed())

ford = PoliceCar(250, 'blue', 'Ford Crown Victoria', True)
print(ford.show_speed())
print(ford.police())