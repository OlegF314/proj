from tkinter import *

root = Tk()
canv = Canvas(root, width = 500, height = 500, bg = "lightblue", cursor = "pencil")
canv.pack()
rect = canv.create_rectangle(50, 50, 100, 100, fill = "blue")


def blink1(color):
    canv.itemconfig(rect, fill=color)
    root.after(10, lambda: glide1(300))


def glide1(border):
    canv.move(rect, 1, 0)
    if canv.coords(rect)[2] < border:
        root.after(10, lambda: glide1(border))
    else:
        root.after(10, lambda: blink2("blue"))


def blink2(color):
    canv.itemconfig(rect, fill=color)
    root.after(10, lambda: glide2(100))


def glide2(border):
    canv.move(rect, -1, 0)
    if canv.coords(rect)[2] > border:
        root.after(10, lambda: glide2(100))
    else:
        root.after(10, lambda: blink1("red"))


blink1("red")
mainloop()
