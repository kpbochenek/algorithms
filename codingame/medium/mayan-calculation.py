L, H = [int(i) for i in input().split()]
numeral = [input() for i in range(H)]
conversion = {}
rev_conversion = {}
for i in range(20):
    value = "".join([line[i*L:(i+1)*L] for line in numeral])
    conversion[value] = i
    rev_conversion[i] = value

S1 = int(input())
num1line = [input() for i in range(S1)]

S2 = int(input())
num2line = [input() for i in range(S2)]

operation = input()


def parse(number):
    count = len(number) // H
    parsed = 0
    for i in range(count):
        value = "".join(number[i*H:(i+1)*H])
        value = conversion[value]
        parsed += value * pow(20, count - i - 1)
    return parsed


def display(number):
    line = rev_conversion[number]
    for x in range(L):
        print(line[x * L:(x + 1) * L])


def display_all(number):
    power = 0
    while pow(20, power) < number:
        power += 1
    power -= 1
    while power > 0:
        display(number // pow(20, power))
        number = number % pow(20, power)
        power -= 1

    display(number)

# To debug: print("Debug messages...", file=sys.stderr)
num1 = parse(num1line)
num2 = parse(num2line)

# print("EQUATION {} {} {} ".format(num1, operation, num2), file=sys.stderr)

result = 0
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 // num2

display_all(result)
