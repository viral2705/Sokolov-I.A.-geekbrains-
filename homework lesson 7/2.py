"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class cloth(ABC):
    @abstractmethod
    def summ(self):
        pass

class coat(cloth):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 20:
            self._size = 20
        elif size > 60:
            self._size = 60
        else:
            self._size = size

    def summ(self):
        return int(self._size / 6.5 + 0.5)


class costume(cloth):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 50:
            self._height = 50
        elif height > 200:
            self._height = 200
        else:
            self._height = height

    @property
    def summ(self):
        return self._height * 2  + 0.3





new_coat = coat(80)
print(f'Размер пальто: {new_coat.size}')
print(f'Ткань для пальто: : {new_coat.summ()}')


new_costume = costume(180)
print(f'Длина костюма: {new_costume.height}')
print(f'Ткань для костюма: {new_costume.summ}')