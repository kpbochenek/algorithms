# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# N: the total number of nodes in the level, including the gateways
# L: the number of links
# E: the number of exit gateways
N, L, E = [int(i) for i in input().split()]

nodes = [set() for i in range(N)]
gateways = set()

for i in range(L):
    # N1: N1 and N2 defines a link between these nodes
    N1, N2 = [int(i) for i in input().split()]
    nodes[N1].add(N2)
    nodes[N2].add(N1)

for i in range(E):
    EI = int(input())  # the index of a gateway node
    gateways.add(EI)


def find_last_link_to_closest_gateway(skynet_node):
    visited = set()
    q = [skynet_node]
    while True:
        current = q[0]
        q = q[1:]
        for neighbour in nodes[current]:
            if neighbour in gateways:
                return current, neighbour
            elif neighbour not in visited:
                visited.add(neighbour)
                q.append(neighbour)

while 1:
    SI = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    ft, to = find_last_link_to_closest_gateway(SI)
    nodes[ft].remove(to)
    nodes[to].remove(ft)

    print("{} {}".format(ft, to))
