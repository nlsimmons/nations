import random
from funcs import *
# from pprint import pprint


class World(object):
    """ Physical features of world map """
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[0 for x in range(width)] for y in range(height)]

    def generateNations(self):
        pass

    def generateNation(self):
        pass

    def generateContinent(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)

        self.grid[y][x] = 1

        queue = self.adjacent(x, y)
        while len(queue):
            random.shuffle(queue)
            (x, y, v) = queue.pop()
            if not self.grid[y][x] and random.randint(0, 100) < 30:
                queue += self.adjacent(x, y)
                self.grid[y][x] = 1

    def adjacent(self, x, y):
        square = []
        for x in incrange(x - 1, x + 1):
            for y in incrange(y - 1, y + 1):
                try:
                    square.append((x, y, self.grid[y][x]))
                except IndexError:
                    pass
        return square
