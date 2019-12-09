import random

class Leader(object):
    def __init__(self, name):
        self.name = name

        self.aggression = random.randint(1, 10)
        self.diplomacy = 10 - self.aggression
        self.effectiveness = random.randint(1, 10)
        self.charisma = random.randint(1, 10)
