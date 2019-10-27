from tkinter import *

root = Tk()
canv = Canvas(root, width = 500, height = 500, bg = "lightblue", cursor = "pencil")
canv.pack()
rect = canv.create_rectangle(50, 50, 100, 100, fill = "blue")

def blink1():
    canv.itemconfig(rect, fill="red")
    root.after(10, glide1)
def glide1():
    canv.move(rect, 1, 0)
    if canv.coords(rect)[2] < 300:
        root.after(10, glide1)
    else:
        root.after(10, blink2)
def blink2():
    canv.itemconfig(rect, fill="blue")
    root.after(10, glide2)
def glide2():
    canv.move(rect, -1, 0)
    if canv.coords(rect)[2] > 100:
        root.after(10, glide2)
    else:
        root.after(10, blink1)
blink1()
mainloop()