import random
from Entity import Entity


class Leader(Entity):
    def __init__(self, name):
        self.name = name

        self.aggression = random.randint(1, 10)
        self.diplomacy = 10 - self.aggression
        self.ability = random.randint(1, 10)
        self.charisma = random.randint(1, 10)

    def getTraits(self):
        return f"Agg: {self.aggression}; Dip: {self.diplomacy}; "\
               f"Abl: {self.ability}; Cha: {self.charisma}"