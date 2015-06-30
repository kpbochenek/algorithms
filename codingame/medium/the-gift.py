N = int(input())
C = int(input())
funds = sorted([int(input()) for x in range(N)])

if sum(funds) < C:
    print("IMPOSSIBLE")
else:
    count = N
    deficit = 0
    result = []
    while count * (funds[0] - deficit) <= C:
        result.append(funds[0])
        C -= count * (funds[0] - deficit)
        deficit = funds[0]
        count -= 1
        funds = funds[1:]

    value = C // count
    rest = C % count
    for x in range(count - rest):
        result.append(value + deficit)
    for r in range(rest):
        result.append(value + deficit + 1)

    for r in sorted(result):
        print(r)
