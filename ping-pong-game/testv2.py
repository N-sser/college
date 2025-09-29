import tkinter as tk
from abc import ABC, abstractmethod

root = tk.Tk()
root.title('PingPongUltimate')
root.resizable(False, False)   
window_width = 1600
window_height = 1200

# Get the screen dimensions to find the "center" point of the window
center_x = int(root.winfo_screenwidth() / 2 - window_width / 2)
center_y = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

game_canvas = tk.Canvas(root,
    width = window_width, 
    height = window_height, 
    bg = "#1d2021",
    highlightthickness = 0
    )
game_canvas.pack()

class GameObject(ABC):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.canvas_id = None

    @abstractmethod
    def render(self, canvas):
        pass

    @abstractmethod
    def update_position(self, canvas):
        print("What this does?")
        pass

class Ball(GameObject):
    def __init__(self, x, y, radius, color, dx=5, dy=5):
        super().__init__(x, y, radius*2, radius*2, color)

        self.dx = dx
        self.dy = dy

    def render(self, canvas):
        self.canvas_id = canvas.create_oval(
            self.x, self.y,
            self.x + self.width, self.y + self.height,
            fill = self.color)

    def bounce_vertical(self):
        self.dy *= -1

    def bounce_horizontal(self, speed_increase=1.05):
        self.dx *= -speed_increase

    def update_position(self, canvas):
        self.x += self.dx
        self.y += self.dy
        canvas.coords(self.canvas_id, 
            self.x, self.y,
            self.x + self.width, self.y + self.height)

class Racket(GameObject):
    def __init__(self, x, y, width, height, color, dy=15):
        super().__init__(x, y, width, height, color)

        self.dy: float = dy

    def render(self, canvas):
        self.canvas_id = canvas.create_rectangle(
            self.x, self.y,
            self.x + self.width, self.y + self.height,
            fill = self.color)

    def update_position(self, canvas):
        self.y += self.dy
        canvas.coords(self.canvas_id,
            self.x, self.y,
            self.x + self.width, self.y + self.height)

class Net(GameObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

    def render(self, canvas):
        self.canvas_id = canvas.create_line(
            self.x, self.y, 
            self.x, self.height, 
            fill = self.color,
            #dash = )
        )

    def update_position(self, canvas):
        return super().update_position(canvas)

ball = Ball(100, 100, 25, 'pink')
ball.render(game_canvas)

left_racket = Racket(400, 400 , 20 ,150, 'orange', 10)
left_racket.render(game_canvas)
left_racket.update_position(game_canvas)

net = Net(window_width / 2, 0, 100, window_height, 'white')
net.render(game_canvas)
net.update_position(game_canvas)

#for i in range(10):
#    ball.update_position(game_canvas)

def game_loop():
    ball.update_position(game_canvas)

    root.after(1000 // 60, game_loop)


root.mainloop()
