from collections.abc import Iterable


def chunking_by(items: list[int], size: int) -> Iterable[list[int]]:
    result = []
    for (i, el) in enumerate(items):
        if i % size == 0:
            result.append([])
        result[-1].append(el)
    return result


print("Example:")
print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

# These "asserts" are used for self-checking
assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []
assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
