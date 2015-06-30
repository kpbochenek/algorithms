# W: number of columns.
# H: number of rows.
W, H = [int(i) for i in input().split()]
labirynth = []
for i in range(H):
    labirynth.append(list(map(int, input().split())))
EX = int(input())


def next_pos(xp, yp, where):
    global labirynth
    tale = labirynth[yp][xp]
    if tale == 1:
        return xp, yp+1
    elif tale == 2 and where == 'LEFT':
        return xp+1, yp
    elif tale == 2 and where == 'RIGHT':
        return xp-1, yp
    elif tale == 3:
        return xp, yp+1
    elif tale == 4 and where == 'TOP':
        return xp-1, yp
    elif tale == 4 and where == 'RIGHT':
        return xp, yp+1
    elif tale == 5 and where == 'TOP':
        return xp+1, yp
    elif tale == 5 and where == 'LEFT':
        return xp, yp+1
    elif tale == 6 and where == 'LEFT':
        return xp+1, yp
    elif tale == 6 and where == 'RIGHT':
        return xp-1, yp
    elif tale == 7:
        return xp, yp+1
    elif tale == 8:
        return xp, yp+1
    elif tale == 9:
        return xp, yp+1
    elif tale == 10 and where == 'TOP':
        return xp-1, yp
    elif tale == 11 and where == 'TOP':
        return xp+1, yp
    elif tale == 12:
        return xp, yp+1
    elif tale == 13:
        return xp, yp+1

while 1:
    XI, YI, POS = input().split()
    XI = int(XI)
    YI = int(YI)

    x, y = next_pos(XI, YI, POS)

    print("{} {}".format(x, y))
