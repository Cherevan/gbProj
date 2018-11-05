from itertools import combinations

# number = [2, 3, 4, 5, 6, 7, 8, 9]      Приклад таблиці множення брут форсом
# for combination in combinations_with_replacement(number, 2):
#     print('{} x {} = {}'.format(combination[0], combination[1], combination[0] * combination[1]))

VOLUME = 7

items = (
    ('светр', 3, 50),
    ('сірники', 0.1, 80),
    ('ніж', 0.2, 60),
    ('футболка', 1, 30),
    ('шкарпетки', 0.5, 40),
    ('ліхтарик', 0.3, 35),
    ('консерва1', 0.4, 40),
    ('консерва2', 0.7, 60),
    ('джинси', 2.8, 20),
    ('книжка', 2.2, 15),
    ('компас', 0.25, 45),
    ('дощовик', 2.9, 40),
    ('сухофрукти', 0.9, 60),
    ('печиво', 0.8, 40),
)


def calcBackPackVol(backpack):
    total = 0
    for item in backpack:
        total += item[1]
    return total


def calcBackPackCost(backpack):
    total = 0
    for item in backpack:
        total += item[2]
    return total


# total_volume = 0   Варіант № 1
# for item in items:
#     total_volume += item[1]
total_volume = sum(list(zip(*items))[1])  # Варіант № 2

print(f'У нас в розпорядженні {len(items)} предметів, об\'ємом {total_volume} л. \
Їх необхідно впакувати у рюкзак {VOLUME} л.')

max_cost = 0
counter = 0
result_cost = []
result_items = []

for num in range(1, len(items) + 1):
    for i, combination in enumerate(combinations(items, num), 1):
        curent_volume = calcBackPackVol(combination)
        curent_cost = calcBackPackCost(combination)
        if curent_volume <= VOLUME and curent_cost >= max_cost:
            counter += 1
            max_cost = curent_cost
            result_items.append(combination)
            result_cost.append(curent_cost)
            print(f'Комбінація №{counter}, ціною {curent_cost} і об\'ємом {curent_volume:.2f} л.: {combination}')

count_result_cost = result_cost.count(max_cost)

print(f'Нам вдалось {count_result_cost} раз знайти найбільшу цінність {max_cost}.')

best_result = result_items[result_cost.index(max_cost)]

print(best_result)
print('Досягнуто об\'єм', calcBackPackVol(best_result), 'літрів.')
