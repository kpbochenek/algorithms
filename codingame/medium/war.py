import sys, math
from collections import deque


def convert(x):
    if x.startswith("10"): return "10"
    if x[0] == 'J': return "11"
    if x[0] == 'Q': return "12"
    if x[0] == 'K': return "13"
    if x[0] == 'A': return "14"
    return x[0]

n = int(input()) # the number of cards for player 1
qp1 = deque([int(convert(input())) for i in range(n)])

m = int(input()) # the number of cards for player 2
qp2 = deque([int(convert(input())) for i in range(m)])

rounds = 0
left = []
right = []
try:
    while qp1 and qp2:
        p1 = qp1.popleft()
        p2 = qp2.popleft()
        left.append(p1)
        right.append(p2)
        print("FIGHT {} {}".format(p1, p2), file=sys.stderr)
        if p1 < p2:
            qp2.extend(left)
            qp2.extend(right)
            left, right = [], []
        elif p1 > p2:
            qp1.extend(left)
            qp1.extend(right)
            left, right = [], []
        else:
            for i in range(3):
                left.append(qp1.popleft())
                right.append(qp2.popleft())
            rounds -= 1
        rounds += 1
except IndexError:
    print("PAT")
else:
    if not qp1:
        print("2 {}".format(rounds))
    elif not qp2:
        print("1 {}".format(rounds))

# To debug: print("Debug messages...", file=sys.stderr)
