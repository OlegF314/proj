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
        if canv.coords(rect)[2] < 200:
            root.after(10, more1)
        else:
            root.after(10, less1)
    else:
        root.after(10, blink2)

def more1():
    x1, y1, x2, y2 = canv.coords(rect)
    canv.coords(rect, x1 - 0.25, y1 - 0.25, x2 + 0.25, y2 + 0.25)
    root.after(10, glide1)

def less1():
    x1, y1, x2, y2 = canv.coords(rect)
    canv.coords(rect, x1 + 0.25, y1 + 0.25, x2 - 0.25, y2 - 0.25)
    root.after(10, glide1)

def blink2():
    canv.itemconfig(rect, fill="blue")
    root.after(10, glide2)

def glide2():
    canv.move(rect, -1, 0)
    if canv.coords(rect)[2] > 100:
        if canv.coords(rect)[2] > 200:
            root.after(10, less2)
        else:
            root.after(10, more2)
    else:
        root.after(10, blink1)

def more2():
    x1, y1, x2, y2 = canv.coords(rect)
    canv.coords(rect, x1 - 0.25, y1 - 0.25, x2 + 0.25, y2 + 0.25)
    root.after(10, glide2)

def less2():
    x1, y1, x2, y2 = canv.coords(rect)
    canv.coords(rect, x1 + 0.25, y1 + 0.25, x2 - 0.25, y2 - 0.25)
    root.after(10, glide2)

blink1()
mainloop()