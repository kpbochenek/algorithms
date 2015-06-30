L = int(input())
H = int(input())
T = input()
R = []
for i in range(H):
    ROW = input()
    chunks=[str(ROW[x:x+L]) for x in range(0, len(ROW), L)]
    R.append(chunks)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

for i in range(H):
    for letter in T.upper():
        if letter in alphabet:
            print(R[i][alphabet.find(letter)], end='')
        else:
            print(R[i][-1], end='')
    print()
