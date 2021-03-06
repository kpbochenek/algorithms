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


A0 = ord('A') - 1
Z0 = ord('Z') + 1
ALPHABET_LEN = Z0 - A0
ZONES_LEN = 30


def letter_distance_move(l1, l2):
    l1o, l2o = ord(l1), ord(l2)
    if l1 == l2:
        return (0, INCREASE)
    if l1 == ' ':
        return min((l2o - A0, INCREASE), (Z0 - l2o, DECREASE))
    elif l2 == ' ':
        return min((Z0 - l1o, INCREASE), (l1o - A0, DECREASE))
    else:
        if l1o < l2o:
            dist = l2o - l1o
            return min((dist, INCREASE), (ALPHABET_LEN - dist, DECREASE))
        else:
            dist = l1o - l2o
            return min((dist, DECREASE), (ALPHABET_LEN - dist, INCREASE))


def zone_distance_move(z1, z2):
    if z1 == z2:
        return (0, MOVE_RIGHT)
    if z1 < z2:
        dist = z2 - z1
        return min((dist, MOVE_RIGHT), (ZONES_LEN - dist, MOVE_LEFT))
    else:
        dist = z1 - z2
        return min((dist, MOVE_LEFT), (ZONES_LEN - dist, MOVE_RIGHT))


class GameState:
    def __init__(self):
        self.zones = [' ' for x in range(ZONES_LEN)]
        self.pos = 0
        self.output = []
        self.moves = 0

    def make_move_and_change_letter(self, new_zone, new_letter):
        move = zone_distance_move(self.pos, new_zone)
        self.output.extend([move[1]] * move[0])
        self.pos = new_zone

        move = letter_distance_move(self.zones[self.pos], new_letter)
        self.output.extend([move[1]] * move[0])
        self.zones[self.pos] = new_letter

        self.moves += 1

    def clone(self):
        gs = GameState()
        gs.zones = self.zones[:]
        gs.pos = self.pos
        gs.output = self.output[:]
        gs.moves = self.moves
        return gs
        
    def score(self):
        return len(self.output)

def calculate_distance(pos, i):
    return zone_distance_move(pos, i)[0]

def calculate_change(a, b):
    return letter_distance_move(a, b)[0]


if __name__ == '__main__':
    magicPhrase = input()

    states = [GameState()]

    for letter in magicPhrase:
        global_states = []
        for state in states:
            new_states = []
            for target_zone in range(ZONES_LEN):
                d = calculate_distance(state.pos, target_zone)
                change = calculate_change(state.zones[target_zone], letter)
                new_states.append((d + change, target_zone, state))
                
            for (cost, tzone, st) in sorted(new_states)[:10]:
                cstate = st.clone()
                cstate.make_move_and_change_letter(tzone, letter)
                cstate.output.append(SPELL)
                global_states.append(cstate)
        states = sorted(global_states, key=lambda s: s.score())[:100]

    print("".join(states[0].output))
