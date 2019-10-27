from tkinter import *

root = Tk()
canv = Canvas(root, width = 500, height = 500, bg = "lightblue", cursor = "pencil")
canv.pack()
rect = canv.create_rectangle(50, 50, 100, 100, fill = "blue")

def blink1():
    canv.itemconfig(rect, fill="red")
    root.after(500, blink2)
def blink2():
    canv.itemconfig(rect, fill="blue")
    root.after(500, blink1)

blink1()
mainloop()