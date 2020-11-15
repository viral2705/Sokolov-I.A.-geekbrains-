l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
l_new = [el for el in l if l.count(el) == 1]
print(f'Старый лист: {l} \nНовый лист: {l_new}')