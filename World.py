import random
from funcs import *
from pprint import pprint
from Tile import Tile


class World(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = []
        self.year = 0

        self.grid = [[0 for x in range(width)] for y in range(height)]

    def doRound(self):
        # year += 1
        random.shuffle(self.tiles)
        # for tile in self.tiles:
            # tile.nation.

    def indexTiles(self):
        self.tiles = []
        for x in incrange(0, self.width - 1):
            for y in incrange(0, self.height - 1):
                if self.grid[y][x]:
                    self.tiles.append(self.grid[y][x])

    def generateContinent(self, size):
        # x = random.randint(0, self.width - 1)
        # y = random.randint(0, self.height - 1)
        x = round(self.width / 2)
        y = round(self.height / 2)

        self.grid[y][x] = Tile(self, x, y)

        queue = adjacent(x, y, self.width, self.height)

        while len(queue):
            (x, y) = queue.pop()
            if self.grid[y][x] == 0 and random.randint(0, 1000) < size:
                queue += adjacent(x, y, self.width, self.height)
                self.grid[y][x] = Tile(self, x, y)

        self.indexTiles()

    def generateSettlements(self):
        for tile in self.tiles:
            tile.settle()

