from typing import Any, Iterable


def split_list(items: list[Any]) -> Iterable[list[Any]]:
    return [items[0:(len(items)+1)//2], items[(len(items)+1)//2:]]


print("Example:")
print(list(split_list([1, 2, 3, 4, 5, 6])))

assert list(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
assert list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])) == [
    ["banana", "apple", "orange"],
    ["cherry", "watermelon"],
]
assert list(split_list([1])) == [[1], []]
assert list(split_list([])) == [[], []]

print("The mission is done! Click 'Check Solution' to earn rewards!")
