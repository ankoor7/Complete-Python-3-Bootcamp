import unittest
from .player import Player
from .card import Card
from deckOfCards import constants


class PlayerTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.cards = [Card(constants.HEARTS, 'Two'), Card(constants.HEARTS, 'Three')]
        self.more_card = [Card(constants.HEARTS, 'Queen'), Card(constants.HEARTS, 'King')]
        self.cash = 400

    def test_instantiation(self):
        this_player = Player(self.cash, self.cards)
        self.assertEqual(2, len(this_player.cards))
        self.assertEqual(400, this_player.cash)

    def test_bet(self):
        this_player = Player(self.cash, self.cards)
        result = this_player.bet(100)
        self.assertEqual(300, this_player.cash)
        self.assertEqual(100, result["bet"])
        self.assertEqual(300, result["stack_value"])

    def test_collect(self):
        this_player = Player(self.cash, self.cards)
        result = this_player.collect(100)
        self.assertEqual(500, this_player.cash)
        self.assertEqual(500, result["stack_value"])

    def test_must_have_cash(self):
        with self.assertRaises(Exception):
            Player()


if __name__ == '__main__':
    unittest.main()
