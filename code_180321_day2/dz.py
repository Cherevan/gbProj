f_name = 'salary.csv'
with open(f_name, 'r', encoding='utf-8') as file:
    file_data = file.readlines()

# print(file_data)


# def data_proceed(x):
#     return x.replace('\n', '').split(',')
#
#
# file_list = tuple(map(data_proceed, file_data))

file_list = tuple(map(lambda x: x.replace('\n', '').split(','), file_data))

# print(file_list)

for data in file_list:
    worker = data.pop(0)
    summa = sum(map(float, data))
    # summa = sum(map(lambda arg: float(arg), data))

    print(f'{worker}: {summa / len(data):.2f} руб')
