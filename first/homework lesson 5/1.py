file = 'file_1.txt'
with open(file, 'w', encoding='utf-8') as f:
    while True:
        text = input(('Введите строку, пустая строка - выход: '))
        if text == '':
            break
        else:
            f.writelines(f'{text} \n')


