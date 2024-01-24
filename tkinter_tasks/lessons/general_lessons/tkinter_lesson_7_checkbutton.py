import tkinter as tk


def select_all():
    for check in [check_age, commercial, wanna_eat]:
        check.select()


def deselect_all():
    for check in [check_age, commercial, wanna_eat]:
        check.deselect()


def toggle_all():
    for check in [check_age, commercial, wanna_eat]:
        check.toggle()


def show():
    print('Флажок 18: ', check_age_value.get())
    print('реклама : ', commerial_value.get())


win = tk.Tk()
check_age_value = tk.StringVar()
commerial_value = tk.IntVar()
check_age_value.set('No')

win.title('Шестой урок')
win.geometry('300x400+100+200')

check_age = tk.Checkbutton(win, text="Вам уже есть 18 лет?",
                           variable=check_age_value,
                           offvalue='No',
                           onvalue='Yes')

commercial = tk.Checkbutton(win, text="Хотите ли видет рекламу?",
                            variable=commerial_value,
                            offvalue=0,
                            onvalue=1
                            )
wanna_eat = tk.Checkbutton(win, text="Будете кушац?", indicatoron=1)
check_age.pack()
commercial.pack()
wanna_eat.pack()
tk.Button(win, text='select_all', command=select_all).pack()
tk.Button(win, text='deselect_all', command=deselect_all).pack()
tk.Button(win, text='toggle_all', command=toggle_all).pack()
tk.Button(win, text='show', command=show).pack()

win.mainloop()
