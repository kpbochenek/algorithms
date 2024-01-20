def is_family(tree: list[list[str]]) -> bool:
    parents = {}
    uniques = set()
    for (parent, child) in tree:
        if child in parents: return False
        if child == parent: return False
        parents[child] = parent
        uniques.add(child)
        uniques.add(parent)
    
    roots = 0
    for u in uniques:
        if u not in parents:
            roots += 1
        
    return roots == 1


print("Example:")
print(
    is_family(
        [
            ["Jack", "Mike"],
            ["Logan", "Mike"],
            ["Logan", "Jack"],
        ]
    )
)

assert is_family([["Logan", "Mike"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Alexander"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Logan"]]) == False
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Jack"]]) == False
assert (
    is_family([["Logan", "William"], ["Logan", "Jack"], ["Mike", "Alexander"]]) == False
)
assert is_family([["Jack", "Mike"], ["Logan", "Mike"], ["Logan", "Jack"]]) == False
assert is_family([['Logan', 'William'], ['Logan', 'Jack'], ['Mike', 'Mike']]) == False
assert is_family([['Logan', 'Mike'], ['Alexander', 'Jack'], ['Jack', 'Alexander']]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
