import sys
import math
from collections import deque

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, c, n = [int(i) for i in input().split()]

groups = []
for i in range(n):
    pi = int(input())
    groups.append(pi)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

answer = 0

start = [-1 for i in range(n)]
count = [-1 for i in range(n)]

posg = 0
i = 0
loopok = True
while i < c:
    if start[posg] != -1 and loopok:
        profit = answer - start[posg]
        loopr = i - count[posg]
        can_loop = (c - i) // loopr
        i += can_loop * loopr
        answer += profit * can_loop
        loopok = False
    else:
        start[posg] = answer
        count[posg] = i
    
    if i < c:
        suma = groups[posg]
        cg = posg
        posg = (posg + 1) % len(groups)
        while cg != posg and suma + groups[posg] <= l:
            suma += groups[posg]
            posg = (posg + 1) % len(groups)
        answer += suma
        i += 1

print(answer)
