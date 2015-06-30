from collections import defaultdict

NORTH = ('N', 0, -1, 'NORTH')
SOUTH = ('S', 0, 1, 'SOUTH')
EAST = ('E', 1, 0, 'EAST')
WEST = ('W', -1, 0, 'WEST')


class Robot:
    def __init__(self, mapa):
        self.mapa = mapa
        self.dirs = [SOUTH, EAST, NORTH, WEST]
        self.dirs_rev = [WEST, NORTH, EAST, SOUTH]
        self.find_start()
        self.find_teleports()
        self.direction = SOUTH
        self.breaker = False
        self.output = []
        self.visited = defaultdict(lambda: 0)

    def find_start(self):
        for y, row in enumerate(mapa):
            for x, tile in enumerate(row):
                if tile == '@':
                    self.px, self.py = x, y
                    return

    def find_teleports(self):
        tps = False
        for y, row in enumerate(mapa):
            for x, tile in enumerate(row):
                if tile == 'T':
                    if tps:
                        self.tp2x = x
                        self.tp2y = y
                    else:
                        self.tp1x = x
                        self.tp1y = y
                        tps = True

    def can_move(self):
        nx = self.px + self.direction[1]
        ny = self.py + self.direction[2]
        return not((self.mapa[ny][nx] == '#') or (not self.breaker and self.mapa[ny][nx] == 'X'))

    def is_finished(self):
        if self.visited[(self.px, self.py)] > 5:
            self.output = ["LOOP"]
            return True
        return self.mapa[self.py][self.px] == '$'

    def move(self):
        self.visited[(self.px, self.py)] += 1
        self.px += self.direction[1]
        self.py += self.direction[2]
        self.output.append(self.direction[3])
        if self.mapa[self.py][self.px] == 'X': self.mapa[self.py] = self.mapa[self.py][:self.px] + ' ' + self.mapa[self.py][self.px+1:]

    def rotate(self):
        for d in self.dirs:
            self.direction = d
            if self.can_move():
                return

    def analyze_tile(self):
        tile = self.mapa[self.py][self.px]
        if tile == 'N': self.direction = NORTH
        if tile == 'S': self.direction = SOUTH
        if tile == 'E': self.direction = EAST
        if tile == 'W': self.direction = WEST
        if tile == 'B': self.breaker = not self.breaker
        if tile == 'I': self.dirs, self.dirs_rev = self.dirs_rev, self.dirs
        if tile == 'T': self.teleport()

    def teleport(self):
        if self.px == self.tp1x and self.py == self.tp1y:
            self.px, self.py = self.tp2x, self.tp2y
        else:
            self.px, self.py = self.tp1x, self.tp1y

L, C = [int(i) for i in input().split()]
mapa = [input() for i in range(L)]

c = Robot(mapa)
while not c.is_finished():
    c.analyze_tile()
    if not c.can_move():
        c.rotate()
    c.move()

for direction in c.output:
    print(direction)
