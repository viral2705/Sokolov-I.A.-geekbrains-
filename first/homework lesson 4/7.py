def func(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
        yield num


for el in func(10):
    print(el)