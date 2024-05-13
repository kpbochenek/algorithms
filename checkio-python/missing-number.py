def missing_number(items: list[int]) -> int:
    items.sort()
    min_diff = min(items[1] - items[0], items[2] - items[1])
    for i in range(len(items)):
        if items[i+1] - items[i] != min_diff:
            return items[i] + min_diff


print("Example:")
print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
