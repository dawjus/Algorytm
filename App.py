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
        self.root.title("Find shorthest path")
        self.canvas = Canvas(self.root, width=self.width*(sizecell+18), height=self.height*(sizecell+5))
        self.canvas.pack()
        self.draw_map()
        
        button = ttk.Button(
            self.root,
            text='Find path',
            command = self.dijkstra
        )
        button.place(x=130, y=10)
        label = Label(self.root, text='Start Vertex:')
        label.place(x=130, y=40)
        label2 = Label(self.root, text='End Vertex:')
        label2.place(x=130, y=90)
        self.choiceStart = StringVar()
        self.choiceEnd = StringVar()
        cbStart = ttk.Combobox(self.root, textvariable=self.choiceStart, values=self.choices)
        cbStart.place(x=130,y=60)
        
        cbEnd = ttk.Combobox(self.root, textvariable=self.choiceEnd, values=self.choices)
        cbEnd.place(x=130, y=110)
        

        
       

    def dijkstra(self):
        G = createGraph(self.matrix)
        dist = dijkstra(G.vertex, G.vertex[self.dict[self.choiceStart.get()]])
        end = self.dict[self.choiceEnd.get()]
        distance = dist[G.vertex[end].index]
        c = getShorthestPath(G, end, distance)
        for i in range(len(c)):
            self.matrix[c[i][0]][c[i][1]] = 4
        self.draw_map()


    def draw_map(self):
        self.dict ={}
        self.choices = []
        countVertex=0
        count =0
        for row in range(self.height):
            for col in range(self.width):
                x1 = col*(self.sizecell+3)
                y1 = row*(self.sizecell+3)
                x2 = x1+self.sizecell
                y2 = y1+self.sizecell
                value = self.matrix[row][col]

                if value == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red") #Vertex
                    self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=self.alphabet[count], font=("Arial", int(self.sizecell/1.4)))
                    self.choices.append(self.alphabet[count])
                    self.dict.update({self.alphabet[count]: countVertex})
                    count +=1
                    countVertex+=1
                elif value ==2:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green") #Tree
                elif value ==3:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue") #empty field
                    countVertex+=1
                elif value == 4:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow") #path


    def run(self):
        self.root.mainloop()



map = Rm.RandomMap(10, 10)
my_map = App(10, map.randomMap())
my_map.run()