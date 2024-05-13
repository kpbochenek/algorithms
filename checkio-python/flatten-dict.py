def flatten(dictionary: dict[str, str | dict]) -> dict[str, str]:
    return flatten2("", dictionary, {})

def flatten2(prefix: str, dictionary: str | dict, output: dict[str,str]) -> dict[str,str]:
    if isinstance(dictionary, str):
        output[prefix] = dictionary
    else:
        if len(dictionary.values()) == 0:
            output[prefix] = ""
        else:
            for k, v in dictionary.items():
                if prefix == "": flatten2(k, v, output)
                else: flatten2(prefix + "/" + k, v, output)
        return output


print("Example:")
print(flatten({"key": "value"}))

# These "asserts" are used for self-checking
assert flatten({"key": "value"}) == {"key": "value"}
assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {
    "key/deeper/more/enough": "value"
}
assert flatten({"empty": {}}) == {"empty": ""}
assert flatten(
    {
        "name": {"first": "One", "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {"place": {"zone": "1", "cell": "2"}},
    }
) == {
    "name/first": "One",
    "name/last": "Drone",
    "job": "scout",
    "recent": "",
    "additional/place/zone": "1",
    "additional/place/cell": "2",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
