import tkinter as tk

win = tk.Tk()
win.geometry('400x500+100+200')
win.title('Третий урок')

# Создаем функции для параметров кнопок command.
# Где при нажатии на кнопку будет выполняться код.
def say_hi():
    print('Greetings, traveler!')


def add_label():
    label = tk.Label(win, text='new')
    label.pack()


count = 0


def counter():
    global count
    count += 1
    button_4['text'] = f'Счетчик: {count}'


def say_hi_active_background():
    return 'brown'


count_smth = 0


def disable_all_buttons():
    global count_smth
    if count_smth % 2 == 0:
        button_2['state'] = tk.DISABLED
        button_3['state'] = tk.DISABLED
        button_4['state'] = tk.DISABLED
        count_smth += 1
    else:
        button_2['state'] = tk.NORMAL
        button_3['state'] = tk.NORMAL
        button_4['state'] = tk.NORMAL
        count_smth += 1


# Как создаются кнопки.
button_1 = tk.Button(win, text='Hi!!!!',
                     command=disable_all_buttons)
button_2 = tk.Button(win, text='Add label!!!!',
                     command=add_label)
button_3 = tk.Button(win, text='Add new lambda',
                     command=lambda: tk.Label(win, text='new lambda').pack())
button_4 = tk.Button(win, text=f'Счетчик: {count}',
                     command=counter,
                     activebackground=say_hi_active_background(),
                     state=tk.DISABLED,
                     bg='red')

# Упаковываем кнопки чтобы mainloop их увидел.
button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()
win.mainloop()
