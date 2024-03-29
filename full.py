from tkinter import *
from random import *
import matplotlib.pyplot as plt
import sys

WIDTH = 48
HEIGHT = 27
SIZE = 30
MODES = 5
MUTATION_STRENGTH = 5
MAP = open("map0.evo", "r")
root = Tk()
canv = Canvas(root, width=1440, height=810, bg="black")
canv.pack()
flag1 = False
lifetimes = []
#genomes = [[randint(0, 79) for i in range(80)] for j in range(64)]
genomes = [list(map(int, open("genom.evo", "r").readline().split())) for i in range(64)]
bots = [[10 + i % 8, 20 + i // 8, 20, 0, 0] for i in range(64)]
# [0] - y
# [1] - x
# [2] - HP
# [3] - orientation:
# 7 0 1
# 6 b 2
# 5 4 3
# [4] - genome pointer
# [5] - graphic rectangle
alive = 64
movey = [-1, -1, 0, 1, 1, 1, 0, -1]
movex = [0, 1, 1, 1, 0, -1, -1, -1]
movegen = {"p": 1, "*": 2, "b": 3, "f": 4, "0": 5}
map1 = []
map2 = []
botnum = 0
turn_end = False
overload = 0
gen_time = 0
colors = {"*": "brown",
          "0": "lightblue",
          "p": "purple",
          "f": "green",
          "b": "red"}
for i in range(HEIGHT):
    map1.append(list(list(MAP.readline().strip())))


def gen_bot(i):
    y = randint(1, 25)
    x = randint(1, 46)
    while map1[y][x] in ["*", "b"]:
        y = randint(1, 25)
        x = randint(1, 46)
    map1[y][x] = "b"
    bots[i][0] = y
    bots[i][1] = x


for i in range(64):
    gen_bot(i)

for i in range(HEIGHT):
    map2.append(
        [canv.create_rectangle(j * SIZE, i * SIZE, (j + 1) * SIZE, (i + 1) * SIZE, fill=colors[map1[i][j]]) for j in
         range(WIDTH)])


# 0 = empty
# * = wall
# p = poison
# f = food
# b = bot
def finish(event):
    global flag1
    if event.keysym == "space":
        flag1 = True


def handover():
    global botnum, overload, turn_end, bots, genomes, gen_time
    bots[botnum][2] -= 1  # Скушал хп у бота
    if bots[botnum][2] <= 0:
        dead(botnum)
    if botnum == alive - 1:
        botnum = 0
        gen_food()
        gen_time += 1
    else:
        botnum += 1
    overload = 0
    turn_end = False


def grab(n):
    global turn_end, botnum
    turn_end = True
    y1 = bots[botnum][0] + movey[n]
    x1 = bots[botnum][1] + movex[n]
    if map1[y1][x1] == "p":
        map1[y1][x1] = "f"
        canv.itemconfig(map2[y1][x1], fill="green")
    elif map1[y1][x1] == "f":
        map1[y1][x1] = "0"
        bots[botnum][2] = min(bots[botnum][2] + 10, 90)
        canv.itemconfig(map2[y1][x1], fill="lightblue")
    bots[botnum][4] = (bots[botnum][4] + movegen[map1[y1][x1]]) % 80


def attack(n):
    global turn_end, botnum
    turn_end = True
    y1 = bots[botnum][0] + movey[n]
    x1 = bots[botnum][1] + movex[n]
    if map1[y1][x1] in ["p", "f"]:
        map1[y1][x1] = "0"
        canv.itemconfig(map2[y1][x1], fill="lightblue")
    elif map1[y1][x1] == "b":
        for i in range(alive):
            if bots[i][0] == y1 and bots[i][1] == x1:
                bots[i][2] -= 10
                bots[botnum][2] = min(bots[botnum][2] + 10, 90)
                if bots[i][2] <= 0:
                    dead(i)
    bots[botnum][4] = (bots[botnum][4] + movegen[map1[y1][x1]]) % 80


def turn(n):
    global overload, botnum
    overload += 1
    bots[botnum][3] = n
    bots[botnum][4] = (bots[botnum][4] + 1) % 80


def look(n):
    global overload, botnum
    overload += 1
    bots[botnum][4] = (bots[botnum][4] + movegen[map1[bots[botnum][0] + movey[n]][bots[botnum][1] + movex[n]]]) % 80


def move(n):
    global turn_end, botnum
    turn_end = True
    y1 = bots[botnum][0] + movey[n]
    x1 = bots[botnum][1] + movex[n]
    cell = map1[y1][x1]
    if cell == "f":
        canv.itemconfig(map2[y1][x1], fill="lightblue")
        bots[botnum][2] = min(bots[botnum][2] + 10, 90)
        map1[y1][x1] = "b"
        map1[bots[botnum][0]][bots[botnum][1]] = "0"
        canv.itemconfig(map2[bots[botnum][0]][bots[botnum][1]], fill="lightblue")
        canv.itemconfig(map2[y1][x1], fill="red")
        bots[botnum][0] = y1
        bots[botnum][1] = x1
    elif cell == "0":
        map1[y1][x1] = "b"
        map1[bots[botnum][0]][bots[botnum][1]] = "0"
        canv.itemconfig(map2[y1][x1], fill="red")
        canv.itemconfig(map2[bots[botnum][0]][bots[botnum][1]], fill="lightblue")
        bots[botnum][0] = y1
        bots[botnum][1] = x1
    elif cell == "p":
        bots[botnum][2] = 0
#        dead(botnum)
    bots[botnum][4] = (bots[botnum][4] + movegen[map1[y1][x1]]) % 80


def dead(bot):
    global bots, alive, botnum, genomes
    map1[bots[bot][0]][bots[bot][1]] = "0"
    canv.itemconfig(map2[bots[bot][0]][bots[bot][1]], fill="lightblue")
    bots[bot][0] = bots[bot][1] = -1
    bots = bots[:bot] + bots[bot + 1:] + [bots[bot]]
    genomes = genomes[:bot] + genomes[bot + 1:] + [genomes[bot]]
    alive -= 1
    if botnum >= bot:
        botnum -= 1
    if alive == 8:
        mutate()


def gen_food():
    k = 0
    while k != 2:
        z = randint(0, 26)
        m = randint(0, 47)
        if map1[z][m] not in ["*", "b"]:
            map1[z][m] = "f"
            canv.itemconfig(map2[z][m], fill="green")
            k += 1
    k = 0
    while k != 5:
        z = randint(0, 26)
        m = randint(0, 47)
        if map1[z][m] not in ["*", "b"]:
            map1[z][m] = "p"
            canv.itemconfig(map2[z][m], fill="purple")
            k += 1



def mutate():
    global alive, turn_end, overload, botnum, flag1, gen_time
    #    print('\n'.join(map(''.join, map1)), end='\n\n')
    #print(sum(map1[i].count('b') for i in range(27)), alive)
    root.bind("<Key>", finish)
    alive = 64
    lifetimes.append(gen_time)
    gen_time = 0
    turn_end = False
    overload = 0
    botnum = 0
    if flag1:
        for j in range(1, 9):
            sys.stdout = open("outgenome" + str(j) + ".evo", "w")
            print(*genomes[j])
        #graph = plt.subplot
        plt.plot(list(range(len(lifetimes))), lifetimes)
        plt.grid()
        plt.show()
        sys.exit()
    for i in range(64):
        genomes[i] = genomes[i % 8][:]
        bots[i][2] = 20
    for i in range(8, 64):
        gen_bot(i)
        canv.itemconfig(map2[bots[i][0]][bots[i][1]], fill="red")
    for i in range(8):
        for j in range(randint(1, MUTATION_STRENGTH)):
            #canv.itemconfig(map2[bots[i][0]][bots[i][1]], fill="HotPink2")
            genomes[i][randint(0, 79)] = randint(0, 79)
    shuffle(genomes)


# def step1():


def mainfunc():
    global botnum, overload, turn_end, bots, genomes, alive  # Объявление глобальных переменных
    flag = True
    while genomes[botnum][bots[botnum][4]] > 39:
        overload += 1
        bots[botnum][4] = (bots[botnum][4] + genomes[botnum][bots[botnum][4]]) % 80
        if overload == 10:
            flag = False
            handover()  # Вызов функции передачи хода
            break
    if flag:
        act = genomes[botnum][bots[botnum][4]] // 8
        n = genomes[botnum][bots[botnum][4]] % 8
        switcher = {  # Словарь который послужит переключателем команд
            0: move,  # Тут написаны имена мини-функций
            1: grab,
            2: attack,
            3: turn,
            4: look
        }
        switcher[act](n)  # По ключу переходит к функции, аргументы функции задаются в ()
        if turn_end or overload == 10:  # Смена хода
            handover()
    root.after(1, mainfunc)

mainfunc()
mainloop()
