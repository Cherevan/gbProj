var_gamer_word = tkinter.StringVar()

main_window.geometry(f'{G_WIDTH}x{G_HEIGHT}+{400}+{300}')

var_used_letters.set("уже пробовали: {}".format(' '.join(used_letters)))

label_1 = tkinter.Label(main_window, textvariable=var_gamer_word)
label_1.config(font=("Courier", 16))
label_1.place(x=0, y=0)


def key_press(arg):
    global mistakes_left
    letter = arg.char.lower()


main_window.bind('<KeyPress>', key_press)


