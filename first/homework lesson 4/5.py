from functools import reduce
l = [el for el in range(100,1001) if el % 2 == 0]
print(l[-1])
def func(a, b):
    return a * b
print(reduce(func, l))