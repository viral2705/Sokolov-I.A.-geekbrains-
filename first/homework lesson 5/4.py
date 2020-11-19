file = 'file_4.txt'
rus_file = 'file_4_rus.txt'
list = {'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
}
with open(file, 'r', encoding='utf-8') as f:
    #lines = f.readlines()
    rus_lines = []
    for line in f:
        rus_lines.append(f'{list[line.split(" - ")[0]]} - {line.split(" - ")[-1]}')
with open(rus_file, 'w', encoding='utf-8') as f:
    f.writelines(rus_lines)