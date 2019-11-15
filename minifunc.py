
def grab(n):
    global turn_end
    turn_end = True
    y1 = bots[botnum][0] + movey[n]
    x1 = bots[botnum][1] + movex[n]
    if map1[y1][x1] == "p":
        map1[y1][x1] = "f"
        canv.create_rectangle(SIZE * x1,
                              SIZE * y1,
                              SIZE * (x1 + 1),
                              SIZE * (y1 + 1),
                              fill="green")
    elif map1[y1][x1] == "f":
        map1[y1][x1] = "0"
        bots[botnum][2] += 10
        canv.create_rectangle(SIZE * x1,
                              SIZE * y1,
                              SIZE * (x1 + 1),
                              SIZE * (y1 + 1),
                              fill="lightblue")
    bots[botnum][4] = (bots[botnum][4] + movegen[map1[y1][x1]]) % 80


def attack(n):
    global turn_end
    turn_end = True
    y1 = bots[botnum][0] + movey[n]
    x1 = bots[botnum][1] + movex[n]
    if map1[y1][x1] in ["p", "f"]:
        map1[y1][x1] = "0"
        canv.create_rectangle(SIZE * x1,
                              SIZE * y1,
                              SIZE * (x1 + 1),
                              SIZE * (y1 + 1),
                              fill="lightblue")
    elif map1[y1][x1] == "b":
        for i in range(alive):
            if bots[i][0] == y1 and bots[i][1] == x1:
                bots[i][2] -= 10
                bots[botnum][2] += 10
                if bots[i][2] <= 0:
                    dead(i)
    bots[botnum][4] = (bots[botnum][4] + movegen[map1[y1][x1]]) % 80

def turn(n):
    global overload
    overload += 1
    bots[botnum][3] = n
    bots[botnum][4] = (bots[botnum][4] + 1) % 80


def look(n):
    global overload
    overload += 1
    bots[botnum][4] = (bots[botnum][4] + movegen[map1[bots[botnum][0] + movey[n]][bots[botnum][1] + movex[n]]]) % 80


def move(n):
    global turn_end
    turn_end = True
    y1 = bots[botnum][0] + movey[n]
    x1 = bots[botnum][1] + movex[n]
    cell = map1[y1][x1]
    if cell == "f":
        canv.create_rectangle(SIZE * x1,
                              SIZE * y1,
                              SIZE * (x1 + 1),
                              SIZE * (y1 + 1),
                              fill="lightblue")
        bots[botnum][2] += 10
        map1[y1][x1] = "b"
        map1[bots[botnum][0]][bots[botnum][1]] = "0"
        bots[botnum][0] = y1
        bots[botnum][1] = x1
        canv.move(bots[botnum][5], movex[n] * SIZE, movey[n] * SIZE)
    elif cell == "p":
        dead(botnum)
    elif cell == "0":
        map1[y1][x1] = "b"
        map1[bots[botnum][0]][bots[botnum][1]] = "0"
        bots[botnum][0] = y1
        bots[botnum][1] = x1
        canv.move(bots[botnum][5], movex[n] * SIZE, movey[n] * SIZE)
    bots[botnum][4] = (bots[botnum][4] + movegen[map1[y1][x1]]) % 80
def dead(bot):
    global bots, alive, botnum
    map1[bots[bot][0]][bots[bot][1]] = "0"
    canv.create_rectangle(SIZE * bots[bot][1],
                          SIZE * bots[bot][0],
                          SIZE * (bots[bot][1] + 1),
                          SIZE * (bots[bot][0] + 1),
                          fill="lightblue")
    bots = bots[:bot] + bots[bot + 1:] + bots[bot]
    alive -= 1
    botnum -= 1
    if alive == 8:
        mutate()


def mutate():
    global alive, turn_end, overload, botnum
    alive = 64
    turn_end = False
    overload = 0
    botnum = 1
    for i in range(64):
        genomes[i] = genomes[i % 8][:]
        bots[i][2] = 20
    for i in range(8, 64):
        y = randint(0, 26)
        x = randint(0, 47)
        while map1[y][x] in ["*", "b"]:
            y = randint(0, 26)
            x = randint(0, 47)
        map1[y][x] = "b"
        canv.create_rectangle(SIZE * x,
                              SIZE * y,
                              SIZE * (x + 1),
                              SIZE * (y + 1),
                              fill="lightblue")
        canv.move(bots[i][5], SIZE * (x - bots[i][1]), SIZE * (y - bots[i][0]))
        bots[i][0] = y
        bots[i][1] = x
    for i in range(8):
        for j in range(randint(1, 3)):
            genomes[i][randint(0, 79)] = randint(0, 79)
