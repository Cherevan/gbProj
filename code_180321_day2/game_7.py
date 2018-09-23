import tkinter
import os
import random
from PIL import Image, ImageTk
from tkinter import messagebox

IMAGES_DIR = 'nums'
FIELD_SIZE = 4

main_window = tkinter.Tk()
main_window.title('игра 15')

# files_list = sorted(os.listdir(IMAGES_DIR))
#
# image_list = []
# for file in files_list:
#     file_rel_path = os.path.join(IMAGES_DIR, file)
#     image = tkinter.PhotoImage(file=file_rel_path)
#     image_list.append(image)


def make_mosaik(filename='test.jpg'):
    image = Image.open(filename)
    regions = []
    pixels = image.width // FIELD_SIZE
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            x1 = j * pixels
            y1 = i * pixels
            x2 = j * pixels + pixels
            y2 = i * pixels + pixels
            box = (x1, y1, x2, y2)
            region = image.crop(box)
            region.load()
            regions.append(ImageTk.PhotoImage(region))

    return regions

# while True:
#     pass

image_list = make_mosaik()

labels_list = []
# внешний цикл по строкам
for row in range(FIELD_SIZE):
    _buf = []
    # внутренний цикл по колонокам
    for column in range(FIELD_SIZE):
        x = row * FIELD_SIZE + column
        label = tkinter.Label(main_window, image=image_list[x])
        label.x = x
        label.row = row
        label.column = column
        label.grid(row=row, column=column)
        _buf.append(label)

    labels_list.append(_buf)

curr = labels_list[-1][-1]


def exchange_items(arg):
    arg.row, curr.row = curr.row, arg.row
    arg.column, curr.column = curr.column, arg.column
    labels_list[arg.row][arg.column], labels_list[curr.row][curr.column] = \
        labels_list[curr.row][curr.column], labels_list[arg.row][arg.column]


def render_item(arg):
    arg.grid(row=arg.row, column=arg.column)


def key_press(arg):
    # print(arg)
    near = None

    if arg == 'Up' and curr.row > 0:
        near = labels_list[curr.row - 1][curr.column]
    elif arg == 'Down' and curr.row < FIELD_SIZE - 1:
        near = labels_list[curr.row + 1][curr.column]
    elif arg == 'Left' and curr.column > 0:
        near = labels_list[curr.row][curr.column - 1]
    elif arg == 'Right' and curr.column < FIELD_SIZE - 1:
        near = labels_list[curr.row][curr.column + 1]

    if near:
        exchange_items(near)
        render_item(near)
        render_item(curr)
        # print(curr, near)


# callback
# main_window.bind('<KeyPress>', key_press)
main_window.bind('<KeyPress>', lambda x: key_press(x.keysym))


def shuffle_game():
    actions = ['Up', 'Down', 'Left', 'Right']
    for _ in range(100):
        current_action = random.sample(actions, 1)[0]
        key_press(current_action)
        # print(current_action)


# shuffle_game()
main_window.after(2000, shuffle_game)

main_window.mainloop()