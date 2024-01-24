# Создаем калькулятор

import tkinter as tk
from tkinter import messagebox


def press_key(event):
    print(repr(event))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r':
        calculate_expression()


win = tk.Tk()
win.geometry('240x265+100+200')
win.resizable(False, False)
win['bg'] = '#A9A9A9'
win.title('Калькулятор')

win.bind('<Key>', press_key)
calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)
calc['state'] = tk.DISABLED


def add_digit(number):
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[-1] in '-+/*' and number == '0':
        number = ''
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, 'end')
    calc.insert('end', value + number)
    calc['state'] = tk.DISABLED


def clear_expression():
    calc['state'] = tk.NORMAL
    calc.delete(0, 'end')
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED


def add_operation(operation):
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value == '0' and operation in '/':
        operation = ''
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate_expression()
        value = calc.get()
    calc.delete(0, 'end')
    calc.insert('end', value + operation)
    calc['state'] = tk.DISABLED



def calculate_expression():
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value:
        if value[-1] in '+-/*':
            value = f'{value}{value[:-1]}'
        # result = str(eval(value))
        calc.delete(0, 'end')
        try:
            calc.insert('end', str(eval(value)))
        except (NameError, SyntaxError):
            messagebox.showinfo('Внимание, буквы в расчетах.')
            calc.insert(0, '0')
    calc['state'] = tk.DISABLED


def make_button_calc(digit):
    return tk.Button(win, text=digit, font=('Arial', 14),
                     bd=5, command=lambda: add_digit(str(digit)), relief=tk.RAISED)


def make_operation_button_calc(operation):
    return tk.Button(win, text=operation, font=('Arial', 14), fg='blue',
                     bd=5, command=lambda: add_operation(operation), relief=tk.RAISED)


def make_button_clear():
    return tk.Button(win, text='C', font=('Arial', 14), fg='black',
                     bd=5, command=lambda: clear_expression(), relief=tk.RAISED)


def make_button_equal():
    return tk.Button(win, text='res', font=('Arial', 14), fg='black',
                     bd=5, command=lambda: calculate_expression(), relief=tk.RAISED)


def grid_operation_calc():
    expressions = ['+', "-", "/", '*']
    for i in range(4):
        (make_operation_button_calc(expressions[i])
         .grid(row=i + 1, column=3, stick='we', padx=5, pady=5))


def grid_button_calc():
    number = 1
    for i in range(1, 4):
        for j in range(3):
            button = make_button_calc(str(number))
            button.grid(row=i, column=j, stick='we', padx=5, pady=5)
            number += 1
    make_button_calc(0).grid(row=4, column=0, stick='we', padx=5, pady=5)
    make_button_clear().grid(row=4, column=1, stick='we', padx=5, pady=5)
    make_button_equal().grid(row=4, column=2, stick='we', padx=5, pady=5)


def grid_columnconfigure_calc():
    win.grid_columnconfigure(0, minsize=60, )
    win.grid_columnconfigure(1, minsize=60, )
    win.grid_columnconfigure(2, minsize=60, )
    win.grid_columnconfigure(3, minsize=60, )
    win.grid_rowconfigure(1, minsize=60, )
    win.grid_rowconfigure(2, minsize=60, )
    win.grid_rowconfigure(3, minsize=60, )
    win.grid_rowconfigure(4, minsize=60, )


def main():
    grid_button_calc()
    grid_columnconfigure_calc()
    grid_operation_calc()

    win.mainloop()


main()
