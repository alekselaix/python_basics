# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    _color = ''
    _states = {'Красный': 7, 'Желтый': 2, 'Зеленый': 6}

    def running(self):
        for color, timer in self._states.items():
            self._color = color
            print(f"Горит {self._color}, ждите {timer} секунд")
            sleep(timer)


traffic = TrafficLight()
traffic.running()
