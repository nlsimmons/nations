import random
from Nation import Nation

colors = ("dark olive green", "dark khaki", "gold", "firebrick1", "khaki",
          "forest green", "mediumorchid4", "magenta2", "skyblue1",
          "linen")


class Settlement():
    def __init__(self, world, nation=None):
        self.world = world
        self.color = random.choice(colors)
        if nation is None:
            nation = Nation(world=world,
                           color=self.color,
                           capital=self)
        self.nation = nation
        self.population = 10
        self.satisfaction = 5
