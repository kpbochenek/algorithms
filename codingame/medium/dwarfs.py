class Node():
    def __init__(self, idx):
        self.idx = idx
        self.parents = set()
        self.children = set()
        self.dist = 1

nodes = {}

n = int(input())  # the number of relationships of influence
for i in range(n):
    x, y = [int(i) for i in input().split()]
    xnode = nodes.get(x, Node(x))
    ynode = nodes.get(y, Node(y))
    xnode.children.add(y)
    ynode.parents.add(x)
    nodes[x] = xnode
    nodes[y] = ynode

queue = []
for n in nodes.values():
    if len(n.children) == 0:
        queue.append(n)

while len(queue) > 0:
    node = queue[0]
    queue = queue[1:]

    for pidx in node.parents:
        parent = nodes[pidx]
        parent.dist = max(parent.dist, node.dist + 1)
        parent.children.remove(node.idx)
        if len(parent.children) == 0:
            queue.append(parent)

print(max(map(lambda n: n.dist, nodes.values())))
