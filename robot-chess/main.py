import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('1280x1024')
root.title('chess')

s = ttk.Style()
s.configure('black.TLabel', background = '#000000', foreground = '#ffffff', padding = (45, 30))
s.configure('white.TLabel', background = '#ffffff', foreground = '#000000', padding = (45, 30))
s.configure('robot.TLabel', background = 'green', foreground = '#000000', padding = (10, 10))

def up(event):
    position = robot.grid_info()
    if  0 < position['row']:
        print('Move up!')
        robot.grid(row = position['row'] - 1)
        robot_row = robot.grid_info()['row']
        robot_col = robot.grid_info()['column']
        tile_color = array[robot_row][robot_col]
        print(f"Robot is at ({robot_row}, {robot_col}) on a {tile_color} tile")

def right(event):
    position = robot.grid_info()
    if position['column'] < 7:
        print('Move right!')
        robot.grid(column = position['column']  + 1)
        robot_row = robot.grid_info()['row']
        robot_col = robot.grid_info()['column']
        tile_color = array[robot_row][robot_col]
        print(f"Robot is at ({robot_row}, {robot_col}) on a {tile_color} tile")

def left(event):
    position = robot.grid_info()
    if 0 < position['column']:
        print('Move left!')
        robot.grid(column = position['column']  - 1)
        robot_row = robot.grid_info()['row']
        robot_col = robot.grid_info()['column']
        tile_color = array[robot_row][robot_col]
        print(f"Robot is at ({robot_row}, {robot_col}) on a {tile_color} tile")

def down(event):
    position = robot.grid_info()
    if position['row'] < 7:
        print('Move down!')
        robot.grid(row = position['row'] + 1)
        robot_row = robot.grid_info()['row']
        robot_col = robot.grid_info()['column']
        tile_color = array[robot_row][robot_col]
        print(f"Robot is at ({robot_row}, {robot_col}) on a {tile_color} tile")

count = True
array = []

for i in range(8):
    column = []
    for j in range(8):
        white = ttk.Label(root, style = 'white.TLabel')
        black = ttk.Label(root, style = 'black.TLabel')
        
        if count:
            white.grid(row = i, column = j)
            #print(white.grid_info())
            column.append('white')
            count = False
        else:
            black.grid(row = i, column = j)
            #print(black.grid_info())
            column.append('black')
            count = True
            
    array.append(column)
    count = not count
    
#print(array)

robot = ttk.Label(root, style = 'robot.TLabel')
robot.grid(row = 4, column = 4)

robot_row = robot.grid_info()['row']
robot_col = robot.grid_info()['column']
tile_color = array[robot_row][robot_col]
print(f"Robot is at ({robot_row}, {robot_col}) on a {tile_color} tile")

robot.bind('<KeyPress-Left>', left)
robot.bind('<KeyPress-Down>', down)
robot.bind('<KeyPress-Up>', up)
robot.bind('<KeyPress-Right>', right)

robot.focus()

root.mainloop()