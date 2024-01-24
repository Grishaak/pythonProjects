import random
import tkinter as tk
from tkinter import ttk

colors = ('blue', 'red', 'green', 'purple', 'pink',
          'white', 'black')
ints = (12, 3, 4, 5, 6)


def show_color():
    print(combo_color.get())


def set_random_color():
    combo_color.set(random.choice(colors))


win = tk.Tk()
win.geometry('300x400+800+150')
win.title("Combobox")

combo_color = ttk.Combobox(win, values=colors)


combo_int = ttk.Combobox(win, values=ints)

button_show_color = ttk.Button(win, text='show_color',
                               command=show_color)
button_set_color = ttk.Button(win, text='set_random_color',
                              command=set_random_color)
combo_color.current(0)
combo_int.current(2)
button_show_color.pack()
button_set_color.pack()
# combo_int.pack()
combo_color.pack()

win.mainloop()
