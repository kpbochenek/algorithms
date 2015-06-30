n = int(input())
vs = [int(i) for i in input().split()]
vmax = []
cmax = 0
for i in vs:
    cmax = max(cmax, i)
    vmax.append(cmax)

cmin = cmax
result = 0
for val, maxval in zip(reversed(vs), reversed(vmax)):
    cmin = min(cmin, val)
    result = min(result, cmin - maxval)

print(result)
