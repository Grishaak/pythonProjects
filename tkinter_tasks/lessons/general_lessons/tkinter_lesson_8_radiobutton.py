import tkinter as tk

win = tk.Tk()
win.geometry('240x265+100+200')
win.title('Радиокнопка')

levels = {
    1: 'Easy',
    2: 'Middle',
    3: 'Hard'
}
races = {
    1: 'Эльфы',
    2: 'Люди',
    3: 'Орки'
}


def select_level():
    level = level_var.get()
    s = f'Вы выбрали {level} уровень' if level else ""
    level_text.set(s)
    print(levels[level])


def select_race():
    race = races.get(race_var.get())
    s = f'Вы играете за {race}' if race else ''
    race_text.set(s)
    print(race)


level_var = tk.IntVar()
level_text = tk.StringVar()

race_var = tk.IntVar()
race_text = tk.StringVar()

tk.Label(win, text='Выберите уровень сложности').pack()

for key, level in sorted(levels.items()):
    tk.Radiobutton(win, text=level, variable=level_var, value=key,
                   command=select_level).pack()
tk.Label(win, textvariable=level_text).pack()
#
for key, level in sorted(races.items()):
    tk.Radiobutton(win, text=level, variable=race_var, value=key,
                   command=select_race).pack()

tk.Label(win, textvariable=race_text).pack()
win.mainloop()
