import sys
import math

# The machines are gaining ground. Time to show them what we're really made of...

mapa = []

nodes = set()

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    row = []
    for l in input():  # width characters, each either a number or a '.'
        if l == '.':
            row.append(-1)
        else:
            nodes.add((i, len(row)))
            row.append(int(l))
    mapa.append(row)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def neighbour(pos, move):
    pass

def check_single_neighbour(pos):
    left = neighbour(pos, (-1, 0))
    right = neighbour(nx, ny, -1, 0)
    top = neighbour(nx, ny, -1, 0)
    bottom = neighbour(nx, ny, -1, 0)


def check_2(nx, ny):
    pass


print("NODES: " + str(nodes), file=sys.stderr)

while nodes:
    new_nodes = set()
    for pos in nodes:
        (nx, ny) = pos
        check_single_neighbour(pos)
        check_2(nx, ny)
        if mapa[ny][nx] > 0:
            new_nodes.add(pos)


    nodes = new_nodes


# Two coordinates and one integer: a node, one of its neighbors, the number of links connecting them.
print("0 0 2 0 1")
print("2 0 2 2 1") 
