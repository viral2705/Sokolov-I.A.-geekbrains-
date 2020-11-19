file = 'file_5.txt'
with open(file, 'w', encoding='utf-8') as f:
    words = input('Введите числа через пробел: ')
    f.write(words)

with open(file, 'r', encoding='utf-8') as f:
    string = f.read()
    print(f'Числа: {string}')
    print('Сумма чисел: ' + str(sum([int(word) for word in string.split()])))

