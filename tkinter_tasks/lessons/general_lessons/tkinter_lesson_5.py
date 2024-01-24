import tkinter as tk

# Знакомство с Entry(ввод)

win = tk.Tk()

win.geometry(f'400x500+100+200')
win.title('Пятый урок.')

tk.Label(win, text='Имя:').grid(row=0, column=0, stick='w')
tk.Label(win, text='Пароль:').grid(row=1, column=0, stick='w')

name = tk.Entry(win)
password=tk.Entry(win, show='*')
name.grid(row=0, column=1)
password.grid(row=1, column=1)


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print("Empty entry")


def delete_entry():
    value = name.delete(first=0, last=tk.END)


def insert_entry():
    delete_entry()
    name.insert('end', 'text')

def submit_entry():
    print(name.get())
    print(password.get())
    delete_entry()
    password.delete(0, 'end')

button_entry = (tk.Button(win, text='get', command=get_entry)
                .grid(row=2, column=0, stick='we'))
button_entry2 = (tk.Button(win, text='delete', command=delete_entry)
                 .grid(row=2, column=1, stick='we'))
button_entry3 = (tk.Button(win, text='insert', command=insert_entry)
                 .grid(row=2, column=2, stick='we'))
button_entry3 = (tk.Button(win, text='submit', command=submit_entry)
                 .grid(row=3, column=0, stick='we'))

win.grid_columnconfigure(0, minsize=70)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
