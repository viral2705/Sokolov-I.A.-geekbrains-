import itertools

def count_func(start, stop):
    for el in itertools.count(start):
        if el > stop:
            break
        else:
            print(el)

def cycle_func(list, end):
    i = 0
    for el in itertools.cycle(list):
        if i > end:
            break
        print(el)
        i += 1


count_func(int(input('Введите стартовый символ: ')), int(input('Введите конечный символ: ')))
cycle_func([1,2,3,4,5,6,7,8,9,0], int(input('Сколько элементов итерируем? ')))