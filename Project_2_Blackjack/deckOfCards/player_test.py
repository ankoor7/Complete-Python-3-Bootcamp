import unittest
from unittest.mock import Mock
from deckOfCards.player import Player
from deckOfCards.card import Card
from deckOfCards.constants import HEARTS
from deckOfCards.hand import Hand
from deckOfCards.stack import Stack
from deckOfCards.deck import Deck


class PlayerTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.cards = [Card(HEARTS, 'Two'), Card(HEARTS, 'Three')]
        self.more_cards = [Card(HEARTS, 'Queen'), Card(HEARTS, 'King')]
        self.cash = 400
        self.deck = Deck()

    def test_instantiation(self):
        this_player = Player(self.deck, self.cash)
        self.assertIsInstance(this_player, Hand)
        self.assertIsInstance(this_player.stack, Stack)
        self.assertFalse(this_player.is_bust())

    def test_must_have_cash(self):
        with self.assertRaises(Exception):
            Player()

    def test_check_is_bust(self):
        is_bust_mock = Mock(return_value=True)
        this_player = Player(self.deck, self.cash)
        this_player.is_bust = is_bust_mock
        self.assertTrue(this_player.is_bust())


    def test_play_turn(self):
        this_player = Player(self.deck, self.cash)
        this_player.check_is_bust = Mock()
        self.deck.deal = Mock(return_value=self.more_cards[0])

        this_player.play_turn()

        self.assertIn(self.more_cards[0], this_player.cards)

    def test_play_turn_when_bust(self):
        this_player = Player(self.deck, self.cash)
        self.deck.deal = Mock(return_value=self.more_cards[0])

        this_player.is_bust = Mock(return_value=True)
        this_player.play_turn()
        self.assertNotIn(self.more_cards[0], this_player.cards)


if __name__ == '__main__':
    unittest.main()
