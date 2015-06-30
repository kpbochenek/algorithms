# W: width of the building.
# H: height of the building.
W, H = [int(i) for i in input().split()]
N = int(input())  # maximum number of turns before game over.
X0, Y0 = [int(i) for i in input().split()]

left, right, top, bottom = 0, W, 0, H

# game loop
while 1:
    BOMB_DIR = input()

    if 'U' in BOMB_DIR:
        bottom = Y0
        Y0 = top + (Y0 - top) // 2
    if 'D' in BOMB_DIR:
        top = Y0
        Y0 = Y0 + (bottom - Y0 + 1) // 2
    if 'L' in BOMB_DIR:
        right = X0
        X0 = left + (X0 - left) // 2
    if 'R' in BOMB_DIR:
        left = X0
        X0 = X0 + (right - X0 + 1) // 2

    print(str(X0) + " " + str(Y0))
