"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула: {direction}')

    def showspeed(self):
        print(f'Текущая скорость авто: {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def showspeed(self):
        if self.speed < 60:
            print(f'Текущая скорость {self.speed}')
        else:
            print(f'Текущая скорость {self.speed}, Скорость превышена!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def showspeed(self):
        if self.speed < 40:
            print(f'Текущая скорость {self.speed}')
        else:
            print(f'Текущая скорость {self.speed}, Скорость превышена!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)





car = TownCar(speed=10, color='white', name='Mersedes')
print(f'Модель авто: {car.name}\n'
      f'Цвет авто: {car.color}')
car.stop()
car.go()
car.turn('left')
car.showspeed()
car.speed = 100
car.showspeed()

car2 = PoliceCar(speed=350, color='black', name='Bugatti',)
print(f'Модель авто: {car2.name}\n'
      f'Цвет авто: {car2.color}')
car2.stop()
car2.go()
car2.turn('right')
car2.showspeed()
car2.speed = 100
car2.showspeed()

