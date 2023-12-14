import heapq

def cheapest_flight(costs: list, a: str, b: str) -> int:
    graph = {}
    visited = set()
    for (c_from, c_to, price) in costs:
        if not c_from in graph: graph[c_from] = []
        graph[c_from].append((c_to, price))

        if not c_to in graph: graph[c_to] = []
        graph[c_to].append((c_from, price))

    Q = []
    if b not in graph: return 0

    heapq.heappush(Q, (0, b))
    while Q:
        (cost, current) = heapq.heappop(Q)
        if current == a: return cost
        if current in visited: continue

        visited.add(current)
        for (dest, price) in graph[current]:
            heapq.heappush(Q, (cost+price, dest))


    print(graph)
    return 0


print("Example:")
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)
assert (
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    )
    == 25
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
