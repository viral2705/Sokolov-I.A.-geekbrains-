"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""

class DivisionByZero(Exception):
    def __init__(self, text):
        self.txt = text


try:
    a = float(input('делимое: '))
    b = float(input('делитель: '))
    if b == 0:
        raise DivisionByZero('DivisionByZero error!')
except DivisionByZero as ex:
    print(ex)
else:
    print('частное:', round(a / b, 2))