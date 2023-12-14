def checkio(number: int) -> str:
    if number % 15 == 0: return "Fizz Buzz"
    if number % 3 == 0: return "Fizz"
    if number % 5 == 0: return "Buzz"
    return str(number)


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")
