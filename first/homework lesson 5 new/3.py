file ='file_3.txt'
cash = 0
rich_list = []
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, text in enumerate(lines):
        text = text.split()
        cash += int(text[1])
        if int(text[1]) < 20000:
            rich_list.append(text[0])
print(f'Сотрудники с ЗП Меньше 20000: {rich_list},\n'
      f'Средняя зарплата {int(cash / len(lines))}')


