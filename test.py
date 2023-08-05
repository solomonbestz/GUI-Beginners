from tkinter import *
from tkinter.ttk import *
import customtkinter as c


class Board(Canvas):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        color1 = ['red', 'black',]
        self.cells_list = []

        for row in range(7):
            for col in range(7):
                self.cell = c.CTkFrame(self, fg_color=color1[1], width=75, height=50, corner_radius=0)
                self.cell.grid(row = row, column=col)
                self.cells_list.append(self.cell)
                color1[1], color1[0] = color1[0], color1[1]

class App(c.CTk):
    def __init__(self):
        super().__init__()
        self.canvas = Board(self, height=400, width=600)
        self.canvas.grid()
        self.canvas.bind("<B1-Motion>", self.move)

        print(self.canvas.cells_list)

        self.label = c.CTkLabel(self)
        self.label.grid(row = 0, column = 0)

    def move(self, e):
        #event.x
        #event.y
        self.label.configure(text=f"Coordinates: X: {e.x_root} Y: {e.y}")
        


    
if __name__=='__main__':
    app = App()
    app.mainloop()
