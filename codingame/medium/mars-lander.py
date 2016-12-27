import sys
from math import *

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(input()) # the number of points used to draw the surface of Mars.

LAND_X, LAND_Y = -1, -1
PREV_X, PREV_Y = -1, -1
for i in range(N):
    # LAND_X: X coordinate of a surface point. (0 to 6999)
    # LAND_Y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    IN_X, IN_Y = [int(i) for i in input().split()]
    if PREV_Y == IN_Y:
        LAND_X = PREV_X
        LAND_Y = PREV_Y
    PREV_X, PREV_Y = IN_X, IN_Y
    
print("LAND " + str(LAND_X) + " : " + str(LAND_Y), file=sys.stderr)


def isOverTarget(x):
    return LAND_X <= x and x <= LAND_X + 1000
    
    
def isFinishing(y):
    return y < LAND_Y + 20
    
    
def hasSafeSpeed(dx, dy):
    return abs(dx) <= 20 - 5 and abs(dy) <= 40 - 5
    
    
def goesInWrongDirection(x, dx):
    return (x < LAND_X and dx < 0) or (LAND_X+1000 < x and dx > 0)
    
    
def goesTooFastHorizontally(dx):
    return abs(dx) > 4*20
    
    
def goesTooSlowHorizontally(dx):
    return abs(dx) < 2*20
    
    
def angleToSlow(dx, dy):
    speed = sqrt(dx*dx + dy*dy)
    return int(degrees(asin(dx / speed)))
    

def angleToAimTarget(x):
    angle = int(degrees(acos(3.711 / 4.0)))
    if (x < LAND_X):
        return -angle
    elif (LAND_X+1000 < x):
        return angle
    else:
        return 0


# game loop
while 1:
    # HS: the horizontal speed (in m/s), can be negative.
    # VS: the vertical speed (in m/s), can be negative.
    # F: the quantity of remaining fuel in liters.
    # R: the rotation angle in degrees (-90 to 90).
    # P: the thrust power (0 to 4).
    X, Y, HS, VS, F, R, P = [int(i) for i in input().split()]
    
    angle, speed = 0, 0
    if not isOverTarget(X):
        if (goesInWrongDirection(X, HS) or goesTooFastHorizontally(HS)):
            angle, speed = angleToSlow(HS, VS), "4"
        elif goesTooSlowHorizontally(HS):
            angle, speed = angleToAimTarget(X), "4"
        else:
            angle, speed = "0", "4"
            if VS >= 0: speed = "3"
    else:
        if isFinishing(Y): angle, speed = "0", "3"
        elif hasSafeSpeed(HS, VS): angle, speed = "0", "2"
        else: angle, speed = angleToSlow(HS, VS), "4"
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    print(angle, speed) # R P. R is the desired rotation angle. P is the desired thrust power.
