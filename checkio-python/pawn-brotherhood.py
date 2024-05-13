def safe_pawns(pawns: set) -> int:
    return len(list(filter(lambda p: others(p, -1) in pawns or others(p, +1) in pawns, pawns)))

def others(pawn: str, mod: int) -> str:
    return chr(ord(pawn[0])+mod) + str(int(pawn[1]) - 1)

print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"d2", "b4", "e3", "g5", "c3", "d4", "f4"}) == 6
assert safe_pawns({"g4", "c4", "b4", "e4", "e5", "d4", "f4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
