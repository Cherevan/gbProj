salary = [
    ['Иванов Е.С.', 7461.58, 8487.61, 8143.43, 7896.41, 5921.96, 7295.52],
    ['Андреев И.В.', 6548.97, 7951.47, 7259.54, 8053.5, 7891.67, 7317.24],
    ['Петров А.И.', 5258.5, 6124.87, 3528.97, 5957.54, 4978.54, 6157.41],
]

# print(salary[0][1])
# print(salary)

# for item in salary:
#     print(item)

salary_zip = list(zip(*salary))
workers = salary_zip.pop(0)

print(workers)
# print(salary_zip)

for item in salary_zip:
    # print(item)
    print(sum(item) / len(item))
