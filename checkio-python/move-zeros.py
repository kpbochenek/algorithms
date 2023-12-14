from typing import Iterable


def move_zeros(items: list[int]) -> Iterable[int]:
    result = []
    zeros = []
    for i in items:
        if i == 0: zeros.append(i)
        else: result.append(i)
    return result + zeros


print("Example:")
print(list(move_zeros([0, 1, 0, 3, 12])))

# These "asserts" are used for self-checking
assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
assert list(move_zeros([0])) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
