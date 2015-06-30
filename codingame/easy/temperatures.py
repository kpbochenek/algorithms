N = int(input())  # the number of temperatures to analyse
if N != 0:
    diff = 100000
    TEMPS = input()
    for t in map(int, TEMPS.split(" ")):
        if abs(t) < abs(diff):
            diff = t
        if abs(t) == abs(diff):
            if t > 0 or diff > 0:
                diff = abs(t)
else:
    diff = 0

print(diff)
