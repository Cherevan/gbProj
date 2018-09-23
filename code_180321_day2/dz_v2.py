f_name = 'salary.csv'

with open(f_name, 'r', encoding='utf-8') as file:
    file_data = file.readlines()

file_list = []
for line in file_data:
    file_list.append(line.replace('\n', '').split(','))

# print(file_list)
# salary = [
#     ['Петров А.И.', '5258.5', '6124.87', '3528.97', '5957.54', '4978.54', '6157.41'],
#     ['Иванов Е.С.', '7461.58', '8487.61', '8143.43', '7896.41', '5921.96', '7295.52'],
#     ['Андреев И.В.', '6548.97', '7951.47', '7259.54', '8053.5', '7891.67', '7317.24']
# ]

# file_list = tuple(map(lambda x: x.split(','), file_data))

# def do_something(arg):
#     # do something else
#     return float(arg)


for data in file_list:
    # worker = data.pop(0)
    # avg_summa = sum(map(float, data)) / len(data)
    # print(f'{worker}: {avg_summa:.2f} руб')
    print(f'{data.pop(0)}: {sum(map(float, data)) / len(data):.2f} руб')
