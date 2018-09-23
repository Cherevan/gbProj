import random

MAX_ERRORS = 8

words_list = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека',
              'шайба', 'олимпиада']

secret_word = random.sample(words_list, 1)[0]
users_word = ['*'] * len(secret_word)
errors_counter = 0

# print(secret_word)


def show_users_word(arg):
    print(''.join(arg))


# show_users_word(users_word)

while True:
    letter = input('введите букву: ').lower()

    if len(letter) != 1 or not letter.isalpha():
        continue

    # print(ord(letter))
    if letter in secret_word:
        for position, char in enumerate(secret_word):
            if char == letter:
                users_word[position] = letter

        show_users_word(users_word)
        if '*' not in users_word:
            print(f'вы выиграли!!!')
            break
    else:
        errors_counter += 1
        print(f'буквы нет, ошибок: {errors_counter}')
        if errors_counter == MAX_ERRORS:
            print(f'игра завершена ;(')
            break


print('пока-пока')
