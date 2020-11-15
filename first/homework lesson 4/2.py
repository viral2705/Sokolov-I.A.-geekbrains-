l = [1, 2, 100, 15, 3, 4, 55, 92]
new_l = [el for i, el in enumerate(l) if el > l[i -1] ]

print(f'Исходный список: {l} \n'
      f'Новый список: {new_l}')
