def changing_direction(elements: list[int]) -> int:
    result = 0
    dir_up = "UN"
    prev = elements[0]
    for e in elements:
        if dir_up == "UN":
            if prev > e: dir_up = False
            elif prev < e: dir_up = True
        elif dir_up:
            if e < prev:
                dir_up = not dir_up
                result += 1
        elif not dir_up:
            if e > prev:
                dir_up = not dir_up
                result += 1
        prev = e
        
    return result


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
