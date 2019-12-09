import random
from funcs import *
from pprint import pprint
from Tile import Tile


class World(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = []
        self.settlements = []

        self.grid = [[0 for x in range(width)] for y in range(height)]

    def randomLand(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if self.grid[y][x]:
                return self.grid[y][x]

    def indexTiles(self):
        self.tiles = []
        for x in incrange(0, self.width - 1):
            for y in incrange(0, self.height - 1):
                if self.grid[y][x]:
                    self.tiles.append(self.grid[y][x])

    def generateContinent(self):
        # x = random.randint(0, self.width - 1)
        # y = random.randint(0, self.height - 1)
        x = round((0 + self.width) / 2)
        y = round((0 + self.height) / 2)

        self.grid[y][x] = Tile(x, y)

        queue = self.adjacent(x, y)
        while len(queue):
            random.shuffle(queue)
            (x, y, tile) = queue.pop()
            if self.grid[y][x] == 0 and random.randint(0, 100) < 30:
                queue += self.adjacent(x, y)
                self.grid[y][x] = Tile(x, y)

        self.indexTiles()

    def generateSettlements(self):
        for tile in self.tiles:
            tile.settle()

    def adjacent(self, x_start, y_start):
        square = []
        for x in incrange(x_start - 1, x_start + 1):
            for y in incrange(y_start - 1, y_start + 1):
                if (x == x_start and y == y_start or
                   x < 0 or x >= self.width or
                   y < 0 or y >= self.height):
                    continue
                try:
                    square.append((x, y, self.grid[y][x]))
                except IndexError:
                    pass
        return square
