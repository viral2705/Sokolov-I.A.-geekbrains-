"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class Data:
    def __init__(self, dd_mm_yy):
        self.day_month_year = str(dd_mm_yy)

    @classmethod
    def extract(cls, dd_mm_yy):
        my_date = []

        for i in dd_mm_yy.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'

today = Data('11 - 1 - 2001')
print(Data.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(today)
print(Data.validation(11, 11, 2022))
print(today.validation(11, 13, 2011))
print(Data.validation(1, 11, 2000))

