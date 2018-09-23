import tkinter
import os

main_window = tkinter.Tk()
main_window.title('игра 15')

files_list = sorted(os.listdir('nums'))

image_list = []
for file in files_list:
    file_rel_path = os.path.join('nums', file)
    image = tkinter.PhotoImage(file=file_rel_path)
    image_list.append(image)

labels_list = []
for x, image in enumerate(image_list):
    row = x // 4
    column = x % 4
    label = tkinter.Label(main_window, image=image)
    label.x = x
    label.row = row
    label.column = column
    label.grid(row=row, column=column)
    labels_list.append(label)

curr = labels_list[-1]

print(curr.x, curr.row, curr.column)


main_window.mainloop()
