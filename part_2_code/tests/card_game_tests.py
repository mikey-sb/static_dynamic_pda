import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.ace = Card('Hearts', 1)
        self.two = Card('Diamonds', 2)
        self.card_game = CardGame()
        self.cards = [self.ace, self.two]

    def test_check_for_is_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.ace))

    def test_check_for_is_not_ace(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.two))

    def test_for_highest_card(self):
        self.assertEqual(self.two, self.card_game.highest_card(self.ace, self.two))

    def test_for_total(self):
      self.assertEqual("You have a total of 3", self.card_game.cards_total(self.cards))

    