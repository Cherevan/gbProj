# Проверка на победу в игре происходит
# в коде функции key_press
import tkinter
import os
import random
from tkinter import messagebox

IMAGES_DIR = 'nums'
FIELD_SIZE = 4
image_list = []
label_list = []
file_list = sorted(os.listdir(IMAGES_DIR))

main_window = tkinter.Tk()
main_window.title('Гра 15')

for file in file_list:
    path_file = os.path.join(IMAGES_DIR, file)
    image = tkinter.PhotoImage(file=path_file)
    image_list.append(image)

for row in range(FIELD_SIZE):
    _tmp = []
    for col in range(FIELD_SIZE):
        x = row * FIELD_SIZE + col
        label = tkinter.Label(main_window, image=image_list[x])
        label.x = x
        label.row = row
        label.col = col
        label.grid(row=row, column=col)
        _tmp.append(label)

    label_list.append(_tmp)

cursor = label_list[-1][-1]


def exchange_lbl(arg):
    arg.row , cursor.row = cursor.row, arg.row
    arg.col, cursor.col = cursor.col, arg.col
    label_list[arg.row][arg.col], label_list[cursor.row][cursor.col] = \
        label_list[cursor.row][cursor.col], label_list[arg.row][arg.col]


def render_item(arg):
    arg.grid(row=arg.row, column=arg.col)


def key_press(arg, win_flag=0):
    near = None
    score = 0

    if arg == 'Up' and cursor.row > 0:
        near = label_list[cursor.row - 1][cursor.col]
    elif arg == 'Down' and cursor.row < (FIELD_SIZE - 1):
        near = label_list[cursor.row + 1][cursor.col]
    elif arg == 'Left' and cursor.col > 0:
        near = label_list[cursor.row][cursor.col - 1]
    elif arg == 'Right' and cursor.col < (FIELD_SIZE - 1):
        near = label_list[cursor.row][cursor.col + 1]

    if near:
        exchange_lbl(near)
        render_item(near)
        render_item(cursor)

    # ПРОВЕРКА НА ПОБЕДУ
    for row in range(FIELD_SIZE):
        for col in range(FIELD_SIZE):
            position = row * FIELD_SIZE + col
            if position == label_list[row][col].x:
                score += 1

    if score > 15 and win_flag != 1:
        tkinter.messagebox.showinfo('You are winner!', 'Congratulation! You win in this great game!')
        _answer = tkinter.messagebox.askquestion('Ask', 'Do you wont restart this game?')
        if _answer == 'yes':
            shuffle_game()
        else:
            exit()


def shuffle_game():
    action = ('Up', 'Down', 'Left', 'Right')
    for _ in range(5):
        rand_action = random.sample(action, 1)[0]
        key_press(rand_action, 1)


main_window.bind('<KeyPress>', lambda evnt: key_press(evnt.keysym))

main_window.after(1500, shuffle_game)

main_window.mainloop()