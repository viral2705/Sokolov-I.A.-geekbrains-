"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
 и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
  реализовать переключение светофора в режимы: красный, желтый, зеленый.
  Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
   третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
    в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time
from itertools import cycle

class TrafficLight:
    __color = 'red'
    __count = 0
    __end = 20

    def run(self):
        for el in cycle([('red', 7), ('yellow', 2), ('green', 7)]):
            self.__color = el[0]
            print(self.__color)
            time.sleep(el[1])
            self.__count += 1
            if self.__count == self.__end:
                break





TrafficLight1  = TrafficLight()
TrafficLight1.run()