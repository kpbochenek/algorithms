while 1:
    SX, SY = [int(i) for i in input().split()]
    val = 0
    px = 0
    for i in range(8):
        MH = int(input())
        if val < MH:
            val = MH
            px = i

    if px == SX:
        print("FIRE")
    else:
        print("HOLD")
