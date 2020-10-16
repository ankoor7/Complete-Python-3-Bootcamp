import unittest
from .game_round import GameRound
from deckOfCards.player import Player
from deckOfCards.deck import Deck
from deckOfCards.dealer import Dealer
from deckOfCards.card import Card
from deckOfCards.constants import suits


class GameRoundTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.cards = [Card(suits.HEARTS, 'Two'), Card(suits.HEARTS, 'Three')]
        self.more_cards = [Card(suits.HEARTS, 'Queen'), Card(suits.HEARTS, 'King')]
        self.cash = 400
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = [
            Player(self.deck),
            Player(self.deck),
            Player(self.deck),
            Player(self.deck)
        ]

    def test_initialisation(self):
        with self.assertRaises(Exception):
            GameRound([], self.dealer)
        return

    def test_play_round(self):

        # each player has a turn in order
        # dealer plays once in turn
        return

    def test_dealer_wins(self):
        # dealer beats all players
        # dealer takes all money
        return

    def test_player_wins(self):
        # check the rules
        return


if __name__ == '__main__':
    unittest.main()
