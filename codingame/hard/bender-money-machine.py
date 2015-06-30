visited = set()

N = int(input())

rooms = [None for i in range(N)]
rooms_cash = [None for i in range(N)]
best = [0 for i in range(N)]

for i in range(N):
    num, cash, l, r = input().split()
    num = int(num)
    rooms_cash[num] = int(cash)
    rooms[num] = (l, r)

max_result = 0

def visit(node, current_cash):
    global max_result
    if node in visited: return
    if node == 'E':
        max_result = max(max_result, current_cash)
        return
    node = int(node)
    if best[node] > current_cash: return
    best[node] = current_cash
    visited.add(node)
    l, r = rooms[node]
    visit(l, current_cash + rooms_cash[node])
    visit(r, current_cash + rooms_cash[node])
    visited.remove(node)

visit(0, 0)

print(max_result)
