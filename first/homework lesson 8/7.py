"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""
class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return f'{self.re} {"+" if self.im >= 0 else ""}{self.im}i'

    def __repr__(self):
        return self.re, self.im

    def __add__(self, other):
        return MyComplex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return MyComplex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return MyComplex(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)


a = Complex(1, 5)
b = Complex(3, 6)
print(a + b)
print(a - b)
print(a * b)