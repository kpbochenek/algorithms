def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    def revs(st, end, rev):
        if rev: return list(range(st, end))
        else: return list(range(end-1, st-1, -1))
    return [ revs(start + i * cols, start + i * cols + cols, i % 2 == 0) for i in range(rows)]  


print("Example:")
print(create_zigzag(3, 5))

# These "asserts" are used for self-checking
assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]
print(create_zigzag(4, 2))
assert create_zigzag(4, 2) == [[1, 2], [4, 3], [5, 6], [8, 7]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
