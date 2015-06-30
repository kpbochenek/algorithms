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


def gates_count(current):
    return sum([1 for n in nodes[current] if n in gateways])


def find_last_link_to_closest_gateway(skynet_node):
    visited = set()
    distance = {skynet_node: 0}
    gates = {}
    q = [skynet_node]
    while q:
        current = q[0]
        q = q[1:]
        gates[current] = gates_count(current)
        for neighbour in nodes[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                if gates_count(neighbour) > 0:
                    distance[neighbour] = distance[current]
                else:
                    distance[neighbour] = distance[current]+1
                q.append(neighbour)
        q.sort(key=lambda x: distance[x])
    for n in nodes[skynet_node]:
        if n in gateways:
            return skynet_node, n

    best_dist = 1000000
    num_gates = 1
    result = None
    for node, dist in distance.items():
        if gates[node] >= num_gates:
            if gates[node] > num_gates or dist < best_dist:
                num_gates = gates[node]
                best_dist = dist
                result = (node, list(filter(lambda x: x in gateways, nodes[node]))[0])
    return result[0], result[1]

while 1:
    SI = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # To debug: print("Debug messages...", file=sys.stderr)

    ft, to = find_last_link_to_closest_gateway(SI)
    nodes[ft].remove(to)
    nodes[to].remove(ft)

    print("{} {}".format(ft, to))
