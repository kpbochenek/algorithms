#!/bin/python

import sys
import math

MOVE_LEFT = '<'
MOVE_RIGHT = '>'
INCREASE = '+'
DECREASE = '-'
SPELL = '.'
START_LOOP = '['
STOP_LOOP = ']'

magicPhrase = input()

ALPHABET_LEN = ord('Z') - ord('A') + 1
ZONES_LEN = 30

zones = [' ' for x in range(ZONES_LEN)]
pos = 0

output = []


def calculate_distance(pos, i):
    return min(abs(pos - i), 30 - abs(pos - i))
    

def calculate_change(a, b):
    if a == ' ' and b == ' ':
        return 0
    if a == ' ':
        return min(abs(ord(b) - ord('A') - 1), abs(ord('Z') + 1 - ord(b)))
    if b == ' ':
        return min(abs(ord(a) - ord('A') - 1), abs(ord('Z') + 1 - ord(a)))
        
    return min(abs(ord(a) - ord(b)), 30 - abs(ord(a) - ord(b)))

def move_to(new_zone):
    global pos, output
    if new_zone > pos:
        if new_zone - pos < pos + ZONES_LEN - new_zone: #go right
            output.extend([MOVE_RIGHT for x in range(new_zone - pos)])
        else:
            output.extend([MOVE_LEFT for x in range(pos + ZONES_LEN - new_zone)])
    elif new_zone < pos:
        if pos - new_zone < new_zone + ZONES_LEN - pos: #go left
            output.extend([MOVE_LEFT for x in range(pos - new_zone)])
        else:
            output.extend([MOVE_RIGHT for x in range(new_zone + ZONES_LEN - pos)])
    pos = new_zone

def change_letter(new_letter):
    current = zones[pos]
    nl, c = ord(new_letter), ord(current)
    if c == nl:
        return
    elif current == ' ':
        if nl - ord('A') + 1 < ord('Z') + 1 - nl: #better to go up
            output.extend([INCREASE for x in range(nl - ord('A') + 1)])
        else:
            output.extend([DECREASE for x in range(ord('Z') + 1 - nl)])
    elif new_letter == ' ':
        if ord('Z') + 1 - c < c - ord('A') + 1: #better to go up
            output.extend([INCREASE for x in range(ord('Z') + 1 - c)])
        else:
            output.extend([DECREASE for x in range(c - ord('A') + 1)])
    else:
        if (nl > c and nl - c < c - ord('A') + ord('Z') - nl + 1) or \
           (c - nl > nl - ord('A') + ord('Z') - c + 1): #better to go up
            output.extend([INCREASE for x in range(min(abs(nl - c), abs(c - ord('A') + ord('Z') - nl + 1)))])
        else:
            output.extend([DECREASE for x in range(min(abs(nl - c), abs(nl - ord('A') + ord('Z') - c + 1)))])
        
    zones[pos] = new_letter


for letter in magicPhrase:
    best_move_zone = None
    best_result = 1000000
    for i in range(ZONES_LEN):
        d = calculate_distance(pos, i)
        change = calculate_change(zones[i], letter)
        if best_result > d + change:
            best_result = d + change
            best_move_zone = i

    move_to(best_move_zone)
    change_letter(letter)
    output.append(SPELL)

print("".join(output))
