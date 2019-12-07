from tkinter import *
from funcs import *
# from pprint import pprint


class View(object):
    """docstring for View"""
    def __init__(self, world, scale):
        width = world.width
        height = world.height

        root = Tk()
        root.title("World")
        canvas = Canvas(root,
                        width=width * scale,
                        height=height * scale)
        canvas.pack()
        canvas.create_rectangle(0,
                                0,
                                width * scale,
                                height * scale,
                                fill="darkblue")

        for x in range(0, width):
            for y in range(0, height):
                if world.grid[y][x]:
                    canvas.create_rectangle(x * scale,
                                            y * scale,
                                            (x + 1) * scale,
                                            (y + 1) * scale,
                                            fill="green")

        root.mainloop()
