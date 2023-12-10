def backward_string_by_word(text: str) -> str:
    result = ""
    word = ""
    for c in text:
        if c == " ":
            result += word
            result += " "
            word = ""
        else:
            word = c + word
    if word:
        result += word
    return result


print("Example:")
print(backward_string_by_word("World         hello"))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
