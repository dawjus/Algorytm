from tkinter import *
from tkinter import ttk
import random
import RandomMap as Rm
import time
from Graph import *
from Dijkstra import *

class App:
    def __init__(self, sizecell, matrix):
        self.width = len(matrix)
        self.height = len(matrix[0])
        self.sizecell = sizecell
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.matrix = matrix
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.width*(sizecell+10), height=self.height*(sizecell+5))
        self.canvas.pack()
        self.start=1
        self.end =5
        self.draw_map()
        button = ttk.Button(
            self.root,
            text='Dijkstra',
            command = self.dijkstra
        )
        button.place(x=130, y=10)
        
        self.choiceStart = IntVar()
        self.choiceEnd = IntVar()
        cbStart = ttk.Combobox(self.root, textvariable=self.choiceStart, values=self.choices)
        cbStart.pack()
        cbEnd = ttk.Combobox(self.root, textvariable=self.choiceEnd, values=self.choices)
        cbEnd.pack()
        
       

    def dijkstra(self):
        G = createGraph(self.matrix)
        dist = dijkstra(G.vertex, G.vertex[self.choiceStart.get()])
        intek = self.choiceEnd.get()
        k = dist[G.vertex[intek].index]
        c = getShorthestPath(G, intek, k)
        for i in range(len(c)):
            self.matrix[c[i][0]][c[i][1]] = 4
        print(self.choiceStart.get())
        self.draw_map()

    def draw_map(self):
        
        self.choices = []
        countVertex=1
        for row in range(self.height):
            for col in range(self.width):
                x1 = col*(self.sizecell+3)
                y1 = row*(self.sizecell+3)
                x2 = x1+self.sizecell
                y2 = y1+self.sizecell
                value = self.matrix[row][col]

                if value == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                    counter = random.randint(0, len(self.alphabet)-1)
                    self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=self.alphabet[counter], font=("Arial", int(self.sizecell/1.4)))
                    self.alphabet = self.alphabet[:counter] + self.alphabet[counter+1:]
                    self.choices.append(countVertex)
                    countVertex+=1
                elif value ==2:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                    self.choices.append(countVertex)
                    countVertex+=1
                elif value ==3:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                elif value == 4:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")


    def run(self):
        self.root.mainloop()
        time.sleep(4)
        self.root.quit()


map = Rm.RandomMap(10, 10)
map = map.randomMap()
my_map2 = App(10, map)
my_map2.run()