sallary = [
    ['Stepan Haritonenko', 5762.52, 5789.54, 6598.54, 5461.32, 5487.54, 7982.95],
    ['Eugen Kochubei', 5432.54, 8453.24, 6547.54, 5475.45, 6583.54, 7451.12],
    ['Vasyl Postrybailo', 4572.54, 7854.12, 3687.47, 6542.98, 9451.00, 7243.87]
]

month = ('Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень')
sallary_zip = list(zip(*sallary))
workers = sallary_zip.pop(0)

for i in sallary:
    print(i)

print('Транспонація списку:')

for i in sallary_zip:
    print(i)

print('\nСередня зарплата за місяць:')

# for i in range(len(sallary_zip)):
#     avg_salary = sum(sallary_zip[i]) / len(workers)
#     print(f'За {month[i]}: {avg_salary:.2f} грн.')

for num, i in enumerate(sallary_zip):
    avg_salary2 = sum(i) / len(i)
    print(num , i)
    print(f'За {month[num]:8}: {avg_salary2:.2f} грн.')
