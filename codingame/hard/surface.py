import collections

W = int(input())
H = int(input())

mapa = [input() for i in range(H)]
cache = [[-1 for x in range(W)] for y in range(H)]


def calculate_cache(px, py):
    global cache, mapa
    if mapa[py][px] == '#':
        cache[py][px] = 0
        return
    
    visited = set()
    value = 0
    queue = collections.deque()
    queue.append((px, py))
    while queue:
        (cx, cy) = queue.pop()
        if (cx, cy) not in visited:
            value += 1
            visited.add((cx, cy))
            if cx > 0   and mapa[cy][cx-1] != '#': queue.append((cx-1, cy))
            if cx < W-1 and mapa[cy][cx+1] != '#': queue.append((cx+1, cy))
            if cy > 0   and mapa[cy-1][cx] != '#': queue.append((cx, cy-1))
            if cy < H-1 and mapa[cy+1][cx] != '#': queue.append((cx, cy+1))

    for val in visited:
        cache[val[1]][val[0]] = value


N = int(input())
for i in range(N):
    X, Y = [int(j) for j in input().split()]
    if cache[Y][X] == -1:
        calculate_cache(X, Y)
    
    print(cache[Y][X])
