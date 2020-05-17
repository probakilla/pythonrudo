""" Unit tests of the Dice class """
import unittest

from perudo.dice import Dice


DICE_VALUES = ["P", "2", "3", "4", "5", "6"]


class DiceTestCase(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_initialize(self):
        self.assertIn(self.dice.value, DICE_VALUES)

    def test_roll(self):
        self.dice.roll()
        self.assertIn(self.dice.value, DICE_VALUES)
