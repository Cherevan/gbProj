salary = [
    ['Иванов Е.С.', 7461.58, 8487.61, 8143.43, 7896.41, 5921.96, 7295.52],
    ['Андреев И.В.', 6548.97, 7951.47, 7259.54, 8053.5, 7891.67, 7317.24],
    ['Петров А.И.', 5258.5, 6124.87, 3528.97, 5957.54, 4978.54, 6157.41],
]

salary_zip = list(zip(*salary))
workers = salary_zip.pop(0)

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь']

for num, item in enumerate(salary_zip):
    avg_salary = sum(item) / len(item)
    print(f'зарплата за {months[num]:8}: {avg_salary:.2f} руб')
