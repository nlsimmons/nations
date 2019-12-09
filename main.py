from World import World
from View import View
import random
# from pprint import pprint

random.seed(1)

print("Generating world...")

world1 = World(30, 15)

world1.generateContinent(300)

print("Generating settlements...")

world1.generateSettlements()

# world1.doRound()

# print("Doing round...")

View(world=world1, scale=30)
