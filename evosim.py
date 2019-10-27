from tkinter import *
from random import *


WIDTH = 48
HEIGHT = 27
SIZE = 30
MAP = open("map.evo", "r")
root = Tk()
canv = Canvas(root, width=1440, height=810, bg="black")
canv.pack()


def create_field():
    field = MAP.readlines()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if field[i][j] == '1':
                canv.create_rectangle(j * SIZE, i * SIZE, (j + 1) * SIZE, (i + 1) * SIZE, fill="brown")
            else:
                canv.create_rectangle(j * SIZE, i * SIZE, (j + 1) * SIZE, (i + 1) * SIZE, fill="lightblue")


create_field()
mainloop()
