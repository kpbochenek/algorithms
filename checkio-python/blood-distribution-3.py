paths = {
    'A': ['A', 'AB'],
    'B': ['B', 'AB'],
    'AB': ['AB'],
    'O': ['O', 'A', 'B', 'AB']
}

def distribute_blood(blood_avail: dict[str, int], blood_needs: dict[str, int]) -> dict[str, dict[str, int]]:
    result = {x: {'A': 0, 'B': 0, 'AB': 0, 'O': 0} for x in ['A', 'B', 'AB', 'O']}
    if blood_needs['O'] > blood_avail['O']: return -1
    result['O']['O'] = min(blood_avail['O'], blood_needs['O'])
    additional_zero = blood_avail['O'] - blood_needs['O']

    result['A']['A'] = min(blood_avail['A'], blood_needs['A'])

    print(result)

    return result


if __name__ == "__main__":
    assert distribute_blood(
        {"A": 150, "B": 100, "AB": 0, "O": 0}, {"A": 100, "B": 100, "AB": 50, "O": 0}
    ) == {
        "A": {"A": 100, "B": 0, "AB": 50, "O": 0},
        "B": {"A": 0, "B": 100, "AB": 0, "O": 0},
        "AB": {"A": 0, "B": 0, "AB": 0, "O": 0},
        "O": {"A": 0, "B": 0, "AB": 0, "O": 0},
    }
    assert distribute_blood(
        {"A": 10, "B": 10, "AB": 20, "O": 20}, {"A": 20, "B": 10, "AB": 30, "O": 0}
    ) == {
        "A": {"A": 10, "B": 0, "AB": 0, "O": 0},
        "B": {"A": 0, "B": 10, "AB": 0, "O": 0},
        "AB": {"A": 0, "B": 0, "AB": 20, "O": 0},
        "O": {"A": 10, "B": 0, "AB": 10, "O": 0},
    }

    print("Coding complete? Click 'Check' to earn cool rewards!")
