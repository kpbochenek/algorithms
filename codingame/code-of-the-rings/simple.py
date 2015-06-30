#!/bin/python

import sys, math

MOVE_LEFT = '<'
MOVE_RIGHT = '>'
INCREASE = '+'
DECREASE = '-'
SPELL = '.'
START_LOOP = '['
STOP_LOOP = ']'

magicPhrase = input().replace(' ', '@')

output = []

def out(c):
    global output
    output.append(c)


out(INCREASE)
current = 'A'

for i in magicPhrase:
    while current < i:
        out(INCREASE)
        current = chr(ord(current) + 1)
    while current > i:
        out(DECREASE)
        current = chr(ord(current) - 1)
    out(SPELL)

print("".join(output))
