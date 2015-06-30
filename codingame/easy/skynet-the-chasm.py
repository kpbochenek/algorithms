R = int(input())  # the length of the road before the gap.
G = int(input())  # the length of the gap.
L = int(input())  # the length of the landing platform.


while 1:
    S = int(input())  # the motorbike's speed.
    X = int(input())  # the position on the road of the motorbike.
    if X < R - 1:
        if G > S - 1:
            print("SPEED")
        elif G < S - 1:
            print("SLOW")
        else:
            print("WAIT")
    elif X > R - 1:
        print("SLOW")
    else:
        print("JUMP")
