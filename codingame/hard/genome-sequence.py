import itertools


def remove_contains(elems):
    result = set()
    for e in elems:
        for r in elems:
            if e in r and e != r:
                break
        else:
            result.add(e)
    return result

def calculate_common_section(a, b):
    common = 0
    for i in range(1, len(b)+1):
        if a[-i:] == b[:i]:
            common = i
    return common
        

def calculate(perm):
    current = ""
    result = 0
    for p in perm:
        common = calculate_common_section(current, p)
        current += p[common:]
        result += len(p) - common
    return result


N = int(input())
gen = []

gen = [input() for i in range(N)]

result = sum([len(g) for g in gen])

for perm in itertools.permutations(remove_contains(gen)):
    result = min(result, calculate(perm))
    
print(result)
