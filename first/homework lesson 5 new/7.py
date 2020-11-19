'''
 Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.

'''
import json

file = 'file_7.txt'
new_file = 'file_7.json'
def cash(profit, costs):
    revenue = int(profit) - int(costs)
    return revenue

def converter_to_dict(string):
    firm, _, pr, cos = string.split()
    revenue = cash(pr, cos)
    return {firm: revenue}, revenue

with open(file, 'r', encoding='utf=8') as f:
    result = {}
    summ = 0
    count_profit_firm = 0
    for line in f:
        current_obj, revenue = converter_to_dict(line)
        result.update(current_obj)
        if revenue > 0:
            summ += revenue
            count_profit_firm += 1
    average = summ / count_profit_firm
result_list = [result, {"average_profit": average}]

with open(new_file, 'w', encoding='utf=8') as f:
    json.dump(result_list, f, ensure_ascii=False)







