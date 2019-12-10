from tkinter import *
from funcs import *
# from pprint import pprint


class View(object):
    """ Class for tk window """
    def __init__(self, world, scale):
        width = world.width
        height = world.height
        self.width = width
        self.height = height

        root = Tk()
        root.title("World")
        map_canvas = Canvas(root,
                            width=width * scale,
                            height=height * scale)
        self.map_canvas = map_canvas
        map_canvas.pack(side="left")
        map_canvas.create_rectangle(0,
                                    0,
                                    width * scale,
                                    height * scale,
                                    fill="darkblue")

        for x in range(0, width):
            for y in range(0, height):
                if world.grid[y][x]:
                    try:
                        color = world.grid[y][x].color
                    except AttributeError:
                        color = "green"

                    tile = world.grid[y][x]
                    rect_id = map_canvas.create_rectangle(x * scale,
                                                          y * scale,
                                                          (x + 1) * scale,
                                                          (y + 1) * scale,
                                                          fill=color)
                    tile.id = rect_id
                    self.tileMouseBind(tile)

        # Initialize tooltip
        tooltip = Canvas(root,
                         width=300,
                         height=self.height * scale)
        tooltip.pack(side="right")
        self.tooltip = tooltip
        self.tooltip_text_id = tooltip.create_text(50, 50, anchor="nw")
        self.tooltip.itemconfig(self.tooltip_text_id, text="Placeholder")

        root.mainloop()

    def tileMouseBind(self, tile):
        self.map_canvas.tag_bind(tile.id, "<Enter>",
                                 lambda e, text=tile.getInfo():
                                 self.setTooltip(e, text))
        self.map_canvas.tag_bind(tile.id, "<Leave>",
                                 lambda e: self.setTooltip(e, ''))

    def setTooltip(self, event, text=""):
        self.tooltip.itemconfig(self.tooltip_text_id, text=text)
