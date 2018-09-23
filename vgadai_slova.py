import random
import sys

words_list = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека', 'шайба', 'олимпиада']
secret_word = random.sample(words_list, 1)[0]
users_word = ['*'] * len(secret_word)
error_counter = 0
MAX_ERRORS = 3


def show_word(arg):
    print('Загадане слово:')
    print(''.join(arg))


def restart(arg):
    answer = input('Бажаєте зіграти ще раз? (y/n)').lower()
    if answer == 'y':
        secret = random.sample(arg, 1)[0]
        new_word = ['*'] * len(secret)
        show_word(new_word)
        return secret, new_word, 0
    else:
        print('Гру завершено.')
        sys.exit()


show_word(users_word)

while True:
    letter = input('Введіть букву: ').lower()
    if len(letter) != 1 or ord(letter) < 1072:
        continue

    if letter in secret_word:
        for num, item in enumerate(secret_word):
            if letter == item:
                users_word[num] = letter
        show_word(users_word)

        if '*' not in users_word:
            print('ПЕРЕМОГА!!!')
            secret_word, users_word, error_counter = restart(words_list)

    else:
        error_counter += 1
        print(f'Введена вами буква відсутня. Ви зробили {error_counter}/{MAX_ERRORS} помилок.')
        if error_counter == MAX_ERRORS:
            print('Ви програли :(')
            print(f'Було загадане слово {secret_word}.')
            secret_word, users_word, error_counter = restart(words_list)
