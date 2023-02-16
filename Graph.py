from Vertex import *
class Graph:
    def __init__(self):
        self.edges = []
        self.vertex = []

    def addVertex(self, vertex):
        self.vertex.append(vertex)


def createGraph(M):
    G = Graph()
    height = len(M)
    width = len(M[0])
    for row in range(height):
        for col in range(width):
            if M[row][col]==1 or M[row][col]==3:
               tmp = Vertex((row,col))
               createNeighbour(row, col, M, tmp)
               G.addVertex(tmp)
    return G

def createNeighbour(i,j,M, V):
    height = len(M)
    width = len(M[0])
    if i -1 >=0 and M[i-1][j]!=2:
        V.addNeighbour((i-1,j),1)

    if j -1 >=0 and M[i][j-1]!=2:
        V.addNeighbour((i,j-1),1)

    if i + 1 < height and M[i+1][j]!=2:
        V.addNeighbour((i+1,j),1)

    if j + 1 <width and M[i][j+1]!=2:
        V.addNeighbour((i,j+1),1)
