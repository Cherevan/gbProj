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

# labels_list = []
# image_list_iterator = iter(image_list)
# for row in range(FIELD_SIZE):
#     _buf = []
#     for column in range(FIELD_SIZE):
#         label = tkinter.Label(main_window, image=next(image_list_iterator))
#         label.row = row
#         label.column = column
#         label.grid(row=row, column=column)
#         _buf.append(label)
#
#     labels_list.append(_buf)

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
# print(curr.row, curr.column)


def key_press(arg):
    print(arg.keysym)


main_window.bind('<KeyPress>', key_press)


main_window.mainloop()
