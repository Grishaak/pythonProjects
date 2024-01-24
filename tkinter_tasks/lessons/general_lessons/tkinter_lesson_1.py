# Здесь будет упражнения с GUI tkinter.
import tkinter as tk

# Создаем экземпляр класса tkinter
win = tk.Tk()

# Меняем название нашего окна
win.title('new_title')

# Задает параметры размера окна и его координат
# на экране. 500 - width, 600 - height,
# +10+ - отступ в пикселях слева и сверху
win.geometry('500x600+700+170')

# Метод изменения окна в ширину и в длину в
# интерактивном режиме
win.resizable(True, True)  # -->
# По умолчанию width:True, height:True

# Задает минимальные размеры окна по высоте и ширине
win.minsize(300, 400)  # --> минимальные размеры
win.maxsize(600, 700)  # --> максимальные размеры

# Задается цвет фона. bg - background
win.config(bg='#0F0D7D')

# Создает переменную для иконки и передает ее в наше окно.
dice = tk.PhotoImage(file='../../icons/dice.png')
win.iconphoto(False, dice)

# Создает постоянный поддержку окна через цикл.
win.mainloop()
