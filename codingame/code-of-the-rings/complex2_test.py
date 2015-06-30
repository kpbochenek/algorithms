import unittest

from complex2 import *


class TestLetterDistance(unittest.TestCase):
    def test_letter_distance(self):
        self.assertEqual(letter_distance_move('A', 'C'), (2, INCREASE))
        self.assertEqual(letter_distance_move('C', 'I'), (6, INCREASE))
        self.assertEqual(letter_distance_move('C', 'A'), (2, DECREASE))
        self.assertEqual(letter_distance_move('I', 'C'), (6, DECREASE))
        
        self.assertEqual(letter_distance_move('B', 'Y'), (4, DECREASE))
        self.assertEqual(letter_distance_move('A', 'Y'), (3, DECREASE))
        self.assertEqual(letter_distance_move('B', 'Z'), (3, DECREASE))
        self.assertEqual(letter_distance_move('A', 'Z'), (2, DECREASE))

        self.assertEqual(letter_distance_move('Y', 'B'), (4, INCREASE))
        self.assertEqual(letter_distance_move('Y', 'A'), (3, INCREASE))
        self.assertEqual(letter_distance_move('Z', 'B'), (3, INCREASE))
        self.assertEqual(letter_distance_move('Z', 'A'), (2, INCREASE))

        self.assertEqual(letter_distance_move(' ', ' ')[0], 0)
        self.assertEqual(letter_distance_move('C', ' '), (3, DECREASE))
        self.assertEqual(letter_distance_move(' ', 'C'), (3, INCREASE))
        self.assertEqual(letter_distance_move('W', ' '), (4, INCREASE))
        self.assertEqual(letter_distance_move(' ', 'W'), (4, DECREASE))

    def test_zone_distance_move(self):
        self.assertEqual(zone_distance_move(1, 1)[0], 0)

        self.assertEqual(zone_distance_move(0, 3), (3, MOVE_RIGHT))
        self.assertEqual(zone_distance_move(2, 6), (4, MOVE_RIGHT))
        self.assertEqual(zone_distance_move(3, 0), (3, MOVE_LEFT))
        self.assertEqual(zone_distance_move(6, 2), (4, MOVE_LEFT))

        self.assertEqual(zone_distance_move(0, 29), (1, MOVE_LEFT))
        self.assertEqual(zone_distance_move(1, 29), (2, MOVE_LEFT))
        self.assertEqual(zone_distance_move(0, 28), (2, MOVE_LEFT))
        self.assertEqual(zone_distance_move(1, 28), (3, MOVE_LEFT))

        self.assertEqual(zone_distance_move(29, 0), (1, MOVE_RIGHT))
        self.assertEqual(zone_distance_move(29, 1), (2, MOVE_RIGHT))
        self.assertEqual(zone_distance_move(28, 0), (2, MOVE_RIGHT))
        self.assertEqual(zone_distance_move(28, 1), (3, MOVE_RIGHT))

        
if __name__ == '__main__':
    unittest.main()
