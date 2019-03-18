import unittest
from deckOfCards.dealer import Dealer
from deckOfCards.deck import Deck


class DealerTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck.deal(4))

    def test_dealer_cards(self):
        self.assertEqual(3, len(self.dealer.cards))
        self.assertEqual(1, len(self.dealer.hidden_card))
        self.assertNotIn(str(self.dealer.hidden_card), self.dealer.show())

    def test_dealer_reveal_bust(self):
        is_bust = self.dealer.reveal()
        self.assertEqual(is_bust, self.dealer.is_bust())

    def test_dealer_reveal(self):
        hidden_card = self.dealer.hidden_card[0]
        self.dealer.reveal()
        self.assertEqual(4, len(self.dealer.cards))
        self.assertEqual(0, len(self.dealer.hidden_card))
        self.assertIn(str(hidden_card), self.dealer.show())

