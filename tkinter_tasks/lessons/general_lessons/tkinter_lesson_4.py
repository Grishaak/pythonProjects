import tkinter as tk

# Виджет grid для размещения кнопки в окне

win = tk.Tk()

win.geometry(f'400x500+100+200')
win.title('Четвертый урок.')

# button_1 = tk.Button(win, text='Button1')
# button_2 = tk.Button(win, text='Button2')
# button_3 = tk.Button(win, text='Button3')
# button_4 = tk.Button(win, text='Button4-new')
# button_5 = tk.Button(win, text='Button5')
# button_6 = tk.Button(win, text='Button6')
# button_7 = tk.Button(win, text='Button7')
# button_8 = tk.Button(win, text='Button8')
#
# # Рассмотрим метод распаковки grid - он позволяет
# # расположить кнопки в виде таблиц
# button_1.grid(row=0, column=0)
# button_2.grid(row=0, column=1, stick='we')
# button_3.grid(row=1, column=0)
# button_4.grid(row=1, column=1)
# button_5.grid(row=2, column=0)
# button_6.grid(row=2, column=1, stick='we')
# # columnspan - размещает кнопку по относительно колонок
# # stick - растягивает кнопку по сторонам указанным в параметре
# # необходим для корреляции расположения кнопки
# button_7.grid(row=3, column=0,columnspan=2, stick='we')
# button_8.grid(row=0, column=2,rowspan=4, stick='ns')
# # grid_columnconfigure - метод параметр для передачи
# # значений расположения кнопок в окне
# win.grid_columnconfigure(0, minsize=70)
# win.grid_columnconfigure(1, minsize=100)

# То же самое только через вложенные циклы
for row in range(5):
    for column in range(3):
        (tk.Button(win, text=f'Button[{row}][{column}]')
         .grid(row=row, column=column))


win.grid_columnconfigure(0, minsize=70)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=150)

win.mainloop()
