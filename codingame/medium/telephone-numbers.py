root = [None for x in range(10)]
result = 0

N = int(input())
for i in range(N):
    telephone = input()
    current = root
    for x in telephone:
        if current[int(x)] is None:
            current[int(x)] = [None for x in range(10)]
            result += 1
        current = current[int(x)]

print(str(result))
