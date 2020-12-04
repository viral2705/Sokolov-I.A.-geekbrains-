"""
4) Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5) Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

class MyError(ValueError):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} цена {self.price}"


class StoreWarehouse:

    def __init__(self, name):
        self.name = name
        self.my_stocks = {}

    def __str__(self):
        result = f"Количество товаров - {self.name} \n"
        for good, good_quantity in self.my_stocks.items():
            result = result + f"Количество = {good_quantity} (шт.) - {good}  \n"
        return result

    # Прием на склад
    def reception(self, good):
        try:
            good_quantity = input(f"Введите количество товара ({good.type}-ов) передаваемого на {self.name}: ")
            if good_quantity.isdigit():
                good_quantity = int(good_quantity)
            else:
                raise MyError("Ошибка ввода данных! Попробуйте еще раз")

            self.my_stocks[good] = good_quantity
        except MyError as err:
            print(err)
            return StoreWarehouse.reception(self, good)

    # Передача в подразделение
    def transfer(self, store, good):
        try:
            good_quantity = input(f"Введите количество товара ({good.type}-ов) передаваемого в {store.name}: ")
            if good_quantity.isdigit():
                good_quantity = int(good_quantity)
            else:
                raise MyError("Ошибка ввода данных! Попробуйте еще раз")

            if self.my_stocks[good] - good_quantity < 0:
                raise MyError("Не хватает остатков! Попробуйте еще раз")
            else:
                self.my_stocks[good] = self.my_stocks[good] - good_quantity
                store.my_stocks[good] = good_quantity
        except MyError as err:
            print(err)
            return StoreWarehouse.transfer(self, store, good)


class Printer(OfficeEquipment):
    def __init__(self, name, price, printer_view):
        super().__init__(name, price)
        self.printer_view = printer_view
        self.type = "принтер"

    def to_print(self):
        return f"Печатаем текст на принтере {self.name}"

    def __str__(self):
        return super().__str__() + f", тип принтера = {self.printer_view}"


class Scanner(OfficeEquipment):
    def __init__(self, name, price, document_size):
        super().__init__(name, price)
        self.document_size = document_size
        self.type = "сканер"

    def to_scan(self):
        return f"Сканируем текст на сканере {self.name}"

    def __str__(self):
        return super().__str__() + f", размер бумаги = {self.document_size}"


class Copier(OfficeEquipment):
    def __init__(self, name, price, copy_speed):
        super().__init__(name, price)
        self.copy_speed = copy_speed
        self.type = "ксерокс"

    def to_copier(self):
        return f"Копируем текст на ксероксе {self.name}"

    def __str__(self):
        return super().__str__() + f", скорость печати = {self.copy_speed}"


my_store = StoreWarehouse("наш магазин")
my_warehouse = StoreWarehouse("наш склад")
printer_1 = Printer('HP', 1000, "Лазерный")
scanner_2 = Scanner('Canon', 800, "А3")
copier_3 = Copier('Xerox', 1700, "55 стр/мин")

print(printer_1)
print(scanner_2)
print(copier_3)

my_warehouse.reception(printer_1)
my_warehouse.reception(scanner_2)
my_warehouse.reception(copier_3)
print(my_warehouse)

my_warehouse.transfer(my_store, printer_1)
my_warehouse.transfer(my_store, scanner_2)
my_warehouse.transfer(my_store, copier_3)
print(my_warehouse)
print(my_store)

print(printer_1.to_print())
print(scanner_2.to_scan())
print(copier_3.to_copier())