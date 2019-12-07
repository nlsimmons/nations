import random
# from pprint import pprint


def incrange(start, end):
    return range(start, end + 1)


class World(object):
    """docstring for ClassName"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[0 for x in range(width)] for y in range(height)]

    def generate(self):
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
