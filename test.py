
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
    bots[botnum][3] = (bots[botnum][3] + n) % 8
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
def back(n)