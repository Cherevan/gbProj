salary = [
    ['Иванов Е.С.', 7461.58, 8487.61, 8143.43, 7896.41, 5921.96, 7295.52],
    ['Андреев И.В.', 6548.97, 7951.47, 7259.54, 8053.5, 7891.67, 7317.24],
    ['Петров А.И.', 5258.5, 6124.87, 3528.97, 5957.54, 4978.54, 6157.41],
]

salary_zip = list(zip(*salary))

# print(salary)
# print(*salary)

workers = salary_zip.pop(0)
#
# print(workers)
#
for item in salary_zip:
    avg_salary = sum(item) / len(item)
    # print(f'зарплата: {avg_salary:.2f} руб')
    print('зарплата: {:.2f} руб'.format(avg_salary))

# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# c = [100, 200, 300, 400]
# d = [1000, 2000, 3000, 4000]
#
# args = [a, b, c, d]
#
# # result = tuple(zip(a, b, c))
# # print(result)
#
# result = tuple(zip(*args))
# print(result)
#
# # **kwargs
