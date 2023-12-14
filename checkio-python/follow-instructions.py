def follow(instructions: str) -> tuple[int, int] | list[int]:
    result = [0, 0]
    for c in instructions:
        match c:
            case 'f': result = (result[0], result[1]+1)
            case 'b': result = (result[0], result[1]-1)
            case 'l': result = (result[0]-1, result[1])
            case 'r': result = (result[0]+1, result[1])
    return result


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
