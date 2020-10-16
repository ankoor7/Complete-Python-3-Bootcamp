import unittest
from unittest.mock import Mock
from deckOfCards.dealer import Dealer
from deckOfCards.deck import Deck
from deckOfCards.card import Card
from deckOfCards.constants import HEARTS


class DealerTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.cards = [
            Card(HEARTS, 'Two'),
            Card(HEARTS, 'Queen'),
            Card(HEARTS, 'King')
        ]
        self.card = Card(HEARTS, 'Two')

        self.dealer.take_cards(self.cards)

    def test_dealer_first_cards(self):
        self.assertEqual(2, len(self.dealer.cards))
        self.assertEqual(1, len(self.dealer.hidden_card))
        self.assertNotIn(self.dealer.hidden_card[0], self.dealer.cards)

    def test_dealer_take_more_cards(self):
        self.dealer.take_cards(self.cards)
        self.assertEqual(5, len(self.dealer.cards))
        self.assertEqual(1, len(self.dealer.hidden_card))

    def test_dealer_is_not_bust_before_reveal(self):
        self.assertFalse(self.dealer.is_bust())

    def test_dealer_is_bust_after_reveal(self):
        self.dealer.reveal()
        self.assertTrue(self.dealer.is_bust())

    def test_dealer_reveal(self):
        hidden_card_name = str(self.dealer.hidden_card[0])
        self.dealer.reveal()
        self.assertEqual(3, len(self.dealer.cards))
        self.assertEqual(0, len(self.dealer.hidden_card))
        self.assertIn(hidden_card_name, self.dealer.show())

    def test_play_turn(self):
        this_deck = Deck()
        this_deck.deal = Mock(return_value=[self.cards[0]])
        this_dealer = Dealer(this_deck)
        this_dealer.play_turn()
        self.assertIn(self.cards[0], this_dealer.hidden_card)

        this_deck.deal.return_value = [self.cards[1]]
        this_dealer.play_turn()
        self.assertIn(self.cards[1], this_dealer.cards)

        this_dealer.is_bust = Mock(return_value=True)
        this_deck.deal.return_value = [self.cards[2]]
        this_dealer.play_turn()
        self.assertNotIn(self.cards[2], this_dealer.cards)


if __name__ == '__main__':
    unittest.main()
