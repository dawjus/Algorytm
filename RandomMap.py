import random
from Graph import *
from Vertex import *


class RandomMap():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.map = [[-1 for _ in range(self.width)] for _ in range(self.height)]

    def randomMap(self):
        for row in range(self.width):
            for col in range(self.height):
                value = random.randint(0, 15)
                if value == 0:
                    self.map[row][col] = 1 #Vertex
                elif value in [1, 2, 3,4,5,6]:
                    self.map[row][col] = 2 #Tree
                else:
                    self.map[row][col] = 3 #Empty field
        return self.map

