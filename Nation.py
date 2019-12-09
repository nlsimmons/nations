from Language import Language
from Leader import Leader
from funcs import *


class Nation():
    def __init__(self, world, color, capital):
        self.world = world
        self.color = color
        self.capital = capital
        self.settlements = [capital]

        self.language = Language()
        self.name = self.language.genName()
        self.leader = Leader(self.language.genName())

    def borders(self):
        border_tiles = []
        owned_tiles = []
        for settlement in self.settlements:
            x = settlement.x
            y = settlement.y
            owned_tiles += (x, y)
            for tile in adjacent(x, y):
                if tile not in border_tiles and tile not in owned_tiles:
                    border_tiles += tile
        for tile in border_tiles:
            if tile in owned_tiles:
                border_tiles.remove(tile)
        return border_tiles

    def action(self):
        pass

    def neighbors(self):
        pass
