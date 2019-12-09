import random
from Nation import Nation

colors = ("dark olive green", "dark khaki", "gold", "firebrick1", "khaki",
          "forest green", "mediumorchid4", "magenta2", "skyblue1",
          "linen")


class Settlement():
    def __init__(self, owner=None):
        self.color = random.choice(colors)
        if owner is None:
            owner = Nation(color=self.color,
                           capital=self)
        self.owner = owner
