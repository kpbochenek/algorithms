from collections import Counter

def most_frequent(data: list[str]) -> str:
    counts = Counter(data)
    result = ('?', 0)
    for (element, count) in counts.items():
        if count > result[1]:
            result = (element, count)
        
    return result[0]


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
