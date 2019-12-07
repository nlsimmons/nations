# import random
from pprint import pprint


class World(object):
    """docstring for ClassName"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[0 for x in range(width)] for y in range(height)]

        pprint(self.grid)

    def generate(self):
        pass