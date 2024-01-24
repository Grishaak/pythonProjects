import tkinter as tk
from random import shuffle


class MyButton(tk.Button):

    def __init__(self, master, x, y, number, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Arial 13', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False

    def __repr__(self):
        return f'MyButton {self.x}, {self.y} {self.number} {self.is_mine}'


class MineSweeper:
    ROW = 6
    COLUMNS = 5
    MINES = 10
    win = tk.Tk()

    def __init__(self):
        self.buttons = []
        count = 1
        for i in range(MineSweeper.ROW):
            sublist = []
            for j in range(MineSweeper.COLUMNS):
                btn = MyButton(MineSweeper.win, x=i, y=j, number=count)
                btn.config(command=lambda button=btn: self.click(button))
                sublist.append(btn)
                count += 1
            self.buttons.append(sublist)

    @staticmethod
    def click(clicked: MyButton):
        print(clicked)
        if clicked.is_mine:
            clicked.config(text='*', bg='red', disabledforeground='black')
        else:
            clicked.config(text=clicked.number)
        clicked.config(state="disabled")

    def create_buttons(self):
        for row in range(MineSweeper.ROW):
            for column in range(MineSweeper.COLUMNS):
                btn = self.buttons[row][column]
                btn.grid(row=row, column=column)

    def start_game(self):
        self.create_buttons()
        self.insert_mines()
        self.print_button()
        MineSweeper.win.mainloop()

    def print_button(self):
        for i in self.buttons:
            print(i)

    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        for i in self.buttons:
            for j in i:
                if j.number in index_mines:
                    j.is_mine = True

    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.ROW * MineSweeper.COLUMNS + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]


game = MineSweeper()
game.start_game()
