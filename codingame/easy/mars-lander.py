import sys, math


N = int(input()) # the number of points used to draw the surface of Mars.
LAND_X = [0 for i in range(N)]
LAND_Y = [0 for i in range(N)]
for i in range(N):
    LAND_X[i], LAND_Y[i] = [int(i) for i in input().split()]

while 1:
    X, Y, HS, VS, F, R, P = [int(i) for i in input().split()]

    print("DEBUG: " + str(VS), file=sys.stderr)
    if VS < -20:
        print("0 4")
    else:
        print("0 2")
