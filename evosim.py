from tkinter import *

# from random import *
# import matplotlib.pyplot as plt


WIDTH = 48
HEIGHT = 27
SIZE = 30
MODES = 5
movey = [-1, -1, 0, 1, 1, 1, 0, -1]
movex = [0, 1, 1, 1, 0, -1, -1, -1]
MAP = open("map.evo", "r")
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show()
root = Tk()
canv = Canvas(root, width=1440, height=810, bg="black")
canv.pack()
genomes = [list(map(int, open("genom.evo", "r").readline().split())) for i in range(64)]
bots = [[20 + i // 8, 10 + i % 8, 20, 0, 0] for i in range(64)]
alive = 64
map1 = []
botnum = 1
turn_end = 1  # Номер бота=1                          #Флаг на окончание хода               #Число ботов
overload = 0


for i in range(HEIGHT):
    map1.append(list(MAP.readline()))
for i in range(64):
    map1[10 + i % 8][20 + i // 8] = "b"


# 0 = empty
# * = wall
# p = poison
# f = food
# b = bot
def create_field():  # 20-27x10-17
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


# def step1():


def mainfunc():
    global botnum, overload, turn_end,bots,genome # Объявление глобальных переменных
    if botnum == 1:
        gen_food()                     # Генерация еды
    act = genome [botnum] [bots [botnum] [4] ] // 8  # Тут надо вынуть цифру из массива bots и преобразовать к человеческому блен виду чтобы сунуть в switcher
    switcher = {  # Словарь который послужит переключателем команд
        1: grab,  # Тут написаны имена мини-функций
        2: attack,
        3: turn,
        4: move,
        5: look,
    }
    root.after(10,switcher[act]())  # По ключу переходит к функции, аргументы функции задаются в ()
    bots[botnum][2] -= 1            #Скушал хп у бота
    if alive == 8:
        mutate()                    # мутатор
        botnum = 1
        overload = 0
        turn_end = 1
        mainfunc()
    if turn_end == 0 or overload == 10:  # Смена хода
        botnum += 1
        overload = 0
        turn_end = 1
    mainfunc()


create_field()
mainloop()
