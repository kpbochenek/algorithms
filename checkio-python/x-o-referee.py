def checkio(game_result: list[str]) -> str:
    for winner in ["X", "O"]:
        for i in range(3):
            if game_result[i][0] == winner and game_result[i][1] == winner and game_result[i][2] == winner:
                return winner
            if game_result[0][i] == winner and game_result[1][i] == winner and game_result[2][i] == winner:
                return winner
            if game_result[0][0] == winner and game_result[1][1] == winner and game_result[2][2] == winner:
                return winner
            if game_result[0][2] == winner and game_result[1][1] == winner and game_result[2][0] == winner:
                return winner
    return "D"


print("Example:")
print(checkio(["X.O", "XX.", "XOO"]))

# These "asserts" are used for self-checking
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

print("The mission is done! Click 'Check Solution' to earn rewards!")
