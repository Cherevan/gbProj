salary = [
    ['Stepan Haritonenko', 5762.52, 5789.54, 6598.54, 5461.32, 5487.54, 7982.95],
    ['Eugen Kochubei', 5432.54, 8453.24, 6547.54, 5475.45, 6583.54, 7451.12],
    ['Vasyl Postrybailo', 4572.54, 7854.12, 3687.47, 6542.98, 9451.00, 7243.87]
]

for num, i in enumerate(salary):
    avg_salary = sum(salary[num][1:]) / (len(salary[num]) - 1)
    print(f'Середня зарплата {salary[num][0]}: {avg_salary:.2f} грн.')

print('\n')

for i in salary:
    worker = i.pop(0)
    avg_salary2 = sum(i) / len(i)
    print(f'Середня зарплата {worker}: {avg_salary2:.2f} грн')