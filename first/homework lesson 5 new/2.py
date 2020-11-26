file ='file_2.txt'
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f'Строк в файле {len(lines)}')
    for i, line in enumerate(lines):
        print(f'В строке {i}  {len(line.split())} слов')

