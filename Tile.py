from Settlement import Settlement


class Tile(object):
    """docstring for Tile"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def settle(self):
        self.settlement = Settlement()
        self.color = self.settlement.color
