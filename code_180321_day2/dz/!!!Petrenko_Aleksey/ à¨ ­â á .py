salary = [
    ['Иванов Е.С.', 7461.58, 8487.61, 8143.43, 7896.41, 5921.96, 7295.52],
    ['Андреев И.В.', 6548.97, 7951.47, 7259.54, 8053.5, 7891.67, 7317.24],
    ['Петров А.И.', 5258.5, 6124.87, 3528.97, 5957.54, 4978.54, 6157.41],
]


class Man:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def _average_salary(self):
        return sum(self.salary) / len(self.salary)

    def __repr__(self):
        return f'Средняя зарплата сотрудника {self.name} равна {self._average_salary:.2f} руб.'


class Office:

    def __init__(self, salary_data):
        self.mans = []
        for line in salary_data:
            self.mans.append(Man(line[0], line[1:]))

    def print_average_salary(self):
        for man in self.mans:
            print(man)


office = Office(salary)
office.print_average_salary()
