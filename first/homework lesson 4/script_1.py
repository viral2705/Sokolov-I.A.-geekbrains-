from sys import argv
script_name, worktime, coast, perfectly = argv
print("Имя скрипта: ", script_name)
print("Выработка сотрудника в часах: ", worktime)
print("Ставка: ", coast)
print("Премия: ", perfectly)
worktime = int(worktime)
coast = int(coast)
perfectly = int(perfectly)

print(f'Сотрудник заработал за {worktime} часов {worktime * coast + perfectly} рублей.')