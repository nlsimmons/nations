from Settlement import Settlement
import random


class Tile():
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.fertility = random.randint(1, 10)
        # Resource abundance (like minerals, oil)

    def settle(self):
        self.settlement = Settlement(self.world)
        self.color = self.settlement.color
