def yaml(a: str) -> dict:
    result = {}
    for line in a.split("\n"):
        if ":" in line:
            k, v = line.split(":")
            result[k] = v.strip()
            try:
                result[k] = int(result[k])
            except:
                pass
    return result


print("Example:")
print(
    yaml(
        """name: Alex
age: 12"""
    )
)

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
