import bull_and_cow

answers = bull_and_cow.get_all_answers()
count = 0

while len(answers) > 1:
    count += 1
    print('Хід №', count)
    print('Можливих варіантів розв\'язку', len(answers))
    ans = bull_and_cow.get_one_answer(answers)
    print('Пропонована комбінація: ', ans)
    bulls = int(input('Скільки виявилось биків? '))
    if bulls == 4:
        break
    cows = int(input('Скільки виявилось корів? '))
    answers = bull_and_cow.del_bad_answers(answers, ans, bulls, cows)

print('Всього', count, 'ходів.')
print('Відповідь: ', answers)