from World import World
from View import View
import random
# from pprint import pprint

random.seed(10)

world1 = World(30, 15)

world1.generateContinent()
world1.generateNations()

# pprint(world1.grid)

View(world=world1, scale=30)
