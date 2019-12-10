import random
from Settlement import Settlement


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

    def getInfo(self):
        string = f"({self.x}, {self.y}); Fertility: {self.fertility}\n"\
                 f"Settlement: {self.settlement}\n"\
                 f"Led by {self.settlement.leader}\n"\
                 f"Owned by {self.settlement.nation}\n"\
                 f"Ruled by {self.settlement.nation.leader}\n"\
                 f"---------------\n"\
                 f"{self.settlement.leader}'s Traits:\n"\
                 f"{self.settlement.leader.getTraits()}\n"\
                 f"---------------\n"\
                 f"{self.settlement.nation.leader}'s Traits:\n"\
                 f"{self.settlement.nation.leader.getTraits()}\n"\

        return string
