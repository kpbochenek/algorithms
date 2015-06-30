from itertools import groupby

R = [input()]
L = int(input())

line = R
while L > 1:
    L -= 1
    line = sum([[str(len(list(elems))), k] for k, elems in groupby(line)], [])

print(" ".join(line))
