import random


# Створення списку всіх відомих відповідей
def get_all_answers():
    ans = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        # Варіант 1 - Множества
        if len(set(map(int, tmp))) == 4:
            ans.append(list(map(int, tmp)))

        # Варіант 2 - Генератор списку
        # lst = ['x' for num in tmp if tmp.count(num) == 1]
        # if len(lst) == 4:
        #     ans.append(list(map(int, tmp)))
    return ans


# Обирає одну можливу відповідь зі списку
def get_one_answer(ans):
    num = random.choice(ans)
    return num


# запит на ввід 4 цифр, що не повторюються
def input_number():
    while True:
        nums = input('Введіть число з 4 унікальних цифр: ')
        if len(nums) != 4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums


# порівнююємо числа і повідомляємо скільки биків та корів
def check(nums, true_num):
    bulls, cows = 0, 0
    for i, item in enumerate(nums):
        if item in true_num:
            if nums[i] == true_num[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


# видалення хибних відповідей
def del_bad_answers(ans, enemy_try, bulls, cows):
    for item in ans[:]:
        temp_bulls, temp_cows = check(item, enemy_try)
        if temp_bulls != bulls or temp_cows != cows:
            ans.remove(item)
    return ans


if __name__ == '__main__':
    print('*** Гра Бики та корови ***')
    answer = get_all_answers()
    enemy = get_one_answer(answer)
    player = input_number()

    while True:
        print('=' * 10, 'Хід гравця', '=' * 10)
        print('Вгадайте загадане число комп\'ютера')
        number = input_number()
        bulls, cows = check(number, enemy)
        print(f'Вгадано Биків: {bulls}, Корів: {cows}')

        if bulls == 4:
            print('*' * 10, 'Ви перемогли!', '*' * 10)
            print('Комп\'ютор загадав число:', enemy)
            break

        print('=' * 10, 'Хід ПК', '=' * 10)
        enemy_try = get_one_answer(answer)
        print('Комп\'ютер вважає, що ви загадали:', enemy_try)
        bulls, cows = check(enemy_try, player)
        print(f'Вгадано Биків: {bulls}, Корів: {cows}')

        if bulls == 4:
            print('*' * 10, 'Переміг штучний інтелект.', '*' * 10)
            print('Комп\'ютор загадав число:', enemy)
            break
        else:
            answer = del_bad_answers(answer, enemy_try, bulls, cows)
