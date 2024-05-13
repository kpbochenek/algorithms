from collections.abc import Iterable

def flat_list_rec(array: list[int], result: list[int]) -> list[int]:
    for a in array:
        if isinstance(a, Iterable):
            result = flat_list_rec(a, result)
        else:
            result.append(a)
    return result
            

def flat_list(array: list[int]) -> Iterable[int]:
    return flat_list_rec(array, [])


print("Example:")
print(list(flat_list([1, 2, 3])))

# These "asserts" are used for self-checking
assert list(flat_list([1, 2, 3])) == [1, 2, 3]
assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
