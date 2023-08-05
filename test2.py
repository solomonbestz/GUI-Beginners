from tkinter import *


class Paint:
    def __init__(self, root):
        self.root = root

        self.current_x = None
        self.current_y = None

        self.brush_size = 10
        self.brush_color = "black"

    def create_widgets(self):
        # Creating the canvas
        self.canvas = Canvas(self.root, width=1000, height=1000)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Setting up bindings for the canvas.
        self.canvas.bind("<Button-1>", self.setup_coords)
        self.canvas.bind("<B1-Motion>", self.drag)

    def setup_coords(self, e):
        # Reset the starting points to the current mouse position
        self.current_x = e.x
        self.current_y = e.y

    def drag(self, e):
        # Create an oval that's size is the same as brush_size
        oval = self.canvas.create_oval(self.current_x, self.current_y, self.current_x+self.brush_size, self.current_y+self.brush_size, fill=self.brush_color)

        # Set the variables values to the current position of the mouse, so that the oval gets drawn correctly on the next call.
        self.current_x = e.x
        self.current_y = e.y


def main():
    root = Tk()
    root.geometry("1000x1000")
    p = Paint(root)
    p.create_widgets()
    mainloop()

if __name__ == '__main__':
    main()
