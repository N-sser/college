import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('1280x1024')
root.title('chess')

s = ttk.Style()
s.configure('black.TLabel', background = '#000000', foreground = '#ffffff', padding = (45, 30))
s.configure('white.TLabel', background = '#ffffff', foreground = '#000000', padding = (45, 30))
s.configure('robot.TLabel', background = 'green', foreground = '#000000', padding = (10, 10))
s.configure('indicator.TLabel', background = 'blue', foreground = '#000000', padding = (100, 50))

class Square:
    def __init__(self, parent_window, style, row, column):
        self.window= parent_window
        self.style: str = style
        self.row: int = row
        self.col: int = column

        # Creating and placing the class of the widget
        self.widget = ttk.Label(self.window, style = self.style)
        self.widget.grid(row = self.row, column = self.col)

class Board:
    def __init__(self, rows, cols):
        self.board_rows: int = rows
        self.board_columns: int = cols
        self.squares= []

    def generate(self):
        count = True

        for i in range(self.board_rows):
            column_of_squares = []
            for j in range(self.board_columns):
                if count:
                    white_square = Square(root, 'white.TLabel', i, j)
                    column_of_squares.append(white_square)
                    count = False
                else:
                    black_square = Square(root, 'black.TLabel', i, j)
                    column_of_squares.append(black_square)
                    count = True

            self.squares.append(column_of_squares)
            count = not count
    
class Robot:
    def __init__(self, parent_window, style, row = 0, column = 0):
        self.window = parent_window
        self.style: str = style
        self.row: int = row
        self.col: int = column
        
        # Creating it and placing the robot
        self.widget = ttk.Label(self.window, style = self.style)
        self.widget.grid(row = self.row, column = self.col)
        
    def get_square_position(self):
        return board.squares[self.row][self.col]

    def get_color(self):
        return 'white' if self.get_square_position().style == 'white.TLabel' else 'black' 

    def left(self, event):
        if  0 < self.col:
            self.col -= 1
            self.widget.grid(column = self.col)
            info.update_text()
            #print(self.get_color())

    def down(self, event):
        if self.row < board.board_rows - 1:
            self.row += 1
            self.widget.grid(row = self.row)
            info.update_text()
    
    def up(self, event):
        if 0 < self.row:
            self.row -= 1
            self.widget.grid(row = self.row)
            info.update_text()

    def right(self, event):
        if  self.col < board.board_columns - 1:
            self.col += 1
            self.widget.grid(column= self.col)
            info.update_text()

class Indicator:
    def __init__(self, parent_window, style):
        self.window = parent_window
        self.style = style
        self.side = 'bottom'
        self.expand = True
        
        self.widget = ttk.Label(self.window, style= self.style)
        self.widget.grid(column = board.board_columns + 1, row = board.board_rows)   
        #self.widget.pack(side = self.side, expand = self.expand)   
    
    def update_text(self):
        self.widget.configure(text = f'{alexa.get_color()}')


board = Board(8,8)
board.generate()

alexa = Robot(root, 'robot.TLabel')

info = Indicator(root, 'indicator.TLabel')

root.bind('<KeyPress-s>', alexa.down)
root.bind('<KeyPress-a>', alexa.left)
root.bind('<KeyPress-w>', alexa.up)
root.bind('<KeyPress-d>', alexa.right)

root.mainloop()