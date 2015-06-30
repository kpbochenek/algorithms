import math

to_float = lambda x: float(x.replace(',', '.'))

LON = to_float(input())
LAT = to_float(input())
N = int(input())

name = None
best = -1
for i in range(N):
    D = input().split(';')
    x = (to_float(D[4]) - LON) * math.cos((LAT + to_float(D[5])) / 2)
    y = to_float(D[5]) - LAT
    dist = math.sqrt(x*x + y*y) * 6371
    if name is None or dist < best:
        best = dist
        name = D[1]

print(name)
