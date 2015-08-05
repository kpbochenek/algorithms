
tasks = []

N = int(input())
for i in range(N):
    start, dur = [int(j) for j in input().split()]
    tasks.append((start + dur, start))

tasks.sort()

ending = 0
result = 0
for t in tasks:
    if t[1] >= ending:
        ending = t[0]
        result += 1

print(result)
