N = int(input())
prev = None
diff = 10000005
for v in sorted([int(input()) for i in range(N)]):
    if prev is not None:
        if v - prev < diff:
            diff = v - prev
    prev = v

print(diff)
