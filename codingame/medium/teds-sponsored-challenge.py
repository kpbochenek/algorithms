from collections import defaultdict

cons = int(input())
nodes = cons + 1

connections = defaultdict(set)
visited = set()

for i in range(cons):
    xi, yi = [int(i) for i in input().split()]
    connections[xi].add(yi)
    connections[yi].add(xi)


def find_max_path_and_possible_gain(visited, current_node):
    visited.add(current_node)
    root_max_path = -1
    root_max_gain = 0
    next_max_path = -1
    for neighbour in [x for x in connections[current_node] if x not in visited]:
        max_path, gain = find_max_path_and_possible_gain(visited, neighbour)
        if root_max_path < max_path:
            next_max_path = root_max_path
            root_max_path = max_path
            root_max_gain = gain
        elif root_max_path == max_path:
            root_max_gain = -1
        else:
            if next_max_path < max_path:
                next_max_path = max_path

    path_to_current = root_max_path + 1
    gain_for_current = root_max_gain + 1
    next_path_to_current = next_max_path + 1
    return path_to_current, min((path_to_current - next_path_to_current)//2, gain_for_current)

mpath, gain = find_max_path_and_possible_gain(visited, 0)
print(mpath - gain)
