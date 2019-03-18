import unittest
from .deck import Deck
from .player import Player
from .card import Card
from deckOfCards import constants


class PlayerTest(unittest.TestCase):
    def test_instantiation(self):
        this_player = Player()
        this_player.take_cards([Card(constants.HEARTS, 'Two'), Card(constants.HEARTS, 'Three')])
        self.assertEqual(2, len(this_player.cards))

    def test_take_cards(self):
        this_deck = Deck()
        this_player = Player()
        this_player.take_cards(this_deck.deal(4))

        self.assertEqual(48, len(this_deck.stack))
        self.assertEqual(4, len(this_player.cards))

    def test_total(self):
        this_player = Player()
        this_player.take_cards([Card(constants.HEARTS, 'Two'), Card(constants.HEARTS, 'Three')])
        self.assertEqual(5, this_player.total())

        this_player.take_cards([Card(constants.HEARTS, 'Four')])
        self.assertEqual(9, this_player.total())

    def test_is_bust(self):
        this_player = Player()
        this_player.take_cards([Card(constants.HEARTS, 'Two'), Card(constants.HEARTS, 'Three')])
        self.assertFalse(this_player.is_bust())

        this_player.take_cards([Card(constants.HEARTS, 'Queen'), Card(constants.HEARTS, 'King')])
        self.assertTrue(this_player.is_bust())

    def test_show_hand(self):
        this_player = Player()
        this_player.take_cards([Card(constants.HEARTS, 'Two'), Card(constants.HEARTS, 'Three')])
        self.assertSequenceEqual(['Two of Hearts', 'Three of Hearts'], this_player.show_hand())


if __name__ == '__main__':
    unittest.main()
