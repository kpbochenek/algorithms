from collections import defaultdict

points = {}
for letter in "eaionrtlsu": points[letter] = 1
for letter in "dg": points[letter] = 2
for letter in "bcmp": points[letter] = 3
for letter in "fhvwy": points[letter] = 4
for letter in "k": points[letter] = 5
for letter in "jx": points[letter] = 8
for letter in "qz": points[letter] = 10

N = int(input())
words = [input() for i in range(N)]
LETTERS = input()


def can_make(word, letters):
    parsed = defaultdict(lambda: 0)
    for l in letters:
        parsed[l] += 1
    for w in word:
        if parsed[w] <= 0:
            return False
        parsed[w] -= 1
    return True


def get_score(word, points):
    return sum([points[w] for w in word])


def calculate_score(word, letters, points):
    if can_make(word, letters):
        return get_score(word, points)
    return 0

score = 0
result = ""
for word in words:
    pts = calculate_score(word, LETTERS, points)
    if pts > score:
        score = pts
        result = word

print(result)
