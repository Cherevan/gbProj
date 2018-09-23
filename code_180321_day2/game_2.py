import tkinter
import os

main_window = tkinter.Tk()
main_window.title('игра 15')

# files_list = sorted(os.listdir('nums'), reverse=True)
files_list = os.listdir('nums')
files_list.sort()
# print(help(list))
# arg (args)
# kwarg (kwargs) -> keyword arg
# print(files_list)

image_list = []
for file in files_list:
    # file_rel_path = 'nums/' + file
    # file_rel_path = f'nums/{file}'
    file_rel_path = os.path.join('nums', file)
    image = tkinter.PhotoImage(file=file_rel_path)
    image_list.append(image)


labels_list = []
for image in image_list:
    label = tkinter.Label(main_window, image=image)
    label.grid()
    labels_list.append(label)

curr = labels_list[-1]

print(labels_list)
# print(labels_list[len(labels_list) - 1])
print(curr)



main_window.mainloop()
