import unittest

from perudo.bet import bet


class BetTestCase(unittest.TestCase):
    def setUp(self):
        self.bet = Bet(3, "2")

    def test_initialize(self):
        self.assertEqual(self.bet.count, 3)
        self.assertEqual(self.bet.value, "2")

    def test_increase_count(self):
        self.bet.increase_count(7)
        self.assertEqual(self.bet.count, 10)

    def test_increase_value(self):
        self.bet.increase_value(2)
        self.assertEqual(self.bet.value, 4)
