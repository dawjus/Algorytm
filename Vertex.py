class Vertex:
    def __init__(self, index, name ="",weight = 0):
        self.index = index
        self.name = name
        self.weight = weight
        self.neighbours = []
        self.parent = None

    def addNeighbour(self, index, weight):
        self.neighbours.append((index, weight))


    def __str__(self):
        return "Index " +str(self.index[0]) + ", " + str(self.index[1]) +" Neighbours: " + str([i for i in self.neighbours])