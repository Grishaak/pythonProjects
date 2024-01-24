# Виджеты параметров кнопок

import tkinter as tk

win = tk.Tk()
win.geometry('300x400+100+200')
win.title('Второй урок')

# Виджет для создания текста в окне
# Все переменные отвечают за параметры текста
label_1 = tk.Label(win, text='''Здарова\nКАК ОНО?!''',
                   bg='red', # Бекграунд
                   fg='white', # цвет символов
                   font=('Arial', 20, 'bold'),
                   padx=10,
                   pady=20,
                   width=10,
                   height=2,
                   anchor="nw", # anchor - сторона света для текста
                   # в виде символов
                   relief=tk.RAISED, bd=10, # Обтекание для фона текста
                   justify=tk.RIGHT # Прижимает текст к определенной точке
                   )
label_1.pack()

win.mainloop()
