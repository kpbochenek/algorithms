width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
mapa = []


def print_node(y, x):
    rx, ry = -1, -1
    bx, by = -1, -1
    for mx in range(x+1, width):
        if mapa[y][mx] != '.':
            rx, ry = mx, y
            break
    for my in range(y+1, height):
        if mapa[my][x] != '.':
            bx, by = x, my
            break
    print("%d %d %d %d %d %d" % (x, y, rx, ry, bx, by))


for i in range(height):
    line = input()  # width characters, each either 0 or .
    mapa.append(line)

for i in range(height):
    for j in range(width):
        if mapa[i][j] == '0':
            print_node(i, j)

print("0 0 1 0 0 1")
