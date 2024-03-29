from tkinter import *
from random import *
import matplotlib.pyplot as plt


WIDTH = 48
HEIGHT = 27
SIZE = 30
MODES = 5
movey = [-1, -1, 0, 1, 1, 1, 0, -1]
movex = [0, 1, 1, 1, 0, -1, -1, -1]
movegen = {"p" : 1, "*" : 2, "b" : 3, "f" : 4, "0" : 5}
MAP = open("map.evo", "r")
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show()
root = Tk()
canv = Canvas(root, width=1440, height=810, bg="black")
canv.pack()
genomes = [list(map(int, open("genom.evo", "r").readline().split())) for i in range(64)]
bots = [[20 + i // 8, 10 + i % 8, 20, 0, 0] for i in range(64)]
#[0] - y
#[1] - x
#[2] - HP
#[3] - orientation:
#7 0 1
#6 b 2
#5 4 3
#[4] - genome pointer
#[5] - graphic rectangle
alive = 64
map1 = []
for i in range(HEIGHT):
    map1.append(list(MAP.readline()))
for i in range(64):
    map1[10 + i % 8][20 + i // 8] = "b"
#0 = empty
#* = wall
#p = poison
#f = food
#b = bot
def create_field():#20-27x10-17
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if map1[i][j] == '*':
                canv.create_rectangle(j * SIZE,
                                      i * SIZE,
                                      (j + 1) * SIZE,
                                      (i + 1) * SIZE,
                                      fill="brown")
            else:
                canv.create_rectangle(j * SIZE,
                                      i * SIZE, 
                                      (j + 1) * SIZE,
                                      (i + 1) * SIZE,
                                      fill="lightblue")
    for i in range(64):
        bots[i].append(canv.create_rectangle(SIZE * (20 + i // 8),
                                             SIZE * (10 + i % 8),
                                             SIZE * ((20 + i // 8) + 1),
                                             SIZE * ((10 + i % 8) + 1),
                                             fill="red"))

#def step1():



create_field()
mainloop()
