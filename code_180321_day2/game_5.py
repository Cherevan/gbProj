import tkinter
import os

IMAGES_DIR = 'nums'
FIELD_SIZE = 4

main_window = tkinter.Tk()
main_window.title('игра 15')

files_list = sorted(os.listdir(IMAGES_DIR))

image_list = []
for file in files_list:
    file_rel_path = os.path.join(IMAGES_DIR, file)
    image = tkinter.PhotoImage(file=file_rel_path)
    image_list.append(image)

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
        print(curr, near)


# callback
# main_window.bind('<KeyPress>', key_press)
main_window.bind('<KeyPress>', lambda x: key_press(x.keysym))


main_window.mainloop()
