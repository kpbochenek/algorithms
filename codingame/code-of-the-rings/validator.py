import sys
import os
import math


MOVE_LEFT = '<'
MOVE_RIGHT = '>'
INCREASE = '+'
DECREASE = '-'
SPELL = '.'
START_LOOP = '['
STOP_LOOP = ']'


data = sys.argv[1]

zones = [' ' for x in range(30)]
pos = 0

output = []
for command in data.strip():
    assert 0 <= pos and pos < 30
    assert len(list(filter(lambda x: ('A' <= x and x <= 'Z') or x == ' ', zones))) == 30
    if command == MOVE_LEFT:
        pos -= 1
        if pos < 0:
            pos = 29
    elif command == MOVE_RIGHT:
        pos += 1
        if pos > 29:
            pos = 0
    elif command == SPELL:
        output.append(zones[pos])
    elif command == INCREASE:
        if zones[pos] == 'Z':
            zones[pos] = ' '
        elif zones[pos] == ' ':
            zones[pos] = 'A'
        else:
            zones[pos] = chr(ord(zones[pos]) + 1)
    elif command == DECREASE:
        if zones[pos] == 'A':
            zones[pos] = ' '
        elif zones[pos] == ' ':
            zones[pos] = 'Z'
        else:
            zones[pos] = chr(ord(zones[pos]) - 1)
    else:
        print('UNKNOWN CHARACRER !!!!!!!!' + command)
print("".join(output))
